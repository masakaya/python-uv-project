# Project Rules for Claude Code

## Branch Protection Policy

**IMPORTANT: Direct push to the following branches is PROHIBITED:**

- `main` - Main branch (stable code)
- `staging` - Staging environment branch
- `production` - Production environment branch

### Workflow

1. Create a feature branch from `main`
2. Make changes and commit
3. Create a Pull Request to `main`
4. After review and merge to `main`, auto-promotion PRs will be created:
   - `main` → `staging` (automatic PR)
   - `staging` → `production` (automatic PR after staging merge)
5. Production merge triggers automatic release creation (version tag + CHANGELOG)

**Always work through Pull Requests. Never push directly to protected branches.**

## Code Quality Standards

This project adheres to strict code quality standards:

### Ruff (Linting & Formatting)

- **All code must pass Ruff checks** before merging
- Ruff automatically formats code on PR creation
- Configuration: `ruff.toml`
- Run locally: `poe lint` or `poe format`

### mypy (Type Checking)

- **All code must pass mypy type checks** before merging
- Type annotations are required for all functions
- Configuration: `pyproject.toml` (`[tool.mypy]` section)
- Run locally: `poe typecheck`

### Enforcement

- GitHub Actions automatically runs Ruff and mypy on all PRs
- reviewdog posts inline comments for any violations
- PRs cannot be merged until all checks pass

**When writing code, ensure it complies with both Ruff and mypy standards.**

## Package Management

This project uses **uv** for package management. **DO NOT use pip**.

### Installing Dependencies

- Use `uv sync` to install all dependencies from pyproject.toml
- Use `uv add <package>` to add a new runtime dependency
- Use `uv add --dev <package>` to add a new development dependency
- Use `uv remove <package>` to remove a dependency

### Running Python

- Use `uv run python <script>` to run Python scripts
- Use `uv run <command>` to run commands in the virtual environment

### Why uv?

uv is a fast Python package installer and resolver written in Rust. It provides:
- Faster dependency resolution and installation
- Better reproducibility
- Built-in virtual environment management
- Compatibility with pip and pyproject.toml standards
