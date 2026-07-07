# Contributing to site-selection-ga

We love your input! We want to make contributing to this project as easy and transparent as possible.

## 📋 Development Process

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/YOUR_USERNAME/site-selection-ga.git`
3. **Create a branch**: `git checkout -b feature/your-feature-name`
4. **Install dependencies**: `pip install -r requirements.txt && pip install -r requirements-dev.txt`
5. **Make your changes**
6. **Run tests**: `pytest --cov=src tests/`
7. **Check code style**: `ruff check . && black .`
8. **Commit and push**: `git commit -m "Add your feature" && git push origin feature/your-feature-name`
9. **Open a Pull Request**

---

## 🧪 Testing Guidelines

- All new features must include unit tests.
- Maintain or improve code coverage (currently 97%).
- Run tests locally before pushing:
  ```bash
  pytest --cov=src tests/
  ```

---

## 🎨 Code Style

We use:
- **Black** for code formatting
- **Ruff** for linting
- **isort** for import sorting

Format your code before committing:
```bash
black .
ruff check --fix .
```

---

## 📝 Commit Message Guidelines

Use clear and descriptive commit messages:

```bash
git commit -m "feat: add new fitness function parameter"
git commit -m "fix: resolve bug in visualization module"
git commit -m "docs: update README with installation instructions"
```

---

## 🏷️ Versioning

We follow [Semantic Versioning](https://semver.org/):
- **MAJOR** version for incompatible API changes
- **MINOR** version for backwards-compatible functionality
- **PATCH** version for backwards-compatible bug fixes

---

## 📄 License

By contributing, you agree that your contributions will be licensed under the **MIT License**.
