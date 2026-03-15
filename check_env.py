#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Environment check script
Check if Git and Python environment meets requirements
"""
import sys
import subprocess
import io
from pathlib import Path

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def check_python_version():
    """Check Python version"""
    print(f"Python version: {sys.version}")
    major, minor = sys.version_info[:2]
    if major == 3 and minor >= 8:
        print("[OK] Python version meets requirements (>= 3.8)")
        return True
    else:
        print("[FAIL] Python version does not meet requirements, need 3.8 or higher")
        return False


def check_git():
    """Check if Git is installed"""
    try:
        result = subprocess.run(['git', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"[OK] Git version: {result.stdout.strip()}")
            return True
        else:
            print("[FAIL] Git is not installed or not in PATH")
            return False
    except FileNotFoundError:
        print("[FAIL] Git is not installed")
        return False


def check_files():
    """Check if required files exist"""
    required_files = [
        'src/git_auto_updater.py',
        'src/git_multi_updater.py',
        'git_repos.example.txt',
    ]
    
    print("\nChecking project files:")
    all_exist = True
    for file in required_files:
        path = Path(file)
        if path.exists():
            print(f"[OK] {file}")
        else:
            print(f"[FAIL] {file} does not exist")
            all_exist = False
    
    return all_exist


def test_script():
    """Test if scripts can run properly"""
    print("\nTesting scripts:")
    try:
        result = subprocess.run(
            [sys.executable, 'src/git_auto_updater.py', '--help'],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print("[OK] git_auto_updater.py can run properly")
            return True
        else:
            print("[FAIL] git_auto_updater.py failed to run")
            return False
    except Exception as e:
        print(f"[FAIL] git_auto_updater.py failed to run: {e}")
        return False


def main():
    print("=" * 60)
    print("Git Auto Updater Environment Check")
    print("=" * 60)
    
    checks = [
        ("Python version", check_python_version),
        ("Git installation", check_git),
        ("Project files", check_files),
        ("Script test", test_script),
    ]
    
    results = []
    for name, check_func in checks:
        print(f"\n{name}:")
        result = check_func()
        results.append((name, result))
    
    print("\n" + "=" * 60)
    print("Check Results Summary:")
    print("=" * 60)
    
    all_passed = True
    for name, result in results:
        status = "[PASS]" if result else "[FAIL]"
        print(f"{name}: {status}")
        if not result:
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("\n[OK] All checks passed! You can start using Git Auto Updater")
        print("\nQuick Start:")
        print("  1. Check QUICK_START.md for basic usage")
        print("  2. Check README.md for full features")
        return 0
    else:
        print("\n[FAIL] Some checks failed, please fix the issues above and retry")
        return 1


if __name__ == '__main__':
    sys.exit(main())

