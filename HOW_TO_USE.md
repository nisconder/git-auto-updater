# How to Use Git Auto Updater

## Quick Start (3 Steps)

### 1. Clone and Verify
```bash
git clone https://github.com/nisconder/git-auto-updater.git
cd git-auto-updater
python check_env.py
```

### 2. Choose Your Usage

**Option A: Single Repository**
```bash
python src/git_auto_updater.py /path/to/your/repo --remote https://github.com/user/repo.git
```

**Option B: Multiple Repositories**
```bash
cp git_repos.example.txt git_repos.txt
# Edit git_repos.txt with your repositories
python src/git_multi_updater.py
```

### 3. Start Monitoring

Run continuously:
```bash
# Single repo
python src/git_auto_updater.py /path/to/your/repo

# Multiple repos
python src/git_multi_updater.py
```

## What You Get

✅ Automatic repository updates
✅ Configurable check intervals (default: 5 minutes)
✅ Detailed logging with timestamps
✅ Multi-threaded support for multiple repos
✅ Cross-platform (Windows/Linux/Mac)

## Need Help?

- Read [README.md](README.md) for full documentation
- Check [QUICKSTART.md](QUICKSTART.md) for detailed examples
- Run `python check_env.py` to verify your environment

## Installation (Optional)

To install as system commands:
```bash
pip install -e .
git-auto-updater /path/to/repo
git-multi-updater
```

---

**Ready to go! Start monitoring your repositories now.**
