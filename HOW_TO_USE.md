# Git Auto Updater 使用说明

## 快速开始（3 步）

### 1. 克隆并验证环境
```bash
git clone https://github.com/nisconder/git-auto-updater.git
cd git-auto-updater
python check_env.py
```

### 2. 选择使用方式

**方式 A：单仓库模式**
```bash
python src/git_auto_updater.py /path/to/your/repo --remote https://github.com/user/repo.git
```

**方式 B：多仓库模式**
```bash
cp git_repos.example.txt git_repos.txt
# 编辑 git_repos.txt，填入你的仓库配置
python src/git_multi_updater.py
```

### 3. 启动监控

持续运行模式：
```bash
# 单仓库
python src/git_auto_updater.py /path/to/your/repo

# 多仓库
python src/git_multi_updater.py
```

## 你将获得

✅ 自动检测并更新仓库
✅ 可配置检查间隔（默认 5 分钟）
✅ 带时间戳的详细日志
✅ 多仓库多线程支持
✅ 跨平台支持（Windows/Linux/Mac）

## 需要帮助？

- 阅读 [README.md](README.md) 获取完整文档
- 查看 [QUICK_START.md](QUICK_START.md) 获取更详细示例
- 运行 `python check_env.py` 检查本机环境

## 安装为命令（可选）

安装后可直接使用命令：
```bash
pip install -e .
git-auto-updater /path/to/repo
git-multi-updater
```

---

**现在就可以开始自动监控你的仓库了。**


