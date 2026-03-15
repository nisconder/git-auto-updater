#!/usr/bin/env python3
"""
Simple test script for Git Auto Updater
"""
import subprocess
import sys
import tempfile
from pathlib import Path


def run_command(cmd, cwd=None):
    """Run a command and return the result"""
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return result.returncode == 0, result.stdout, result.stderr


def test_help_commands():
    """Test that help commands work"""
    print("Testing help commands...")
    
    tests = [
        ([sys.executable, 'check_env.py'], 'Environment check'),
        ([sys.executable, 'src/git_auto_updater.py', '--help'], 'Single repo help'),
        ([sys.executable, 'src/git_multi_updater.py', '--help'], 'Multi repo help'),
    ]
    
    all_passed = True
    for cmd, name in tests:
        success, stdout, stderr = run_command(cmd)
        status = "PASS" if success else "FAIL"
        print(f"  [{status}] {name}")
        if not success:
            print(f"    Error: {stderr}")
            all_passed = False
    
    return all_passed


def test_config_file():
    """Test that example config file exists and is readable"""
    print("\nTesting configuration file...")
    
    config_file = Path('git_repos.example.txt')
    if config_file.exists():
        print("  [PASS] Example config file exists")
        
        try:
            content = config_file.read_text(encoding='utf-8')
            if '#' in content:
                print("  [PASS] Config file contains comments")
                return True
        except Exception as e:
            print(f"  [FAIL] Could not read config file: {e}")
            return False
    else:
        print("  [FAIL] Example config file not found")
        return False


def test_documentation():
    """Test that all documentation files exist"""
    print("\nTesting documentation...")
    
    doc_files = [
        'README.md',
        'QUICK_START.md',
        'INSTALL.md',
        'CHANGELOG.md',
        'CONTRIBUTING.md',
        'AUTHORS.md',
        'SECURITY.md',
        'examples/USAGE_EXAMPLES.md',
    ]
    
    all_exist = True
    for doc_file in doc_files:
        path = Path(doc_file)
        status = "PASS" if path.exists() else "FAIL"
        print(f"  [{status}] {doc_file}")
        if not path.exists():
            all_exist = False
    
    return all_exist


def test_source_files():
    """Test that source files are present"""
    print("\nTesting source files...")
    
    source_files = [
        'src/git_auto_updater.py',
        'src/git_multi_updater.py',
    ]
    
    all_exist = True
    for source_file in source_files:
        path = Path(source_file)
        status = "PASS" if path.exists() else "FAIL"
        print(f"  [{status}] {source_file}")
        if not path.exists():
            all_exist = False
    
    return all_exist


def test_import():
    """Test that source files can be imported"""
    print("\nTesting Python imports...")
    
    tests = [
        ('git_auto_updater', 'Single repo module'),
        ('git_multi_updater', 'Multi repo module'),
    ]
    
    all_passed = True
    for module, name in tests:
        try:
            # Add src to path
            import sys
            src_path = Path('src')
            if str(src_path) not in sys.path:
                sys.path.insert(0, str(src_path))
            
            __import__(module)
            print(f"  [PASS] {name} can be imported")
        except Exception as e:
            print(f"  [FAIL] {name} import failed: {e}")
            all_passed = False
    
    return all_passed


def test_invalid_interval_arguments():
    """Test that invalid interval values are rejected"""
    print("\nTesting interval argument validation...")

    tests = [
        ([sys.executable, 'src/git_auto_updater.py', 'dummy_repo', '--interval', '0', '--once'], 'Single repo interval=0'),
        ([sys.executable, 'src/git_auto_updater.py', 'dummy_repo', '--interval', '-1', '--once'], 'Single repo interval=-1'),
        ([sys.executable, 'src/git_multi_updater.py', '--interval', '0', '--once'], 'Multi repo interval=0'),
        ([sys.executable, 'src/git_multi_updater.py', '--interval', '-1', '--once'], 'Multi repo interval=-1'),
    ]

    all_passed = True
    for cmd, name in tests:
        success, stdout, stderr = run_command(cmd)
        status = "PASS" if not success else "FAIL"
        print(f"  [{status}] {name}")
        if success:
            all_passed = False
            continue

        combined_output = f"{stdout}\n{stderr}"
        expected_markers = [
            'interval must be a positive integer',
            'interval 必须是正整数',
        ]
        if not any(marker in combined_output for marker in expected_markers):
            print("    Error: missing expected validation message")
            all_passed = False

    return all_passed


def main():
    print("=" * 60)
    print("Git Auto Updater Test Suite")
    print("=" * 60)
    
    tests = [
        ("Source files", test_source_files),
        ("Documentation", test_documentation),
        ("Help commands", test_help_commands),
        ("Configuration", test_config_file),
        ("Python imports", test_import),
        ("Interval argument validation", test_invalid_interval_arguments),
    ]
    
    results = []
    for name, test_func in tests:
        result = test_func()
        results.append((name, result))
    
    print("\n" + "=" * 60)
    print("Test Results Summary")
    print("=" * 60)
    
    all_passed = True
    for name, result in results:
        status = "PASS" if result else "FAIL"
        print(f"  {status} {name}")
        if not result:
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("\n[OK] All tests passed!")
        return 0
    else:
        print("\n[FAIL] Some tests failed. Please check the output above.")
        return 1


if __name__ == '__main__':
    sys.exit(main())

