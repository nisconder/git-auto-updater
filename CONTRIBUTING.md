# 参与贡献指南

感谢你考虑为 Git Auto Updater 贡献代码或文档。

## 如何贡献

### 报告 Bug

1. 先检查 Issues 是否已有同类问题。
2. 如果没有，请提交新 issue，并包含：
   - 问题描述
   - 复现步骤
   - 预期行为与实际行为
   - 环境信息（操作系统、Python 版本、Git 版本）
   - 相关日志或截图

### 提出新功能

1. 先创建 issue 说明你的想法。
2. 描述使用场景和预期效果。
3. 等待维护者反馈后再开始实现。

### 提交代码

1. Fork 本仓库。
2. 新建分支：`git checkout -b feature/your-feature-name`
3. 保持代码风格一致并补充必要文档。
4. 提交 Pull Request。

## 代码规范

- 使用 4 空格缩进
- 遵循 PEP 8
- 函数和类应包含清晰 docstring
- 命名语义化、可读性强
- 保持函数职责单一

## 提交信息建议

```text
类型(范围): 简短描述
```

常见类型：
- feat：新功能
- fix：修复问题
- docs：文档更新
- refactor：重构
- test：测试相关
- chore：杂项维护

## 文档贡献

涉及使用方式或行为变化时，请同步更新：
- README.md
- QUICK_START.md
- INSTALL.md
- VERIFICATION.md
- examples/USAGE_EXAMPLES.md

