# Contributing to one-chat-api

Thanks for your interest in contributing! This document explains how to set up your environment, run checks, and submit changes.

## Getting started
- Fork and clone the repo
- Python 3.8+ recommended
- Install dev deps:
  - `python -m pip install --upgrade pip`
  - `pip install -e .`
  - `pip install -r requirements.txt`
  - `pip install pytest requests-mock ruff black mypy`

## Development workflow
- Lint: `ruff check .`
- Format: `black .`
- Type check: `mypy one_chat`
- Tests: `pytest`

## Commit style
- Keep commits focused; reference issues like `#123` when relevant
- Use clear, imperative messages (e.g., "Add broadcast validation")

## Pull requests
- Ensure CI passes (lint, type check, tests)
- Add/adjust tests for new behavior
- Update docs/README if user-facing behavior changes

## Reporting bugs / requesting features
- Use GitHub Issues and fill out the templates
- Provide minimal reproduction for bugs when possible

## Security
- Please do not file public issues for security reports. See SECURITY.md.

