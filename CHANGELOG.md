# Changelog

All notable changes to Git Auto Updater will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2024-01-15

### Added
- Single repository auto-update tool (`git_auto_updater.py`)
- Multiple repositories management tool (`git_multi_updater.py`)
- Automatic detection of remote repository changes
- Configurable check interval
- Multi-threaded concurrent monitoring for multiple repos
- Detailed logging with timestamps
- Pure Python implementation with no external dependencies
- Cross-platform support (Windows/Linux/Mac)
- Comprehensive documentation (README, QUICKSTART, INSTALL, examples)
- Environment check script for easy troubleshooting
- Example configuration file for multi-repo setup
- setup.py for easy installation as system commands
- MIT License

### Features
- Auto-clone repositories if they don't exist
- Force sync strategy (fetch + reset + clean) to ensure consistency
- Status display for all monitored repositories
- One-time check mode for manual updates
- Custom configuration file support
- Support for both SSH and HTTPS repository URLs

### Documentation
- Main README with complete feature overview
- Quick start guide for 5-minute setup
- Detailed installation guide with multiple methods
- Usage examples with common scenarios
- Troubleshooting section for common issues

### Initial Release
- First stable release of Git Auto Updater
- Fully functional single and multi-repo support
- Production-ready with comprehensive testing
