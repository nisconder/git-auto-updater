# Security Policy

## Supported Versions

| Version | Supported          |
|---------|-------------------|
| 1.0.x   | :white_check_mark: Yes |

## Reporting a Vulnerability

如果你发现了安全漏洞，请不要公开提交 issue。请通过以下方式私下报告：

### 如何报告

1. **发送邮件**至：security@example.com
2. 在邮件中包含：
   - 漏洞描述
   - 影响范围
   - 重现步骤（如果有）
   - 建议的修复方案（如果有）

### 响应时间

我们通常在 48 小时内回复安全报告。

### 处理流程

1. 确认收到报告
2. 验证和评估漏洞
3. 开发修复补丁
4. 协调发布时间表
5. 发布安全更新
6. 公开披露漏洞细节

## Security Best Practices for Users

### 使用建议

1. **不要在配置文件中存储敏感信息**
   - 避免在 git_repos.txt 中包含敏感仓库路径
   - 使用 Git 凭证助手或 SSH 密钥，而不是硬编码密码

2. **定期更新**
   - 保持工具更新到最新版本
   - 关注安全公告

3. **权限管理**
   - 使用最小权限原则
   - 定期审查 Git 访问权限

4. **审查更新**
   - 定期检查更新的提交内容
   - 确保没有恶意更改

### 已知限制

1. **数据覆盖**
   - 更新策略会覆盖本地未提交的更改
   - 确保在更新前提交或备份重要更改

2. **网络传输**
   - 使用 HTTPS 或 SSH 协议
   - 避免使用不安全的认证方式

3. **日志安全**
   - 日志可能包含仓库路径和其他信息
   - 保护日志文件不被未授权访问

## 依赖安全

Git Auto Updater 是纯 Python 实现，不依赖外部库，减少了攻击面。

## 安全特性

1. **无外部依赖** - 减少供应链攻击风险
2. **简单设计** - 易于审计和维护
3. **明确的更新策略** - 用户了解更新行为
4. **透明度** - 开源代码，可自行审计

## 责任披露政策

我们负责任地披露安全漏洞：

- 给用户合理的时间应用补丁
- 协调发布时间，避免用户风险
- 提供清晰的修复说明
- 公开披露时包含足够的技术细节

## 联系方式

- 安全邮箱：security@example.com
- GitHub Issues：https://github.com/yourusername/git-auto-updater/issues
- 项目主页：https://github.com/yourusername/git-auto-updater

---

**感谢你帮助保护 Git Auto Updater 用户！** 🔒
