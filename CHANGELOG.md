# Changelog

All notable changes to this project will be documented in this file.

## [0.4.0] - 2025-09-15
### Added
- CI workflow for lint, type check, tests
- CONTRIBUTING.md, SECURITY.md, issue/PR templates
- pyproject.toml configuration; typed marker `py.typed`
- Examples folder
- Basic unit tests for message and broadcast

### Changed
- Broadcast API now accepts lists consistently; normalizes single string
- Added request timeouts across all network calls
- Consistent error handling for senders
 - Relax dependency: `requests>=2.32.2` to support Python 3.8 CI
