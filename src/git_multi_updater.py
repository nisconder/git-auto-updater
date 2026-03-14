#!/usr/bin/env python3
import os
import subprocess
import time
from pathlib import Path
from typing import Optional, List, Tuple
import threading
from datetime import datetime


class GitRepoManager:
    def __init__(self, local_path: str, remote_url: str, check_interval: int = 300):
        self.local_path = Path(local_path)
        self.remote_url = remote_url
        self.check_interval = check_interval
        self.current_commit = None

    def run_command(self, command: list[str], cwd: Optional[Path] = None) -> Tuple[bool, str]:
        try:
            result = subprocess.run(
                command,
                cwd=cwd or self.local_path,
                capture_output=True,
                text=True,
                check=False
            )
            return result.returncode == 0, result.stdout.strip()
        except Exception as e:
            return False, str(e)

    def get_remote_commit(self) -> Optional[str]:
        success, output = self.run_command(['git', 'ls-remote', 'origin', 'HEAD'])
        if success and output:
            return output.split()[0]
        return None

    def get_local_commit(self) -> Optional[str]:
        success, output = self.run_command(['git', 'rev-parse', 'HEAD'])
        if success and output:
            return output
        return None

    def check_and_update(self) -> bool:
        if not self.local_path.exists():
            return False

        remote_commit = self.get_remote_commit()
        local_commit = self.get_local_commit()

        if not remote_commit or not local_commit:
            return False

        if remote_commit != local_commit:
            self.log(f"检测到更新: {local_commit[:8]} -> {remote_commit[:8]}")
            return self.update_repo()
        
        return False

    def update_repo(self) -> bool:
        self.log("开始更新仓库...")
        
        success, output = self.run_command(['git', 'fetch', 'origin'])
        if not success:
            self.log(f"fetch 失败: {output}")
            return False

        success, output = self.run_command(['git', 'reset', '--hard', 'origin/HEAD'])
        if not success:
            self.log(f"reset 失败: {output}")
            return False

        success, output = self.run_command(['git', 'clean', '-fd'])
        if not success:
            self.log(f"clean 失败: {output}")
            return False

        self.log("仓库更新成功")
        return True

    def clone_if_not_exists(self) -> bool:
        if not self.local_path.exists():
            self.log(f"仓库不存在，开始克隆: {self.remote_url}")
            parent_dir = self.local_path.parent
            
            if not parent_dir.exists():
                parent_dir.mkdir(parents=True)
            
            success, output = self.run_command([
                'git', 'clone', self.remote_url, str(self.local_path)
            ], cwd=parent_dir)
            
            if success:
                self.log("克隆成功")
                return True
            else:
                self.log(f"克隆失败: {output}")
                return False
        return False

    def log(self, message: str) -> None:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        repo_name = self.local_path.name
        print(f"[{timestamp}] [{repo_name}] {message}")

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


class MultiRepoManager:
    def __init__(self, config_file: str):
        self.config_file = Path(config_file)
        self.repos: List[GitRepoManager] = []
        self.threads: List[threading.Thread] = []

    def load_config(self) -> None:
        if not self.config_file.exists():
            print(f"配置文件不存在: {self.config_file}")
            return

        with open(self.config_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                
                parts = line.split('|')
                if len(parts) == 2:
                    local_path, remote_url = parts
                    self.repos.append(GitRepoManager(local_path.strip(), remote_url.strip()))

    def run_all_once(self) -> None:
        print(f"开始检查 {len(self.repos)} 个仓库...")
        for repo in self.repos:
            repo.run_once()

    def run_all_forever(self) -> None:
        print(f"开始监控 {len(self.repos)} 个仓库...")
        
        for repo in self.repos:
            thread = threading.Thread(target=repo.run_forever, daemon=True)
            thread.start()
            self.threads.append(thread)

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n停止监控...")

    def print_status(self) -> None:
        print("仓库状态:")
        print("-" * 50)
        for repo in self.repos:
            exists = "✓" if repo.local_path.exists() else "✗"
            print(f"{exists} {repo.local_path}")
            print(f"   Remote: {repo.remote_url}")
            if repo.local_path.exists():
                local_commit = repo.get_local_commit()
                print(f"   本地: {local_commit[:8] if local_commit else 'N/A'}")
        print("-" * 50)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Git仓库自动更新工具（多仓库版本）')
    parser.add_argument('--config', '-c', default='git_repos.txt',
                       help='配置文件路径，默认为 git_repos.txt')
    parser.add_argument('--interval', '-i', type=int, default=300,
                       help='检查间隔（秒），默认300秒（5分钟）')
    parser.add_argument('--once', action='store_true',
                       help='只检查一次，不持续运行')
    parser.add_argument('--status', '-s', action='store_true',
                       help='显示所有仓库状态')
    
    args = parser.parse_args()
    
    manager = MultiRepoManager(args.config)
    manager.load_config()

    if not manager.repos:
        print("没有找到配置的仓库")
        return

    for repo in manager.repos:
        repo.check_interval = args.check_interval

    if args.status:
        manager.print_status()
    elif args.once:
        manager.run_all_once()
    else:
        manager.run_all_forever()


if __name__ == '__main__':
    main()
