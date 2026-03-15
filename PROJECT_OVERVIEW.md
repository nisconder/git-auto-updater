# 项目概览

Git Auto Updater 用于自动检测并同步 Git 仓库更新，支持单仓库与多仓库模式。

## 项目结构

```text
git-auto-updater/
├── README.md
├── QUICK_START.md
├── HOW_TO_USE.md
├── INSTALL.md
├── VERIFICATION.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── AUTHORS.md
├── SECURITY.md
├── LICENSE
├── check_env.py
├── test_basic.py
├── git_repos.example.txt
├── src/
│   ├── git_auto_updater.py
│   └── git_multi_updater.py
└── examples/
    └── USAGE_EXAMPLES.md
```

## 核心能力

- 自动检测远程更新
- 单仓库自动同步
- 多仓库并发同步
- 可配置检查间隔
- 支持一次性检查

## 技术特点

- 纯 Python 实现
- 无外部运行时依赖
- 支持 Windows/Linux/Mac
- 命令行接口清晰易用

## 文档导航

- [README.md](README.md)：完整介绍
- [QUICK_START.md](QUICK_START.md)：快速上手
- [HOW_TO_USE.md](HOW_TO_USE.md)：日常使用说明
- [INSTALL.md](INSTALL.md)：安装与排障
- [VERIFICATION.md](VERIFICATION.md)：验证流程
- [USAGE_EXAMPLES.md](examples/USAGE_EXAMPLES.md)：场景示例

## 适用场景

- 个人项目持续同步
- 多仓库批量维护
- 本地镜像仓库定时更新

