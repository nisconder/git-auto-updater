#!/usr/bin/env python3
"""
环境检查脚本
检查 Git 和 Python 环境是否满足要求
"""
import sys
import subprocess
from pathlib import Path


def check_python_version():
    """检查 Python 版本"""
    print(f"Python 版本: {sys.version}")
    major, minor = sys.version_info[:2]
    if major == 3 and minor >= 8:
        print("✓ Python 版本满足要求 (>= 3.8)")
        return True
    else:
        print("✗ Python 版本不满足要求，需要 3.8 或更高版本")
        return False


def check_git():
    """检查 Git 是否安装"""
    try:
        result = subprocess.run(['git', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ Git 版本: {result.stdout.strip()}")
            return True
        else:
            print("✗ Git 未安装或不在 PATH 中")
            return False
    except FileNotFoundError:
        print("✗ Git 未安装")
        return False


def check_files():
    """检查必要文件是否存在"""
    required_files = [
        'src/git_auto_updater.py',
        'src/git_multi_updater.py',
        'git_repos.example.txt',
    ]
    
    print("\n检查项目文件:")
    all_exist = True
    for file in required_files:
        path = Path(file)
        if path.exists():
            print(f"✓ {file}")
        else:
            print(f"✗ {file} 不存在")
            all_exist = False
    
    return all_exist


def test_script():
    """测试脚本是否能正常运行"""
    print("\n测试脚本:")
    try:
        result = subprocess.run(
            [sys.executable, 'src/git_auto_updater.py', '--help'],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print("✓ git_auto_updater.py 可以正常运行")
            return True
        else:
            print("✗ git_auto_updater.py 运行失败")
            return False
    except Exception as e:
        print(f"✗ git_auto_updater.py 运行失败: {e}")
        return False


def main():
    print("=" * 60)
    print("Git Auto Updater 环境检查")
    print("=" * 60)
    
    checks = [
        ("Python 版本", check_python_version),
        ("Git 安装", check_git),
        ("项目文件", check_files),
        ("脚本测试", test_script),
    ]
    
    results = []
    for name, check_func in checks:
        print(f"\n{name}:")
        result = check_func()
        results.append((name, result))
    
    print("\n" + "=" * 60)
    print("检查结果汇总:")
    print("=" * 60)
    
    all_passed = True
    for name, result in results:
        status = "✓ 通过" if result else "✗ 失败"
        print(f"{name}: {status}")
        if not result:
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("\n✓ 所有检查通过！你可以开始使用 Git Auto Updater 了")
        print("\n快速开始:")
        print("  1. 查看 QUICKSTART.md 了解基本用法")
        print("  2. 查看 README.md 了解完整功能")
        return 0
    else:
        print("\n✗ 部分检查失败，请解决上述问题后重试")
        return 1


if __name__ == '__main__':
    sys.exit(main())
