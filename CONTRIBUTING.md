# Contributing to Git Auto Updater

感谢你考虑为 Git Auto Updater 做出贡献！

## 如何贡献

### 报告 Bug

如果你发现了 bug：

1. 检查 [Issues](https://github.com/yourusername/git-auto-updater/issues) 是否已有相关问题
2. 如果没有，创建一个新的 issue，包含：
   - 清晰的标题描述问题
   - 详细的重现步骤
   - 预期行为
   - 实际行为
   - 环境信息（操作系统、Python 版本、Git 版本）
   - 错误日志或截图

### 提出新功能

1. 先创建一个 issue 讨论你的想法
2. 说明功能的用例和预期行为
3. 等待维护者的反馈
4. 获得批准后再开始实现

### 提交代码

#### 准备工作

1. Fork 本仓库
2. 创建你的特性分支：`git checkout -b feature/your-feature-name`
3. 确保你的代码遵循现有的代码风格
4. 添加适当的文档和注释
5. 测试你的更改

#### 代码规范

- 使用 4 空格缩进
- 遵循 PEP 8 风格指南
- 函数和类添加 docstring
- 使用有意义的变量和函数名
- 保持函数简短和专注

#### 提交规范

提交信息应该清晰描述更改：

```
类型(范围): 简短描述

详细描述（可选）

类型可以是：
- feat: 新功能
- fix: 修复 bug
- docs: 文档更新
- style: 代码格式（不影响功能）
- refactor: 重构
- test: 测试相关
- chore: 构建/工具相关
```

示例：
```
fix(updater): handle authentication errors gracefully

Add proper error handling for Git authentication failures
and provide helpful error messages to users.
```

#### Pull Request 流程

1. 推送到你的 fork：`git push origin feature/your-feature-name`
2. 创建 Pull Request
3. 在 PR 描述中：
   - 引用相关的 issue
   - 描述你的更改
   - 添加截图（如适用）
   - 说明测试情况
4. 等待代码审查
5. 根据反馈进行修改
6. 审查通过后，你的代码将被合并

## 开发环境设置

### 1. 克隆仓库

```bash
git clone https://github.com/yourusername/git-auto-updater.git
cd git-auto-updater
```

### 2. 创建虚拟环境（推荐）

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. 安装开发依赖

```bash
pip install -e .
```

### 4. 运行测试

```bash
python check_env.py
python src/git_auto_updater.py --help
python src/git_multi_updater.py --help
```

### 5. 运行示例

编辑 `git_repos.example.txt` 添加测试仓库，然后：

```bash
python src/git_multi_updater --once
```

## 项目结构

```
git-auto-updater/
├── .gitignore              # Git 忽略文件
├── LICENSE                 # MIT 许可证
├── README.md              # 主文档
├── QUICKSTART.md          # 快速开始指南
├── INSTALL.md             # 安装指南
├── CHANGELOG.md           # 变更日志
├── CONTRIBUTING.md        # 贡献指南（本文件）
├── check_env.py           # 环境检查脚本
├── requirements.txt       # Python 依赖
├── setup.py              # 安装配置
├── git_repos.example.txt  # 配置文件示例
├── src/
│   ├── git_auto_updater.py     # 单仓库工具
│   └── git_multi_updater.py    # 多仓库工具
└── examples/
    └── usage_examples.md       # 使用示例
```

## 测试指南

在提交 PR 前，请确保：

1. 代码能够成功运行环境检查
2. 单仓库工具能够正常工作
3. 多仓库工具能够正常工作
4. 在不同操作系统上测试（如果可能）
5. 错误处理正常工作

## 文档更新

如果你的更改影响了用户使用：

1. 更新 README.md 中的相关部分
2. 如果是新功能，在 CHANGELOG.md 中添加条目
3. 考虑在 examples/usage_examples.md 中添加示例

## 社区准则

### 行为准则

- 尊重所有贡献者
- 建设性的反馈
- 欢迎新手
- 保持讨论专注和友好

### 沟通

- 使用英语提交 issue 和 PR
- 清晰和简洁的沟通
- 耐心等待回应

## 获取帮助

如果你在贡献过程中需要帮助：

1. 查看 [README.md](README.md) 和 [examples/usage_examples.md](examples/usage_examples.md)
2. 搜索现有的 Issues
3. 创建新的 issue 标记为 `question`

## 许可

贡献的代码将使用与项目相同的 [MIT License](LICENSE)。

## 致谢

感谢所有为 Git Auto Updater 做出贡献的人！

---

**准备好贡献了吗？开始吧！** 🚀
