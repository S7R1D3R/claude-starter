---
description: Clean build artifacts and caches
---

# Clean Build Artifacts

Remove build artifacts, caches, and temporary files to start fresh.

## Files and Directories to Clean

### JavaScript/Node.js
- `node_modules/` (optional, requires reinstall)
- `dist/`, `build/`, `.next/`, `.nuxt/`
- `.cache/`, `.parcel-cache/`
- `*.log` files

### Python
- `__pycache__/` directories
- `*.pyc`, `*.pyo`, `*.pyd` files
- `.pytest_cache/`, `.tox/`
- `dist/`, `build/`, `*.egg-info/`
- `.coverage`, `htmlcov/`

### Rust
- `target/` directory
- `Cargo.lock` (optional)

### Go
- Binary executables in `bin/`
- `go.sum` (optional, requires rebuild)

### Java
- `target/` (Maven)
- `build/` (Gradle)
- `.gradle/`
- `*.class` files

### General
- `.DS_Store` (macOS)
- `Thumbs.db` (Windows)
- Editor files (`.vscode/.`, `.idea/.`)
- Log files

## Cleaning Process

1. **List** what will be deleted (for user confirmation)
2. **Confirm** with user before deleting node_modules or large directories
3. **Delete** build artifacts
4. **Delete** caches
5. **Report** space recovered
6. **Suggest** running `/dev:setup` to reinstall if dependencies were removed

## Safety

**IMPORTANT**:
- NEVER delete source code
- NEVER delete `.git` directory
- NEVER delete configuration files
- ASK before removing `node_modules` or similar large dependency directories

**Arguments**: Accepts `--deep` to also remove dependency directories
