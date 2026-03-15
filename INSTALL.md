# 安装指南

本文档介绍 Git Auto Updater 的安装方式与验证步骤。

## 前置要求

- Python 3.8 或更高版本
- Git 已正确安装

检查命令：

```bash
python --version
git --version
```

建议先执行环境检查：

```bash
python check_env.py
```

## 安装方式

### 方式一：直接使用（推荐）

```bash
git clone https://github.com/nisconder/git-auto-updater.git
cd git-auto-updater
python src/git_auto_updater.py --help
python src/git_multi_updater.py --help
```

### 方式二：安装为命令

```bash
git clone https://github.com/nisconder/git-auto-updater.git
cd git-auto-updater
pip install -e .
git-auto-updater --help
git-multi-updater --help
```

### 方式三：虚拟环境安装（推荐生产使用）

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
pip install -e .
```

## 安装验证

### 快速验证

```bash
python check_env.py
python test_basic.py
```

### 真实仓库验证

```bash
# 单仓库一次性检查
git-auto-updater /path/to/repo --remote https://github.com/user/repo.git --once

# 多仓库模式
cp git_repos.example.txt git_repos.txt
# 编辑 git_repos.txt 后运行
python src/git_multi_updater.py --status
```

## 常见问题

### 找不到命令

- 确认当前 Python 环境与安装环境一致。
- 如果使用 `pip install -e .`，请检查 Scripts/bin 目录是否在 PATH 中。

### 模块导入失败

- 在项目根目录执行命令。
- 重新执行 `pip install -e .`。

### Git 认证失败

- 优先使用 SSH Key 或 Git 凭证助手。
- 避免在脚本中硬编码账号密码。

## 下一步

- 阅读 [HOW_TO_USE.md](HOW_TO_USE.md) 了解基础流程
- 阅读 [examples/USAGE_EXAMPLES.md](examples/USAGE_EXAMPLES.md) 查看常见场景
- 阅读 [VERIFICATION.md](VERIFICATION.md) 做完整验证
