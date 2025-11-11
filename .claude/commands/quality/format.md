---
description: Auto-format code using configured formatters
---

# Format Code

Automatically format code using appropriate formatters.

## Auto-Detect Formatters

Check for formatters and configuration:

### JavaScript/TypeScript
- **Prettier**: `.prettierrc.*`, `package.json`
  - Command: `prettier --write .`
  - Glob: `**/*.{js,jsx,ts,tsx,json,css,md}`

### Python
- **Black**: `pyproject.toml`, `black.toml`
  - Command: `black .`
- **autopep8**: Setup in config
  - Command: `autopep8 --in-place --recursive .`
- **yapf**: `.style.yapf`
  - Command: `yapf -ir .`

### Rust
- **rustfmt**: `rustfmt.toml`, `Cargo.toml`
  - Command: `cargo fmt`

### Go
- **gofmt**: Always available
  - Command: `gofmt -w .`
- **goimports**: If installed
  - Command: `goimports -w .`

### Ruby
- **RuboCop**: `.rubocop.yml`
  - Command: `rubocop -a`

### Java
- **google-java-format**: If configured
  - Command: `java-format --replace`

### C/C++
- **clang-format**: `.clang-format`
  - Command: `clang-format -i **/*.{c,cpp,h}`

### PHP
- **PHP-CS-Fixer**: `.php-cs-fixer.php`
  - Command: `php-cs-fixer fix`

## Formatting Process

1. **Detect** project language(s)
2. **Check** for formatter installation
3. **Identify** files to format:
   - All files (default)
   - Staged files only (if specified)
   - Specific paths (from arguments)
4. **Run** formatter
5. **Report** formatted files

## Safety

Before formatting:
- Ensure working directory is clean OR
- Warn user about uncommitted changes
- Suggest creating a git checkpoint

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✨ FORMATTING CODE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Running: prettier --write .

✓ src/components/Button.jsx - formatted
✓ src/utils/api.js - formatted
✓ src/App.tsx - formatted
━ tests/unit.test.js - no changes needed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Formatted: 3 files
Unchanged: 1 file
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Configuration Check

If no formatter configuration found:
1. Detect language
2. Suggest popular formatter
3. Offer to create basic configuration
4. Provide setup instructions

## Post-Format Actions

After formatting:
- Run linter to verify no issues introduced
- Suggest reviewing changes with `git diff`
- Remind to commit formatted files

## Arguments

- `/quality:format` - Format all files
- `/quality:format src/` - Format specific directory
- `/quality:format --staged` - Format only staged files
- `/quality:format --check` - Check without modifying (dry run)

**IMPORTANT**: Respect project's formatter configuration. Never force a style.
