# Python Project Template

Basic Python project structure with modern best practices.

## Features

- **pyproject.toml** - Modern Python packaging
- **src layout** - Proper package structure
- **pytest** - Testing framework
- **black** - Code formatting
- **pylint** - Linting
- **mypy** - Type checking

## Usage

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Install dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black src/ tests/

# Lint
pylint src/

# Type check
mypy src/
```

## Project Structure

```
project/
├── src/
│   └── mypackage/
│       ├── __init__.py
│       └── main.py
├── tests/
│   └── test_main.py
├── pyproject.toml
├── README.md
└── .gitignore
```
