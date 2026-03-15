# 仓库验证指南

本指南用于验证 Git Auto Updater 的完整性、可用性与基础功能。

## 快速验证

### 1. 检查文件

```bash
# Windows
Get-ChildItem

# Linux/Mac
ls -la
```

### 2. 检查环境

```bash
python check_env.py
```

预期结果：显示全部检查通过。

### 3. 运行基础测试

```bash
python test_basic.py
```

预期结果：测试通过且无异常退出。

## 完整验证步骤

### 步骤 1：验证脚本可执行

```bash
python src/git_auto_updater.py --help
python src/git_multi_updater.py --help
```

### 步骤 2：验证安装入口

```bash
pip install -e .
git-auto-updater --help
git-multi-updater --help
```

### 步骤 3：验证文档与示例

确认以下文件存在：
- README.md
- QUICK_START.md
- INSTALL.md
- VERIFICATION.md
- examples/USAGE_EXAMPLES.md

## 常见问题

### 环境检查失败

- 检查 Python 与 Git 是否已安装。
- 确认当前终端可直接调用 `python` 与 `git`。

### 测试失败

- 先执行 `pip install -e .`。
- 重新运行 `python test_basic.py`。

### 命令不可用

- 确认当前激活的是正确虚拟环境。
- 重新安装后再验证命令帮助输出。

