# Changelog

All notable changes to this project will be documented in this file.

## [0.4.1] - 2025-09-15
### Added
- Extensive unit tests across all senders and wrappers
- Issue/PR templates, CONTRIBUTING.md, SECURITY.md
- .env.example for safe local usage

### Changed
- Python support: requires Python >= 3.8 (classifiers updated)
- Typing compatibility for 3.8 (avoid built-in generics like list[str])
- Standardized error handling (fail status) in broadcast sender
- Requests dependency relaxed to `>=2.32.2` for Py3.8 CI
- Consistent request timeouts across all HTTP calls
- CI workflow for lint/type/test on PR and push

### Fixed
- Broadcast API normalization and type handling for recipients
- Mypy clean across the codebase

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
