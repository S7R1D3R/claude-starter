---
description: Run linters to check code quality and style
---

# Run Linters

Execute appropriate linters based on project type and report issues.

## Auto-Detect Linters

Check for configuration files and run corresponding linters:

### JavaScript/TypeScript
- **.eslintrc.*** → `eslint . --ext .js,.jsx,.ts,.tsx`
- **package.json** with eslint → `npm run lint` or `eslint .`
- **.prettierrc.*** → `prettier --check .`

### Python
- **pylintrc** or **setup.cfg** → `pylint src/`
- **.flake8** → `flake8 .`
- **mypy.ini** → `mypy .`
- **pyproject.toml** → Check for configured linters

### Rust
- **Cargo.toml** → `cargo clippy -- -D warnings`
- **rustfmt.toml** → `cargo fmt --check`

### Go
- **go.mod** → `golint ./...` and `go vet ./...`
- **.golangci.yml** → `golangci-lint run`

### Ruby
- **.rubocop.yml** → `rubocop`

### Java
- **checkstyle.xml** → `checkstyle`
- **pom.xml** → `mvn checkstyle:check`

### PHP
- **phpcs.xml** → `phpcs`
- **psalm.xml** → `psalm`

## Execution Process

1. **Detect** available linters
2. **Run** each linter sequentially
3. **Collect** all issues
4. **Categorize** by severity
5. **Report** findings

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔍 LINTING RESULTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ ESLint: Passed
✗ Prettier: 3 files need formatting

src/components/Button.jsx
  ✗ Line 23: Missing space before function parentheses
  ✗ Line 45: Line exceeds 80 characters

src/utils/api.js
  ⚠ Line 12: Prefer const over let when variable is not reassigned

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Summary: 2 errors, 1 warning
Run /quality:format to auto-fix formatting issues
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Auto-Fix Option

If linter supports auto-fix:
- Inform user about fixable issues
- Suggest running with `--fix` flag
- Or suggest `/quality:format` command

## Exit Status

- **Success (all passed)**: Report clean status
- **Warnings only**: Report warnings, suggest fixes
- **Errors found**: Report errors, suggest fixes or /quality:review

## Integration with CI/CD

If linting fails, remind user that:
- CI/CD may block PR
- Suggest fixing before committing
- Provide specific fix commands

## Arguments

- `/quality:lint` - Run all available linters
- `/quality:lint src/` - Lint specific directory
- `/quality:lint --fix` - Auto-fix issues where possible

**IMPORTANT**: Always show the full command being run for transparency.
