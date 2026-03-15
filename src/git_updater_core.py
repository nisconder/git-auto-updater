#!/usr/bin/env python3
import subprocess
import time
from datetime import datetime
from pathlib import Path
from typing import Callable, List, Optional, Tuple


class GitUpdaterCore:
    def __init__(
        self,
        local_path: str,
        remote_url: Optional[str] = None,
        check_interval: int = 300,
        logger: Optional[Callable[[str], None]] = None,
    ):
        self.local_path = Path(local_path)
        self.remote_url = remote_url
        self.check_interval = check_interval
        self._logger = logger

    @staticmethod
    def _is_identity_write_command(command: List[str]) -> bool:
        if len(command) < 2:
            return False
        if command[0] != 'git' or command[1] != 'config':
            return False

        tokens = [part.lower() for part in command[2:]]
        has_identity_key = any(token in ('user.name', 'user.email') for token in tokens)
        if not has_identity_key:
            return False

        read_only_flags = {
            '--get', '--get-all', '--get-regexp', '--list', '-l',
            '--show-origin', '--show-scope', '--name-only', '--null', '-z'
        }
        is_read_only = any(token in read_only_flags for token in tokens)
        return not is_read_only

    def log(self, message: str) -> None:
        if self._logger:
            self._logger(message)
            return

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        repo_name = self.local_path.name
        print(f"[{timestamp}] [{repo_name}] {message}")

    def run_command(self, command: List[str], cwd: Optional[Path] = None) -> Tuple[bool, str]:
        if self._is_identity_write_command(command):
            return False, "安全保护：禁止通过本工具修改 git user.name/user.email，请手动执行 git config。"

        try:
            result = subprocess.run(
                command,
                cwd=cwd or self.local_path,
                capture_output=True,
                text=True,
                check=False,
            )
            output = result.stdout.strip()
            error = result.stderr.strip()
            combined_output = "\n".join(part for part in [output, error] if part)
            return result.returncode == 0, combined_output
        except Exception as e:
            return False, str(e)

    def list_remotes(self) -> List[str]:
        success, output = self.run_command(['git', 'remote'])
        if not success or not output:
            return []
        return [line.strip() for line in output.splitlines() if line.strip()]

    def get_remote_url(self, remote_name: str) -> Optional[str]:
        success, output = self.run_command(['git', 'remote', 'get-url', remote_name])
        if success and output:
            return output.strip()
        return None

    def get_remote_by_url(self, remote_url: str) -> Optional[str]:
        for remote_name in self.list_remotes():
            url = self.get_remote_url(remote_name)
            if url == remote_url:
                return remote_name
        return None

    def get_upstream_remote(self) -> Optional[str]:
        success, output = self.run_command(['git', 'rev-parse', '--abbrev-ref', '--symbolic-full-name', '@{u}'])
        if not success or not output or '/' not in output:
            return None
        return output.split('/', 1)[0]

    def get_current_branch(self) -> Optional[str]:
        success, output = self.run_command(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
        if success and output and output != 'HEAD':
            return output
        return None

    def get_local_commit(self) -> Optional[str]:
        success, output = self.run_command(['git', 'rev-parse', 'HEAD'])
        if success and output:
            return output
        return None

    def get_remote_ref(self) -> str:
        branch = self.get_current_branch()
        if branch:
            return f"refs/heads/{branch}"
        return 'HEAD'

    def resolve_remote_name(self) -> Optional[str]:
        remotes = self.list_remotes()

        if self.remote_url:
            matched = self.get_remote_by_url(self.remote_url)
            if matched:
                return matched

            if 'origin' not in remotes:
                success, output = self.run_command(['git', 'remote', 'add', 'origin', self.remote_url])
                if not success:
                    self.log(f"添加 origin 失败: {output}")
                    return None
                self.log("已添加 origin 并绑定配置的 remote URL")
                return 'origin'

            origin_url = self.get_remote_url('origin')
            if origin_url != self.remote_url:
                success, output = self.run_command(['git', 'remote', 'set-url', 'origin', self.remote_url])
                if not success:
                    self.log(f"origin URL 与配置不一致，且修正失败: {output}")
                    return None
                self.log("origin URL 与配置不一致，已自动修正")
            return 'origin'

        upstream_remote = self.get_upstream_remote()
        if upstream_remote:
            return upstream_remote

        if 'origin' in remotes:
            return 'origin'

        if remotes:
            return remotes[0]

        return None

    def get_remote_commit(self, remote_name: str) -> Optional[str]:
        remote_ref = self.get_remote_ref()
        success, output = self.run_command(['git', 'ls-remote', remote_name, remote_ref])
        if success and output:
            return output.split()[0]
        return None

    def is_working_tree_dirty(self) -> bool:
        success, output = self.run_command(['git', 'status', '--porcelain'])
        if not success:
            return True
        return bool(output.strip())

    def update_repo(self) -> bool:
        self.log("开始更新仓库...")

        remote_name = self.resolve_remote_name()
        if not remote_name:
            self.log("未找到可用远端，跳过更新")
            return False

        success, output = self.run_command(['git', 'fetch', remote_name])
        if not success:
            self.log(f"fetch 失败: {output}")
            return False

        if self.is_working_tree_dirty():
            self.log("检测到未提交改动或未跟踪文件，已跳过自动更新（避免覆盖本地工作）")
            return False

        branch = self.get_current_branch()
        if not branch:
            self.log("当前为 detached HEAD，已跳过自动更新")
            return False

        merge_target = f"{remote_name}/{branch}"
        success, output = self.run_command(['git', 'merge', '--ff-only', merge_target])
        if not success:
            self.log(f"快进更新失败（可能存在分叉提交）: {output}")
            return False

        self.log("仓库更新成功")
        return True

    def check_and_update(self) -> bool:
        if not self.local_path.exists():
            return False

        remote_name = self.resolve_remote_name()
        if not remote_name:
            self.log("未找到可用远端")
            return False

        remote_commit = self.get_remote_commit(remote_name)
        local_commit = self.get_local_commit()

        if not remote_commit or not local_commit:
            self.log("无法获取提交信息")
            return False

        if remote_commit != local_commit:
            self.log(f"检测到更新: {local_commit[:8]} -> {remote_commit[:8]}")
            return self.update_repo()

        return False

    def clone_if_not_exists(self) -> bool:
        if self.local_path.exists():
            return False

        if not self.remote_url:
            self.log("仓库不存在且未配置 remote URL，无法克隆")
            return False

        self.log(f"仓库不存在，开始克隆: {self.remote_url}")
        parent_dir = self.local_path.parent
        parent_dir.mkdir(parents=True, exist_ok=True)

        success, output = self.run_command(['git', 'clone', self.remote_url, str(self.local_path)], cwd=parent_dir)
        if success:
            self.log("克隆成功")
            return True

        self.log(f"克隆失败: {output}")
        return False

    def run_once(self) -> None:
        self.clone_if_not_exists()
        if self.local_path.exists():
            self.check_and_update()

    def run_forever(self) -> None:
        self.clone_if_not_exists()
        while True:
            if self.local_path.exists():
                self.check_and_update()
            time.sleep(self.check_interval)
