# Contributing to Claude Code Starter

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)

---

## Code of Conduct

This project adheres to a Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details.

---

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports:
- **Search existing issues** to avoid duplicates
- **Check the documentation** - the issue might be expected behavior
- **Test with the latest version** - the bug may already be fixed

When creating a bug report, use the bug report template and include:
- Clear, descriptive title
- Steps to reproduce
- Expected vs actual behavior
- Error logs if applicable
- Environment details (OS, Claude Code version)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. Use the feature request template and include:
- **Use case**: Describe the problem you're trying to solve
- **Proposed solution**: How you think it should work
- **Alternatives**: Other approaches you considered
- **Examples**: Code examples or mockups

### Contributing Code

1. **Fork the repository**
2. **Create a feature branch** from `main`
3. **Make your changes** following our coding standards
4. **Add tests** for new functionality
5. **Update documentation** as needed
6. **Submit a pull request**

### Improving Documentation

Documentation improvements are always welcome:
- Fix typos or unclear explanations
- Add examples
- Improve setup instructions
- Translate documentation
- Write tutorials or guides

---

## Development Setup

### Prerequisites

- Git 2.28+
- Python 3.7+ (for hooks)
- Claude Code CLI (latest version)
- Language-specific tools (based on your contribution)

### Setup Steps

1. **Fork and clone:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/claude-starter.git
   cd claude-starter
   ```

2. **Create branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Test your setup:**
   ```bash
   # Test hooks
   python3 .claude/hooks/session-start.py '{"type": "sessionStart"}'

   # Verify slash commands
   ls .claude/commands/
   ```

4. **Install pre-commit hooks (optional but recommended):**
   ```bash
   pip install pre-commit
   pre-commit install
   ```

---

## Coding Standards

### General Principles

- **Keep it simple**: Prefer clarity over cleverness
- **DRY**: Don't repeat yourself
- **YAGNI**: You ain't gonna need it (don't over-engineer)
- **Self-documenting code**: Use clear names, add comments for complex logic
- **Test your code**: Include tests for new features

### Language-Specific Standards

#### Python (Hooks)

- Follow **PEP 8** style guide
- Use **type hints** where appropriate
- Maximum line length: **88** characters (Black default)
- Use **docstrings** for functions and classes
- Format with **Black**: `black .claude/hooks/`

```python
def process_input(data: dict) -> dict:
    """Process input data and return result.

    Args:
        data: Input dictionary

    Returns:
        Processed dictionary
    """
    # Implementation
    return result
```

#### Markdown (Documentation)

- Maximum line length: **80** characters (excluding code blocks)
- Use **ATX-style headers** (# instead of ===)
- Include **table of contents** for long documents
- Use **code fences** with language identifiers

#### YAML/JSON (Configuration)

- **2-space indentation**
- Include **comments** explaining configuration options
- Validate syntax before committing

---

## Commit Guidelines

### Conventional Commits

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.

**Format:**
```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, no logic change)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `perf`: Performance improvements
- `ci`: CI/CD changes

**Examples:**
```bash
feat(hooks): add caching to session-start hook

Implement file-based caching for language detection to improve
session startup performance by ~10x on large projects.

Closes #42

---

fix(commands): correct pytest path in quality:test command

The command was using wrong path for pytest configuration.

---

docs(setup): add troubleshooting section for macOS

Added common issues and solutions for macOS users experiencing
installation problems.
```

### Commit Best Practices

- **Atomic commits**: Each commit should represent one logical change
- **Present tense**: "Add feature" not "Added feature"
- **Imperative mood**: "Fix bug" not "Fixes bug"
- **Reference issues**: Use `Closes #123` or `Relates to #456`
- **Keep commits small**: Easier to review and revert if needed

---

## Pull Request Process

### Before Submitting

1. **Update documentation** reflecting your changes
2. **Add tests** for new functionality
3. **Run all tests** and ensure they pass
4. **Update CHANGELOG.md** under "Unreleased" section
5. **Rebase on latest main** to avoid merge conflicts
6. **Self-review** your changes

### Submitting Pull Request

1. **Use the PR template** - Fill out all relevant sections
2. **Link related issues** - Reference issues being addressed
3. **Describe changes clearly** - What, why, and how
4. **Add screenshots/examples** if applicable
5. **Mark as draft** if work in progress

### PR Title Format

Follow Conventional Commits for PR titles:
```
feat: Add session-start caching
fix: Correct pytest configuration path
docs: Improve setup instructions for Windows
```

### Review Process

- Maintainers will review within **3-5 business days**
- Address feedback by **pushing new commits** (don't force-push during review)
- Request re-review after addressing feedback
- PRs with failing tests won't be merged
- At least **one approval** required before merge

### After Merge

- Delete your feature branch
- Pull latest main: `git pull origin main`
- Your contribution will be credited in the next release!

---

## Testing Guidelines

### Hook Testing

Test hooks manually before submitting:

```bash
# Test session-start hook
python3 .claude/hooks/session-start.py '{"type": "sessionStart"}'

# Test pre-tool-use hook (should block)
python3 .claude/hooks/pre-tool-use.py '{
  "type": "preToolUse",
  "tool": "Bash",
  "parameters": {"command": "rm -rf /"}
}'

# Check exit code
echo $?  # Should be 2 (blocked)
```

### Command Testing

Test slash commands using Claude Code:

```bash
# Start Claude Code in a test project
cd /tmp/test-project
claude-code

# Try your command
/your:command
```

### Test Checklist

- [ ] Hook runs without errors
- [ ] Hook produces expected output (JSON format)
- [ ] Security hooks properly block dangerous operations
- [ ] Performance is acceptable (hooks run in < 5 seconds)
- [ ] Error handling works correctly
- [ ] Edge cases are handled

---

## Documentation

### What to Document

- **New features**: Usage instructions and examples
- **Breaking changes**: Migration guide
- **Configuration options**: Purpose and valid values
- **Hooks**: When they run, what they do, and how to configure
- **Commands**: Syntax, options, and examples

### Documentation Structure

```markdown
# Feature Name

Brief description (1-2 sentences)

## Usage

bash
# Example command


## Options

- `--option`: Description

## Examples

### Example 1

Description

bash
code example


## Troubleshooting

Common issues and solutions
```

### Documentation Locations

- `README.md` - Project overview, quick start
- `CLAUDE.md` - Instructions for Claude AI
- `docs/SETUP.md` - Detailed installation and configuration
- `docs/HOOKS.md` - Hook reference
- `docs/COMMANDS.md` - Command reference
- `docs/SKILLS.md` - Skills system guide
- Code comments - Complex logic, non-obvious behavior

---

## Contribution Checklist

Before submitting your PR, verify:

### Code
- [ ] Code follows project style guidelines
- [ ] No new warnings or errors introduced
- [ ] Existing tests pass
- [ ] New tests added for new functionality
- [ ] Code reviewed by yourself first

### Documentation
- [ ] README updated if needed
- [ ] Relevant docs updated
- [ ] Code comments added for complex logic
- [ ] Examples provided for new features

### Git
- [ ] Commits follow Conventional Commits format
- [ ] Branch is up to date with main
- [ ] No merge conflicts
- [ ] Commit messages are clear and descriptive

### Testing
- [ ] Manually tested changes
- [ ] Tested on multiple scenarios
- [ ] Edge cases considered
- [ ] Error handling verified

---

## Getting Help

### Communication Channels

- **GitHub Issues**: Bug reports, feature requests
- **GitHub Discussions**: Questions, ideas, showcase
- **Pull Request Comments**: Code review discussions

### Questions?

- Check existing documentation first
- Search closed issues - your question might be answered
- Open a new discussion for general questions
- Open an issue for bugs or feature requests

---

## Recognition

Contributors are recognized in:
- **CHANGELOG.md** - Listed in each release
- **README.md** - Contributors section
- **Release notes** - Notable contributions highlighted

---

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT License).

---

**Thank you for contributing to Claude Code Starter! 🎉**
