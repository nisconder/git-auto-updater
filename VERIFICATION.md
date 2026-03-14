# Repository Verification Guide

本指南帮助你验证 Git Auto Updater 仓库的完整性和可用性。

## Quick Verification

### 1. 检查仓库完整性

```bash
# 列出所有文件
ls -la

# 验证 Git 状态
git status
```

预期输出：
- 应该看到所有项目文件
- Git 状态应该显示 "nothing to commit, working tree clean"

### 2. 运行环境检查

```bash
python check_env.py
```

预期输出：
```
============================================================
Git Auto Updater Environment Check
============================================================
...
[OK] All checks passed! You can start using Git Auto Updater
```

### 3. 运行基础测试

```bash
python test_basic.py
```

预期输出：
```
============================================================
Git Auto Updater Test Suite
============================================================
...
[OK] All tests passed!
```

## 完整验证步骤

### 步骤 1: 验证文件结构

```bash
# 检查根目录文件
ls -la | grep -E "^\-"

# 检查源代码目录
ls -la src/

# 检查示例目录
ls -la examples/
```

验证点：
- ✓ README.md 存在
- ✓ QUICKSTART.md 存在
- ✓ INSTALL.md 存在
- ✓ check_env.py 存在
- ✓ test_basic.py 存在
- ✓ src/git_auto_updater.py 存在
- ✓ src/git_multi_updater.py 存在
- ✓ examples/usage_examples.md 存在
- ✓ git_repos.example.txt 存在

### 步骤 2: 验证文档完整性

```bash
# 统计文档文件数量
ls -la *.md | wc -l
```

预期：至少 8 个文档文件

```bash
# 验证关键文档内容
grep -q "Git Auto Updater" README.md && echo "README.md OK"
grep -q "Quick Start" QUICKSTART.md && echo "QUICKSTART.md OK"
grep -q "Installation" INSTALL.md && echo "INSTALL.md OK"
```

### 步骤 3: 验证源代码

```bash
# 检查 Python 脚本的可执行性
python -m py_compile src/git_auto_updater.py
python -m py_compile src/git_multi_updater.py

# 测试导入
python -c "import sys; sys.path.insert(0, 'src'); import git_auto_updater; print('git_auto_updater OK')"
python -c "import sys; sys.path.insert(0, 'src'); import git_multi_updater; print('git_multi_updater OK')"
```

### 步骤 4: 验证工具功能

```bash
# 测试单仓库工具帮助
python src/git_auto_updater.py --help

# 测试多仓库工具帮助
python src/git_multi_updater.py --help

# 测试状态显示
python src/git_multi_updater.py --status
```

### 步骤 5: 验证配置文件

```bash
# 检查配置文件是否存在
test -f git_repos.example.txt && echo "Config file OK"

# 验证配置文件格式
grep -q "|" git_repos.example.txt && echo "Config format OK"
```

## 高级验证

### 验证 Git 历史

```bash
# 查看提交历史
git log --oneline

# 验证提交数量
git log --oneline | wc -l
```

预期：至少有 10 个提交

### 验证安装功能

```bash
# 测试 setup.py 语法
python -m py_compile setup.py

# 尝试安装（不实际安装，只检查）
python setup.py check
```

### 验证跨平台兼容性

```bash
# 检查路径处理
grep -r "Path\|path" src/ | wc -l

# 验证无平台特定的硬编码路径
grep -r "C:\\" src/ | wc -l  # 应该为 0
grep -r "/home" src/ | wc -l  # 应该为 0
```

## 常见问题

### Q: 文件数量不对

**症状**：文件数量少于预期

**解决方案**：
1. 检查是否完整克隆了仓库
2. 运行 `git status` 查看是否有未跟踪的文件
3. 尝试重新克隆

### Q: 环境检查失败

**症状**：`python check_env.py` 报错

**解决方案**：
1. 确认 Python 版本 >= 3.8
2. 确认 Git 已安装
3. 检查错误消息并参考 INSTALL.md

### Q: 测试失败

**症状**：`python test_basic.py` 报错

**解决方案**：
1. 确保在项目根目录运行
2. 检查 Python 路径设置
3. 查看具体错误消息

### Q: 无法导入模块

**症状**：`ModuleNotFoundError`

**解决方案**：
1. 确保在正确的目录
2. 手动添加 src 到 Python 路径
3. 或使用 `pip install -e .` 安装

## 验证清单

使用此清单确保仓库完全可用：

- [ ] 所有必需文件存在
- [ ] Git 状态正常（无未提交更改）
- [ ] 环境检查通过
- [ ] 基础测试通过
- [ ] 所有文档可读
- [ ] 源代码可编译
- [ ] 工具帮助命令正常
- [ ] 配置文件格式正确
- [ ] 可以导入所有模块

## 完整验证命令序列

将以下命令复制到终端，一次性运行所有验证：

```bash
echo "=== Repository Verification ===" && \
echo "1. Checking files..." && \
ls -la | grep -E "^\-" && \
echo "" && \
echo "2. Git status..." && \
git status && \
echo "" && \
echo "3. Environment check..." && \
python check_env.py && \
echo "" && \
echo "4. Basic tests..." && \
python test_basic.py && \
echo "" && \
echo "=== Verification Complete ==="
```

## 下一步

如果所有验证都通过，你可以：

1. 查看 **QUICKSTART.md** 开始使用
2. 查看 **README.md** 了解完整功能
3. 查看 **PROJECT_OVERVIEW.md** 了解项目结构
4. 查看 **INSTALL.md** 进行安装

## 需要帮助？

如果验证过程中遇到问题：

1. 查看错误消息的详细信息
2. 参考 **INSTALL.md** 中的故障排除部分
3. 运行 `python check_env.py` 获取诊断信息
4. 提交 Issue 到 GitHub

---

**验证完成后，你就可以开始使用 Git Auto Updater 了！**
