# Contributing to OneChat Python Library

Thank you for your interest in contributing to **one-chat-api**! We appreciate all the help we can get to make this library better for everyone. Whether it's reporting bugs, suggesting new features, improving documentation, or submitting code changes, all contributions are highly valued.

This document outlines the guidelines for contributing to this project.

---

## 🛠️ Getting Started

1. **Fork the repository** to your own GitHub account.
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/one-chat-api.git
   cd one-chat-api
   ```
3. **Set up your environment**. Python 3.8 or higher is required. We recommend using a virtual environment.
4. **Install dependencies**:
   ```bash
   python -m pip install --upgrade pip
   pip install -e .
   pip install -r requirements.txt
   pip install pytest requests-mock ruff black mypy
   ```

---

## 💻 Development Workflow

Before submitting a Pull Request, please ensure your code follows our quality standards. You can verify this by running the following checks locally:

- **Linting:** Ensure code is clean and adheres to style guidelines.
  ```bash
  ruff check .
  ```
- **Formatting:** Format your code automatically using Black.
  ```bash
  black .
  ```
- **Type Checking:** Verify Python type hints to ensure stability.
  ```bash
  mypy one_chat
  ```
- **Testing:** Run the test suite to ensure no existing functionality is broken.
  ```bash
  pytest
  ```

---

## 📝 Commit Style

We maintain a clean and readable commit history. Please follow these guidelines:

- Keep your commits atomic and focused on a single change.
- Write clear, descriptive, and imperative commit messages (e.g., "Add broadcast message validation", "Fix type hint in send_location").
- If your commit resolves an open issue, reference it in the commit message (e.g., "Fixes #123").

---

## 🚀 Submitting a Pull Request (PR)

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/my-new-feature
   ```
2. Make your changes and commit them.
3. Push your branch to your fork:
   ```bash
   git push origin feature/my-new-feature
   ```
4. Open a Pull Request against the `main` branch of the upstream repository.
5. In your PR description, explain what changes you made and why.
6. Ensure that the Continuous Integration (CI) checks (linting, typing, tests) pass successfully.
7. If your changes affect user-facing behavior, please update the `README.md` or relevant documentation accordingly.

---

## 🐞 Reporting Bugs & Requesting Features

If you encounter any bugs or have ideas for new features, please use the **GitHub Issues** page.

- **Bugs:** Provide a clear and concise description, along with steps to reproduce the issue. A minimal reproducible example is always appreciated.
- **Features:** Explain why the feature would be useful and how it should work.

---

## 🛡️ Security Vulnerabilities

If you discover a security vulnerability within the library, **please do not open a public issue**. Instead, follow the guidelines outlined in our [SECURITY.md](SECURITY.md) file to report it responsibly.

---

Thank you for contributing!
