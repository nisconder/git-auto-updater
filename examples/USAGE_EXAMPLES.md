# 使用示例

本文档提供详细的使用示例，帮助你快速上手 Git Auto Updater。

## 目录

- [单仓库示例](#单仓库示例)
- [多仓库示例](#多仓库示例)
- [常见使用场景](#常见使用场景)
- [故障排除](#故障排除)

## 单仓库示例

### 示例 1：首次克隆并监控

```bash
# 场景：你想监控一个新项目
git-auto-updater C:\Users\yourname\repos\myproject --remote https://github.com/username/myproject.git
```

输出示例：
```
[2024-01-15 10:30:00] [myproject] 仓库不存在，开始克隆: https://github.com/username/myproject.git
[2024-01-15 10:30:15] [myproject] 克隆成功
[2024-01-15 10:30:15] [myproject] 没有更新
[2024-01-15 10:30:15] [myproject] 等待 300 秒后再次检查...
```

### 示例 2：监控已存在的仓库

```bash
# 场景：你已经克隆了一个项目，现在想自动监控更新
git-auto-updater C:\Users\yourname\repos\myproject
```

### 示例 3：只检查一次

```bash
# 场景：只想检查是否有更新，不想持续运行
git-auto-updater C:\Users\yourname\repos\myproject --once
```

输出示例：
```
[2024-01-15 10:35:00] [myproject] 没有更新
```

或（如果有更新）：
```
[2024-01-15 10:35:00] [myproject] 检测到更新: a1b2c3d -> e5f6g7h
[2024-01-15 10:35:00] [myproject] 开始更新仓库...
[2024-01-15 10:35:02] [myproject] 仓库更新成功
```

### 示例 4：自定义检查间隔

```bash
# 场景：项目更新频繁，想每2分钟检查一次
git-auto-updater C:\Users\yourname\repos\myproject --interval 120

# 场景：项目更新较少，想每30分钟检查一次
git-auto-updater C:\Users\yourname\repos\myproject --interval 1800
```

## 多仓库示例

### 示例 1：基本配置和监控

1. **创建配置文件**

```bash
cp git_repos.example.txt git_repos.txt
```

2. **编辑配置文件**

```
C:\Users\yourname\repos\project1|https://github.com/username/project1.git
C:\Users\yourname\repos\project2|https://github.com/username/project2.git
C:\Users\yourname\repos\project3|https://github.com/username/project3.git
```

3. **开始监控**

```bash
git-multi-updater
```

输出示例：
```
开始监控 3 个仓库...
[2024-01-15 10:30:00] [project1] 仓库不存在，开始克隆: https://github.com/username/project1.git
[2024-01-15 10:30:00] [project2] 仓库不存在，开始克隆: https://github.com/username/project2.git
[2024-01-15 10:30:00] [project3] 仓库不存在，开始克隆: https://github.com/username/project3.git
[2024-01-15 10:30:15] [project1] 克隆成功
[2024-01-15 10:30:20] [project2] 克隆成功
[2024-01-15 10:30:25] [project3] 克隆成功
[2024-01-15 10:30:25] [project1] 没有更新
[2024-01-15 10:30:25] [project1] 等待 300 秒后再次检查...
[2024-01-15 10:30:25] [project2] 没有更新
[2024-01-15 10:30:25] [project2] 等待 300 秒后再次检查...
[2024-01-15 10:30:25] [project3] 没有更新
[2024-01-15 10:30:25] [project3] 等待 300 秒后再次检查...
```

### 示例 2：查看仓库状态

```bash
git-multi-updater --status
```

输出示例：
```
仓库状态:
--------------------------------------------------
✓ C:\Users\yourname\repos\project1
   Remote: https://github.com/username/project1.git
   本地: a1b2c3d
✓ C:\Users\yourname\repos\project2
   Remote: https://github.com/username/project2.git
   本地: e5f6g7h
✗ C:\Users\yourname\repos\project3
   Remote: https://github.com/username/project3.git
--------------------------------------------------
```

### 示例 3：使用自定义配置文件

```bash
# 场景：你有多个不同的仓库列表
git-multi-updater --config work_repos.txt
git-multi-updater --config personal_repos.txt
```

### 示例 4：混合 Windows 和 Linux 路径

```
# work_repos.txt
C:\Users\yourname\work\project1|https://github.com/company/project1.git
C:\Users\yourname\work\project2|https://github.com/company/project2.git

# personal_repos.txt (在 Linux 上)
/home/yourname/personal/project1|https://github.com/username/project1.git
/home/yourname/personal/project2|https://github.com/username/project2.git
```

## 常见使用场景

### 场景 1：开发环境自动更新

```bash
# 在开发服务器上自动更新依赖库
git-multi-updater --config dev_repos.txt --interval 600
```

配置示例：
```
/opt/code/library1|https://github.com/company/library1.git
/opt/code/library2|https://github.com/company/library2.git
```

### 场景 2：监控开源项目更新

```bash
# 监控你关注的开源项目
git-multi-updater --config opensource_repos.txt
```

配置示例：
```
C:\Users\yourname\opensource\react|https://github.com/facebook/react.git
C:\Users\yourname\opensource\vue|https://github.com/vuejs/vue.git
C:\Users\yourname\opensource\angular|https://github.com/angular/angular.git
```

### 场景 3：团队协作同步

```bash
# 团队成员保持代码同步
git-auto-updater C:\Users\yourname\team\shared-project --interval 120
```

### 场景 4：定时检查更新

在 Linux/Mac 上使用 crontab：

```bash
# 每小时检查一次更新
0 * * * * cd /path/to/git-auto-updater && python src/git_multi_updater.py --once >> /var/log/git-updater.log 2>&1
```

在 Windows 上使用任务计划程序：

1. 打开"任务计划程序"
2. 创建基本任务
3. 设置触发器（例如每天）
4. 设置操作：运行程序
   - 程序：`python`
   - 参数：`C:\Users\yourname\git-auto-updater\src\git_multi_updater.py --once`

## 故障排除

### 问题 1：Git 命令未找到

**错误信息**：
```
系统找不到指定的文件
```

**解决方案**：
1. 确保 Git 已安装
2. 将 Git 添加到系统 PATH 环境变量
3. 重启命令行窗口

### 问题 2：权限不足

**错误信息**：
```
fatal: could not read Username for 'https://github.com'
```

**解决方案**：
1. 配置 Git 凭证存储：
   ```bash
   git config --global credential.helper store
   git config --global user.name "yourname"
   git config --global user.email "youremail@example.com"
   ```
2. 或使用 SSH URL 替代 HTTPS URL

### 问题 3：网络连接失败

**错误信息**：
```
failed to connect to github.com
```

**解决方案**：
1. 检查网络连接
2. 检查代理设置
3. 配置 Git 代理：
   ```bash
   git config --global http.proxy http://proxy.example.com:8080
   git config --global https.proxy https://proxy.example.com:8080
   ```

### 问题 4：路径格式错误

**错误信息**：
```
No such file or directory
```

**解决方案**：
1. 使用绝对路径
2. Windows 路径示例：
   - 正确：`C:\Users\yourname\repos\project`
   - 错误：`~\repos\project` 或 `./repos/project`

### 问题 5：配置文件编码问题

**错误信息**：
```
UnicodeDecodeError
```

**解决方案**：
1. 确保配置文件使用 UTF-8 编码
2. 使用文本编辑器检查文件编码

## 高级技巧

### 技巧 1：日志记录

将输出重定向到日志文件：

```bash
git-multi-updater >> git-updater.log 2>&1
```

### 技巧 2：后台运行

Linux/Mac：
```bash
nohup git-multi-updater > git-updater.log 2>&1 &
```

Windows PowerShell：
```powershell
Start-Process python -ArgumentList "src\git_multi_updater.py" -RedirectStandardOutput "git-updater.log" -RedirectStandardError "git-updater-error.log" -NoNewWindow
```

### 技巧 3：通知更新

结合其他工具（如 notify-send、slack 等）在更新时发送通知。

---

如有其他问题，请查看 [README.md](../README.md) 或提交 Issue。
