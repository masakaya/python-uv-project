# Project Rules for Claude Code

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
