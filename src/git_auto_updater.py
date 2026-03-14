#!/usr/bin/env python3
import subprocess
import time
from pathlib import Path
from typing import Optional


def positive_int(value: str) -> int:
    interval = int(value)
    if interval <= 0:
        raise ValueError
    return interval

class GitAutoUpdater:
    def __init__(self, repo_path: str, check_interval: int = 300):
        self.repo_path = Path(repo_path)
        self.check_interval = check_interval
        self.current_commit = None

    def run_command(self, command: list[str], cwd: Optional[Path] = None) -> tuple[bool, str]:
        try:
            result = subprocess.run(
                command,
                cwd=cwd or self.repo_path,
                capture_output=True,
                text=True,
                check=False
            )
            output = result.stdout.strip()
            error = result.stderr.strip()
            combined_output = "\n".join(part for part in [output, error] if part)
            return result.returncode == 0, combined_output
        except Exception as e:
            return False, str(e)

    def get_remote_commit(self) -> Optional[str]:
        remote_ref = self.get_remote_ref()
        success, output = self.run_command([
            'git', 'ls-remote', 'origin', remote_ref
        ])
        if success and output:
            return output.split()[0]
        return None

    def get_remote_ref(self) -> str:
        branch = self.get_current_branch()
        if branch:
            return f"refs/heads/{branch}"
        return 'HEAD'

    def get_reset_target(self) -> str:
        branch = self.get_current_branch()
        if branch:
            return f"origin/{branch}"
        return 'origin/HEAD'

    def get_current_branch(self) -> Optional[str]:
        success, output = self.run_command([
            'git', 'rev-parse', '--abbrev-ref', 'HEAD'
        ])
        if success and output and output != 'HEAD':
            return output
        return None

    def get_local_commit(self) -> Optional[str]:
        success, output = self.run_command([
            'git', 'rev-parse', 'HEAD'
        ])
        if success and output:
            return output
        return None

    def check_and_update(self) -> bool:
        remote_commit = self.get_remote_commit()
        local_commit = self.get_local_commit()

        if not remote_commit or not local_commit:
            print("无法获取提交信息")
            return False

        if remote_commit != local_commit:
            print(f"检测到更新: {local_commit[:8]} -> {remote_commit[:8]}")
            return self.update_repo()
        
        print("没有更新")
        return False

    def update_repo(self) -> bool:
        print("开始更新仓库...")
        reset_target = self.get_reset_target()
        
        success, output = self.run_command(['git', 'fetch', 'origin'])
        if not success:
            print(f"fetch 失败: {output}")
            return False

        success, output = self.run_command(['git', 'reset', '--hard', reset_target])
        if not success:
            print(f"reset 失败: {output}")
            return False

        success, output = self.run_command(['git', 'clean', '-fd'])
        if not success:
            print(f"clean 失败: {output}")
            return False

        print("仓库更新成功")
        return True

    def clone_if_not_exists(self, remote_url: str) -> bool:
        if not self.repo_path.exists():
            print(f"仓库不存在，开始克隆: {remote_url}")
            parent_dir = self.repo_path.parent
            parent_dir.mkdir(parents=True, exist_ok=True)
            
            success, output = self.run_command([
                'git', 'clone', remote_url, str(self.repo_path)
            ], cwd=parent_dir)
            
            if success:
                print("克隆成功")
                return True
            else:
                print(f"克隆失败: {output}")
                return False
        return False

    def run_once(self, remote_url: Optional[str] = None) -> None:
        if remote_url:
            self.clone_if_not_exists(remote_url)
        
        if self.repo_path.exists():
            self.check_and_update()
        else:
            print(f"仓库路径不存在: {self.repo_path}，请提供 --remote 用于首次克隆")

    def run_forever(self, remote_url: Optional[str] = None) -> None:
        if remote_url:
            self.clone_if_not_exists(remote_url)
        
        while True:
            if self.repo_path.exists():
                self.check_and_update()
            else:
                print(f"仓库路径不存在: {self.repo_path}，请提供 --remote 用于首次克隆")
            print(f"等待 {self.check_interval} 秒后再次检查...")
            time.sleep(self.check_interval)


def main():
    import argparse

    def parse_interval(value: str) -> int:
        try:
            return positive_int(value)
        except (TypeError, ValueError):
            raise argparse.ArgumentTypeError('interval must be a positive integer')
    
    parser = argparse.ArgumentParser(description='Git仓库自动更新工具')
    parser.add_argument('repo_path', help='本地仓库路径')
    parser.add_argument('--remote', '-r', help='远程仓库URL（首次克隆时使用）')
    parser.add_argument('--interval', '-i', type=parse_interval, default=300,
                       help='检查间隔（秒，正整数），默认300秒（5分钟）')
    parser.add_argument('--once', action='store_true',
                       help='只检查一次，不持续运行')
    
    args = parser.parse_args()
    
    updater = GitAutoUpdater(args.repo_path, args.interval)
    
    if args.once:
        updater.run_once(args.remote)
    else:
        updater.run_forever(args.remote)


if __name__ == '__main__':
    main()
