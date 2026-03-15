#!/usr/bin/env python3
import time
from pathlib import Path
from typing import Optional

from git_updater_core import GitUpdaterCore


def positive_int(value: str) -> int:
    interval = int(value)
    if interval <= 0:
        raise ValueError
    return interval

class GitAutoUpdater:
    def __init__(self, repo_path: str, check_interval: int = 300):
        self.repo_path = Path(repo_path)
        self.core = GitUpdaterCore(repo_path, check_interval=check_interval, logger=self._log)

    def run_command(self, command: list[str], cwd: Optional[Path] = None) -> tuple[bool, str]:
        return self.core.run_command(command, cwd=cwd)

    def _log(self, message: str) -> None:
        print(message)

    def get_current_branch(self) -> Optional[str]:
        return self.core.get_current_branch()

    def get_local_commit(self) -> Optional[str]:
        return self.core.get_local_commit()

    def check_and_update(self) -> bool:
        return self.core.check_and_update()

    def update_repo(self) -> bool:
        return self.core.update_repo()

    def clone_if_not_exists(self, remote_url: str) -> bool:
        self.core.remote_url = remote_url
        return self.core.clone_if_not_exists()

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
            print(f"等待 {self.core.check_interval} 秒后再次检查...")
            time.sleep(self.core.check_interval)


def main():
    import argparse

    def parse_interval(value: str) -> int:
        try:
            return positive_int(value)
        except (TypeError, ValueError):
            raise argparse.ArgumentTypeError('interval must be a positive integer')
    
    parser = argparse.ArgumentParser(description='Git repository auto updater')
    parser.add_argument('repo_path', help='Local repository path')
    parser.add_argument('--remote', '-r', help='Remote repository URL (used for first clone)')
    parser.add_argument('--interval', '-i', type=parse_interval, default=300,
                       help='Check interval in seconds (positive integer), default: 300 (5 min)')
    parser.add_argument('--once', action='store_true',
                       help='Run one check only, then exit')
    
    args = parser.parse_args()
    
    updater = GitAutoUpdater(args.repo_path, args.interval)
    
    if args.once:
        updater.run_once(args.remote)
    else:
        updater.run_forever(args.remote)


if __name__ == '__main__':
    main()
