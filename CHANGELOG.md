# 更新日志

本文档记录 Git Auto Updater 的重要变更。

格式参考 Keep a Changelog，版本号遵循 Semantic Versioning。

## [未发布]

## [1.0.0] - 2024-01-15

### 新增
- 单仓库自动更新工具（git_auto_updater.py）
- 多仓库管理工具（git_multi_updater.py）
- 自动检测远程仓库更新
- 可配置检查间隔
- 多仓库并发监控
- 带时间戳的详细日志
- 纯 Python 实现，无外部依赖
- 跨平台支持（Windows/Linux/Mac）
- 完整文档与示例
- 环境检查脚本
- 多仓库配置示例文件
- setup.py 安装配置
- MIT 许可证

### 特性
- 仓库不存在时自动克隆
- 采用 fetch + reset + clean 的强制同步策略
- 支持一次性检查模式
- 支持自定义配置文件
- 支持 SSH 与 HTTPS 仓库地址

### 文档
- 主文档（README）
- 快速开始（QUICK_START）
- 安装指南（INSTALL）
- 使用示例（examples/USAGE_EXAMPLES.md）
- 常见问题与排障说明

### 首次发布
- Git Auto Updater 首个稳定版本
- 单仓库与多仓库功能可用
