#!/usr/bin/env python3
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import List
from datetime import datetime

from git_updater_core import GitUpdaterCore


def positive_int(value: str) -> int:
    interval = int(value)
    if interval <= 0:
        raise ValueError
    return interval


class GitRepoManager(GitUpdaterCore):
    def __init__(self, local_path: str, remote_url: str, check_interval: int = 300):
        super().__init__(local_path, remote_url=remote_url, check_interval=check_interval, logger=self.log)

    def log(self, message: str) -> None:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        repo_name = self.local_path.name
        print(f"[{timestamp}] [{repo_name}] {message}")


class MultiRepoManager:
    def __init__(self, config_file: str, max_workers: int = 4):
        self.config_file = Path(config_file)
        self.repos: List[GitRepoManager] = []
        self.max_workers = max_workers

    def load_config(self) -> None:
        if not self.config_file.exists():
            print(f"配置文件不存在: {self.config_file}")
            return

        self.repos.clear()
        with open(self.config_file, 'r', encoding='utf-8') as f:
            for line_number, line in enumerate(f, start=1):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                
                parts = line.split('|', 1)
                if len(parts) == 2:
                    local_path, remote_url = parts
                    self.repos.append(GitRepoManager(local_path.strip(), remote_url.strip()))
                else:
                    print(f"忽略无效配置行 {line_number}: {line}")

    def run_all_once(self) -> None:
        print(f"开始检查 {len(self.repos)} 个仓库...")
        worker_count = max(1, min(self.max_workers, len(self.repos)))

        with ThreadPoolExecutor(max_workers=worker_count) as executor:
            future_map = {executor.submit(repo.run_once): repo for repo in self.repos}
            for future in as_completed(future_map):
                repo = future_map[future]
                try:
                    future.result()
                except Exception as e:
                    print(f"[{repo.local_path.name}] 任务执行异常: {e}")

    def run_all_forever(self) -> None:
        print(f"开始监控 {len(self.repos)} 个仓库（最大并发线程: {self.max_workers}）...")
        if not self.repos:
            return

        interval = min(repo.check_interval for repo in self.repos)

        try:
            while True:
                self.run_all_once()
                print(f"等待 {interval} 秒后再次检查...")
                time.sleep(interval)
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

    def parse_interval(value: str) -> int:
        try:
            return positive_int(value)
        except (TypeError, ValueError):
            raise argparse.ArgumentTypeError('interval must be a positive integer')
    
    parser = argparse.ArgumentParser(description='Git repository auto updater (multi-repo)')
    parser.add_argument('--config', '-c', default='git_repos.txt',
                       help='Config file path, default: git_repos.txt')
    parser.add_argument('--interval', '-i', type=parse_interval, default=300,
                       help='Check interval in seconds (positive integer), default: 300 (5 min)')
    parser.add_argument('--once', action='store_true',
                       help='Run one check only, then exit')
    parser.add_argument('--status', '-s', action='store_true',
                       help='Print status for all repositories')
    parser.add_argument('--workers', '-w', type=parse_interval, default=4,
                       help='Max worker threads for multi-repo checks (positive integer), default: 4')
    
    args = parser.parse_args()
    
    manager = MultiRepoManager(args.config, max_workers=args.workers)
    manager.load_config()

    if not manager.repos:
        print("没有找到配置的仓库")
        return

    for repo in manager.repos:
        repo.check_interval = args.interval

    if args.status:
        manager.print_status()
    elif args.once:
        manager.run_all_once()
    else:
        manager.run_all_forever()


if __name__ == '__main__':
    main()
