# 快速开始指南

## 5 分钟快速上手

### 1. 克隆或下载项目

```bash
git clone https://github.com/nisconder/git-auto-updater.git
cd git-auto-updater
```

### 2. 确认环境

确保你已安装：
- Python 3.8+
- Git

检查方式：
```bash
python --version
git --version
```

### 3. 选择使用方式

#### 方式 A：直接运行（最简单）

```bash
# 单仓库
python src/git_auto_updater.py C:\path\to\your\repo --remote https://github.com/user/repo.git

# 多仓库（先配置）
cp git_repos.example.txt git_repos.txt
# 编辑 git_repos.txt 添加你的仓库
python src/git_multi_updater.py
```

#### 方式 B：安装为系统命令

```bash
pip install -e .

# 现在可以直接使用
git-auto-updater C:\path\to\your\repo --remote https://github.com/user/repo.git
git-multi-updater
```

### 4. 验证是否工作

```bash
# 单仓库测试
git-auto-updater /path/to/repo --remote https://github.com/username/repo.git --once

# 多仓库测试
git-multi-updater --status
```

### 5. 开始自动监控

```bash
# 单仓库（持续运行）
git-auto-updater /path/to/repo

# 多仓库（持续运行）
git-multi-updater
```

## 常见问题快速解答

### Q: 如何停止监控？
A: 按 `Ctrl+C`

### Q: 如何修改检查频率？
A: 使用 `--interval` 参数，单位是秒（必须是正整数）
```bash
git-auto-updater /path/to/repo --interval 600  # 每10分钟检查一次
```

### Q: 配置文件在哪里？
A: `git_repos.txt`（需要从 `git_repos.example.txt` 复制）

### Q: 支持哪些操作系统？
A: Windows、Linux、Mac 都支持

## 下一步

- 查看 [README.md](README.md) 了解完整功能
- 查看 [examples/usage_examples.md](examples/usage_examples.md) 了解更多使用示例
- 根据你的需求修改配置

## 需要帮助？

如有问题，请提交 Issue 或查看文档。
