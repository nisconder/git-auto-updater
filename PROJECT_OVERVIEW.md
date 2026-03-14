# Git Auto Updater - Project Overview

## Quick Summary

Git Auto Updater 是一个自动监控和更新 Git 仓库的工具，支持单仓库和多仓库管理。

## Project Structure

```
git-auto-updater/
├── .gitignore                    # Git 忽略规则
├── LICENSE                       # MIT 许可证
├── README.md                     # 主文档（完整功能说明）
├── QUICKSTART.md                 # 快速开始指南（5分钟上手）
├── INSTALL.md                    # 详细安装指南
├── CHANGELOG.md                  # 版本变更日志
├── CONTRIBUTING.md               # 贡献指南
├── AUTHORS.md                    # 贡献者列表
├── SECURITY.md                   # 安全政策
├── check_env.py                  # 环境检查脚本
├── test_basic.py                 # 基础测试脚本
├── requirements.txt              # Python 依赖（无外部依赖）
├── setup.py                      # 安装配置
├── git_repos.example.txt         # 多仓库配置文件示例
├── src/                          # 源代码目录
│   ├── git_auto_updater.py       # 单仓库自动更新工具
│   └── git_multi_updater.py      # 多仓库自动更新工具
└── examples/                     # 示例和文档
    └── usage_examples.md         # 详细使用示例
```

## Key Features

### Core Functionality
- ✅ 自动检测远程仓库更新
- ✅ 支持单仓库和多仓库管理
- ✅ 可配置的检查间隔
- ✅ 多线程并发监控
- ✅ 详细的日志输出

### Technical Features
- ✅ 纯 Python 实现
- ✅ 无外部依赖
- ✅ 跨平台支持（Windows/Linux/Mac）
- ✅ Python 3.8+ 支持

### User Experience
- ✅ 简单的命令行界面
- ✅ 完善的文档
- ✅ 环境检查工具
- ✅ 示例配置文件

## Quick Start

### 1. Check Environment
```bash
python check_env.py
```

### 2. Run Tests
```bash
python test_basic.py
```

### 3. Use Single Repo Tool
```bash
python src/git_auto_updater.py /path/to/repo --remote https://github.com/user/repo.git
```

### 4. Use Multi Repo Tool
```bash
cp git_repos.example.txt git_repos.txt
# Edit git_repos.txt with your repositories
python src/git_multi_updater.py
```

### 5. Install as System Commands (Optional)
```bash
pip install -e .
git-auto-updater /path/to/repo
git-multi-updater
```

## Documentation

### For New Users
1. Start with **QUICKSTART.md** - Get up and running in 5 minutes
2. Read **README.md** - Understand all features
3. Check **examples/usage_examples.md** - See detailed examples

### For Installation
1. Review **INSTALL.md** - Detailed installation guide
2. Run **check_env.py** - Verify your environment
3. Run **test_basic.py** - Test basic functionality

### For Contributors
1. Read **CONTRIBUTING.md** - How to contribute
2. Check **CHANGELOG.md** - Version history
3. See **AUTHORS.md** - Current contributors

### For Security
1. Review **SECURITY.md** - Security policy and best practices
2. Report vulnerabilities privately

## Version Information

- **Current Version**: 1.0.0
- **Python Requirement**: 3.8+
- **Git Requirement**: Any recent version
- **License**: MIT

## Testing

Run all tests:
```bash
python test_basic.py
```

Expected output:
```
============================================================
Git Auto Updater Test Suite
============================================================
Testing source files...
  [PASS] src/git_auto_updater.py
  [PASS] src/git_multi_updater.py
...
[OK] All tests passed!
```

## Common Use Cases

1. **Development Environment** - Automatically update dependencies
2. **CI/CD Pipeline** - Keep code synchronized
3. **Open Source Monitoring** - Track updates to projects you follow
4. **Team Collaboration** - Keep team code in sync

## Getting Help

1. Check documentation files in the root directory
2. Run `python check_env.py` to diagnose issues
3. Submit an issue on GitHub with:
   - Your operating system
   - Python version
   - Git version
   - Error message
   - Steps to reproduce

## Project Statistics

- **Total Files**: 16
- **Documentation Files**: 8
- **Python Scripts**: 4
- **Configuration Files**: 3
- **License**: MIT

## Repository Status

- ✅ All documentation complete
- ✅ Environment check script working
- ✅ Basic tests passing
- ✅ Installation guide provided
- ✅ Contribution guidelines available
- ✅ Security policy in place

## Next Steps

For new users:
1. Read QUICKSTART.md
2. Run check_env.py
3. Try the examples

For contributors:
1. Read CONTRIBUTING.md
2. Review the code
3. Submit pull requests

---

**Ready to use? Check out QUICKSTART.md to get started!**
