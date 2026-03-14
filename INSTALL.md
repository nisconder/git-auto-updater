# Installation Guide

详细安装指南 - Git Auto Updater

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation Methods](#installation-methods)
- [Verifying Installation](#verifying-installation)
- [Troubleshooting](#troubleshooting)

## Prerequisites

### Required Software

1. **Python 3.8 or higher**
   
   **Check installation:**
   ```bash
   python --version
   # or
   python3 --version
   ```
   
   **If not installed:**
   - Windows: Download from [python.org](https://www.python.org/downloads/)
   - Linux: `sudo apt install python3`
   - Mac: `brew install python`

2. **Git**
   
   **Check installation:**
   ```bash
   git --version
   ```
   
   **If not installed:**
   - Windows: Download from [git-scm.com](https://git-scm.com/download/win)
   - Linux: `sudo apt install git`
   - Mac: `brew install git`

### Verifying Prerequisites

Run the environment check script:
```bash
python check_env.py
```

All checks should pass before proceeding.

## Installation Methods

### Method 1: Direct Download (Simplest)

1. **Download the project**
   
   Using Git:
   ```bash
   git clone https://github.com/nisconder/git-auto-updater.git
   cd git-auto-updater
   ```
   
   Or download as ZIP from GitHub and extract.

2. **Run directly**
   
   ```bash
   # Single repo
   python src/git_auto_updater.py /path/to/repo --remote https://github.com/user/repo.git
   
   # Multiple repos
   python src/git_multi_updater.py
   ```

### Method 2: System-wide Installation (Recommended for Frequent Use)

1. **Clone or download the project** (same as Method 1)

2. **Install using pip**
   
   ```bash
   pip install -e .
   ```
   
   The `-e` flag installs in "editable" mode, allowing you to modify the code if needed.

3. **Use as system commands**
   
   ```bash
   git-auto-updater /path/to/repo
   git-multi-updater
   ```

4. **Uninstall** (if needed)
   ```bash
   pip uninstall git-auto-updater
   ```

### Method 3: Virtual Environment (Best Practice)

1. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

2. **Activate virtual environment**
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **Linux/Mac:**
   ```bash
   source venv/bin/activate
   ```

3. **Install in virtual environment**
   ```bash
   pip install -e .
   ```

4. **Deactivate** (when done)
   ```bash
   deactivate
   ```

### Method 4: Windows Service (Auto-start on Boot)

1. **Create a batch script** (`start_updater.bat`):
   ```batch
   @echo off
   cd C:\path\to\git-auto-updater
   git-multi-updater
   ```

2. **Install as Windows Service** (using [NSSM](https://nssm.cc/)):
   ```bash
   nssm install GitAutoUpdater C:\path\to\start_updater.bat
   nssm start GitAutoUpdater
   ```

### Method 5: Systemd Service (Linux)

1. **Create service file** `/etc/systemd/system/git-auto-updater.service`:
   ```ini
   [Unit]
   Description=Git Auto Updater Service
   After=network.target

   [Service]
   Type=simple
   User=nisconder
   WorkingDirectory=/path/to/git-auto-updater
   ExecStart=/usr/bin/python3 /path/to/git-auto-updater/src/git_multi_updater.py
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

2. **Enable and start service**
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable git-auto-updater
   sudo systemctl start git-auto-updater
   ```

## Verifying Installation

### Quick Test

```bash
# Test single repo command
git-auto-updater --help
# or
python src/git_auto_updater.py --help

# Test multi-repo command
git-multi-updater --help
# or
python src/git_multi_updater.py --help
```

### Full Environment Check

```bash
python check_env.py
```

Expected output:
```
============================================================
Git Auto Updater Environment Check
============================================================

Python version: 3.x.x
[OK] Python version meets requirements (>= 3.8)

Git installation:
[OK] Git version: git version 2.x.x

Project files:
[OK] src/git_auto_updater.py
[OK] src/git_multi_updater.py
[OK] git_repos.example.txt

Script test:
[OK] git_auto_updater.py can run properly

============================================================
Check Results Summary:
============================================================
Python version: [PASS]
Git installation: [PASS]
Project files: [PASS]
Script test: [PASS]
============================================================

[OK] All checks passed! You can start using Git Auto Updater
```

### Test with a Real Repository

```bash
# Single repo test
git-auto-updater /tmp/test-repo --remote https://github.com/octocat/Hello-World.git --once

# Multi-repo test
cp git_repos.example.txt git_repos.txt
# Edit git_repos.txt to add a test repository
git-multi-updater --status
```

## Troubleshooting

### Common Issues

#### 1. "Command not found" error

**Symptom:**
```
'git-auto-updater' is not recognized as an internal or external command
```

**Solution:**
- Make sure you installed with `pip install -e .`
- Check if Python Scripts directory is in PATH
- Use full path: `python src/git_auto_updater.py`

#### 2. "No module named" error

**Symptom:**
```
ModuleNotFoundError: No module named 'xxx'
```

**Solution:**
- Reinstall: `pip install -e .`
- Check Python version (needs 3.8+)
- Use virtual environment

#### 3. Permission denied

**Symptom:**
```
PermissionError: [Errno 13] Permission denied
```

**Solution:**
- Run as administrator/sudo
- Check file permissions
- Ensure write access to repository paths

#### 4. Git authentication errors

**Symptom:**
```
fatal: could not read Username for 'https://github.com'
```

**Solution:**
- Configure Git credentials:
  ```bash
  git config --global credential.helper store
  ```
- Or use SSH URLs instead of HTTPS
- Or use personal access tokens

#### 5. Encoding issues on Windows

**Symptom:**
```
UnicodeDecodeError or garbled text
```

**Solution:**
- Use Python 3.8+
- Run environment check: `python check_env.py`
- Check if terminal supports UTF-8

### Getting Help

If you encounter issues not covered here:

1. Check the [README.md](README.md) for usage information
2. Check [examples/usage_examples.md](examples/usage_examples.md) for detailed examples
3. Run `python check_env.py` to diagnose issues
4. Submit an issue on GitHub with:
   - Your operating system
   - Python version
   - Git version
   - Error message
   - Steps to reproduce

## Next Steps

After successful installation:

1. Read [QUICKSTART.md](QUICKSTART.md) for a quick start
2. Read [README.md](README.md) for complete features
3. Check [examples/usage_examples.md](examples/usage_examples.md) for detailed examples
4. Configure your repositories and start monitoring!

---

**Need help?** Submit an issue on GitHub or check the documentation.
