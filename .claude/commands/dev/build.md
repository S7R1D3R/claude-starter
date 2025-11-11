---
description: Build the project for production
---

# Build Project for Production

Execute the production build process for the project.

## Build Commands by Type

### JavaScript/TypeScript
- **package.json** with "build" script → `npm run build`
- **Vite** → Creates `dist/`
- **Next.js** → Creates `.next/`
- **React** → Creates `build/`
- **TypeScript** → `tsc` or `npx tsc`

### Python
- **setup.py** → `python setup.py build` or `python -m build`
- **pyproject.toml** → `poetry build` or `python -m build`

### Rust
- **Cargo.toml** → `cargo build --release`

### Go
- **go.mod** → `go build -o bin/app` or `go build .`

### Java
- **Maven** → `mvn clean package`
- **Gradle** → `gradle build`

## Build Process

1. **Clean** previous build artifacts if necessary
2. **Run** the build command
3. **Verify** build succeeded
4. **Report** output location
5. **Check** build size and provide optimization tips if large

## Optimization Checks

After building:
- Report bundle size
- Suggest optimizations if build is large (>5MB for web apps)
- Check for source maps in production
- Verify minification

## Error Handling

If build fails:
- Show error output
- Suggest common fixes (missing dependencies, type errors, etc.)
- Recommend running tests first

**Arguments**: Accepts `$ARGUMENTS` for build flags (e.g., `/dev:build --production`)
