# Git Auto Updater

自动监控和更新 Git 仓库的工具，支持单仓库和多仓库管理。

## 功能特点

- ✅ 自动检测远程仓库更新
- ✅ 支持单仓库和多仓库管理
- ✅ 可配置的检查间隔
- ✅ 多线程并发监控（多仓库版本）
- ✅ 详细的日志输出
- ✅ 纯 Python 实现，无需额外依赖
- ✅ 跨平台支持（Windows/Linux/Mac）

## 环境要求

- Python 3.8 或更高版本
- Git 已安装并配置好

## 安装方式

### 方式一：直接使用（推荐）

```bash
# 克隆仓库
git clone https://github.com/nisconder/git-auto-updater.git
cd git-auto-updater

# 验证环境
python check_env.py

# 直接运行脚本
python src/git_auto_updater.py --help
python src/git_multi_updater.py --help
```

### 方式二：安装为系统命令

```bash
# 克隆仓库
git clone https://github.com/nisconder/git-auto-updater.git
cd git-auto-updater

# 安装
pip install -e .

# 现在可以直接使用命令
git-auto-updater --help
git-multi-updater --help
```

## 使用说明

### 单仓库版本

监控单个 Git 仓库，当远程仓库有更新时自动拉取。

#### 基本用法

```bash
# 使用安装后的命令
git-auto-updater /path/to/repo --remote https://github.com/user/repo.git

# 或直接运行脚本
python src/git_auto_updater.py /path/to/repo --remote https://github.com/user/repo.git
```

#### 参数说明

- `repo_path`: 本地仓库路径（必填）
- `--remote, -r`: 远程仓库 URL（首次克隆时使用）
- `--interval, -i`: 检查间隔（秒，正整数），默认 300 秒（5 分钟）
- `--once`: 只检查一次，不持续运行

#### 使用示例

```bash
# 首次克隆并监控（每5分钟检查一次）
git-auto-updater C:\Users\yourname\repos\myproject --remote https://github.com/user/myproject.git

# 只检查一次
git-auto-updater C:\Users\yourname\repos\myproject --remote https://github.com/user/myproject.git --once

# 自定义检查间隔（例如每10分钟检查一次）
git-auto-updater C:\Users\yourname\repos\myproject --remote https://github.com/user/myproject.git --interval 600

# 检查已存在的仓库
git-auto-updater C:\Users\yourname\repos\myproject
```

### 多仓库版本

监控多个 Git 仓库，从配置文件读取仓库列表。

#### 基本用法

```bash
# 使用安装后的命令
git-multi-updater

# 或直接运行脚本
python src/git_multi_updater.py
```

#### 配置文件

1. 复制示例配置文件：

```bash
cp git_repos.example.txt git_repos.txt
```

2. 编辑 `git_repos.txt`，添加你的仓库配置：

```
本地路径|远程仓库URL
```

示例配置：

```
# Windows 路径示例
C:\Users\yourname\repos\project1|https://github.com/username/project1.git
C:\Users\yourname\repos\project2|https://github.com/username/project2.git

# Linux/Mac 路径示例
/home/username/repos/project1|https://github.com/username/project1.git
/home/username/repos/project2|https://github.com/username/project2.git
```

#### 参数说明

- `--config, -c`: 配置文件路径，默认为 `git_repos.txt`
- `--interval, -i`: 检查间隔（秒，正整数），默认 300 秒（5 分钟）
- `--once`: 只检查一次，不持续运行
- `--status, -s`: 显示所有仓库状态

#### 使用示例

```bash
# 持续监控所有配置的仓库
git-multi-updater

# 只检查一次
git-multi-updater --once

# 查看仓库状态
git-multi-updater --status

# 使用自定义配置文件
git-multi-updater --config my_repos.txt

# 自定义检查间隔
git-multi-updater --interval 600
```

## 更新策略

工具使用以下策略更新仓库：

1. `git fetch origin` - 获取远程更新
2. `git reset --hard origin/<当前分支>` - 优先重置到当前分支对应的远程版本
3. `git reset --hard origin/HEAD` - 当无法识别当前分支时回退到默认分支
4. `git clean -fd` - 清理未跟踪的文件和目录

这个策略确保本地仓库与远程完全同步，即使有冲突也会自动解决。

## 使用场景

- 上游仓库更新后需要自动同步
- CI/CD 流程中需要保持代码最新
- 开发环境需要定期更新依赖
- 监控多个开源项目的更新
- 团队协作中保持代码同步

## 停止监控

使用 `Ctrl+C` 可以停止持续监控模式。

## 注意事项

1. **数据安全**：本地未提交的更改会在更新时丢失，建议在使用前提交或备份重要更改
2. **权限要求**：确保有访问远程仓库的权限
3. **路径格式**：Windows 路径可以使用反斜杠或正斜杠
4. **网络稳定**：确保网络连接稳定，否则可能导致更新失败
5. **署名安全**：工具不会修改 Git 的 `user.name` 或 `user.email`（包含本地与全局配置）

## 常见问题

### Q: 更新失败怎么办？

A: 检查以下几点：
- 网络连接是否正常
- 是否有访问远程仓库的权限
- 本地仓库是否被其他程序占用
- 查看错误日志，根据提示解决问题

### Q: 可以保留本地更改吗？

A: 当前版本的更新策略是强制同步，会覆盖本地更改。如需保留更改，请在更新前手动提交。

### Q: 支持私有仓库吗？

A: 支持。确保 Git 已配置好相应的认证方式（SSH、HTTPS with token 等）。

### Q: 如何自定义日志输出？

A: 可以修改源代码中的 `log` 方法，将输出重定向到文件或其他地方。

## 更多文档

- **[HOW_TO_USE.md](HOW_TO_USE.md)** - 精简使用说明（3步上手）
- **[QUICK_START.md](QUICK_START.md)** - 5分钟快速上手指南
- **[INSTALL.md](INSTALL.md)** - 详细安装指南
- **[VERIFICATION.md](VERIFICATION.md)** - 仓库验证指南
- **[PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)** - 项目结构概览
- **[PROJECT_COMPLETION_REPORT.md](PROJECT_COMPLETION_REPORT.md)** - 项目完成报告
- **[USAGE_EXAMPLES.md](examples/USAGE_EXAMPLES.md)** - 详细使用示例
- **[CHANGELOG.md](CHANGELOG.md)** - 版本变更日志
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - 贡献指南
- **[AUTHORS.md](AUTHORS.md)** - 作者与贡献者信息
- **[SECURITY.md](SECURITY.md)** - 安全策略

## 开发

```bash
# 克隆仓库
git clone https://github.com/nisconder/git-auto-updater.git
cd git-auto-updater

# 验证环境
python check_env.py

# 运行测试
python test_basic.py

# 创建虚拟环境（可选）
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

# 安装开发版本
pip install -e .
```

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 联系方式

如有问题或建议，请提交 Issue。

---

**⭐ 如果这个工具对你有帮助，请给个 Star！**


