---
description: Generate API documentation from code comments and structure
---

# Generate Documentation

Automatically generate API documentation from code structure and comments.

## Documentation Tools by Language

### JavaScript/TypeScript
- **JSDoc** → `jsdoc src/ -d docs/api`
- **TypeDoc** → `typedoc src/ --out docs/api`
- **documentation.js** → `documentation build src/** -f html -o docs/api`

### Python
- **Sphinx** → `sphinx-build -b html docs/ docs/_build`
- **pdoc** → `pdoc --html --output-dir docs/api src/`
- **mkdocs** → `mkdocs build`

### Rust
- **cargo doc** → `cargo doc --no-deps --open`

### Go
- **godoc** → `godoc -http=:6060` or `go doc`
- **pkgsite** → For package documentation

### Java
- **Javadoc** → `javadoc -d docs/api src/**/*.java`

### Ruby
- **YARD** → `yard doc`
- **RDoc** → `rdoc`

### PHP
- **phpDocumentor** → `phpdoc -d src/ -t docs/api`

## Documentation Generation Process

### 1. Detect Documentation Tool
Check for:
- Existing configuration files
- Language-specific doc generators
- Package.json scripts

### 2. Scan Codebase Structure
Identify:
- Public APIs
- Exported functions/classes
- Module structure
- Entry points

### 3. Extract Documentation
From:
- JSDoc/docstring comments
- Type definitions
- Function signatures
- Module exports

### 4. Generate Documentation
Run appropriate tool:
```bash
# TypeScript example
typedoc --entryPoints src/index.ts --out docs/api
```

### 5. Enhance Documentation
Add:
- Usage examples
- Code snippets
- Architecture diagrams (if applicable)
- Getting started guide

## Output Structure

```
docs/
├── api/              # Auto-generated API docs
│   ├── index.html
│   ├── modules/
│   └── classes/
├── guides/           # Manual guides
│   ├── getting-started.md
│   └── tutorials/
├── architecture/     # Architecture docs
│   └── overview.md
└── assets/           # Images, diagrams
```

## Post-Generation

After generating docs:
1. Open documentation in browser (if HTML)
2. Verify all public APIs are documented
3. Check for broken links
4. Suggest hosting options:
   - GitHub Pages
   - Read the Docs
   - Netlify/Vercel

## Documentation Coverage Check

Scan for undocumented code:
```
Missing documentation:
  • src/utils/api.ts:45 - Function `fetchData` has no JSDoc
  • src/models/User.ts:12 - Class `User` has no description

Coverage: 78% (23/30 public APIs documented)
```

## Integration with README

Update README.md with:
- Link to generated documentation
- Quick API reference
- Example usage

## Arguments

- `/docs:generate` - Generate full documentation
- `/docs:generate src/api` - Document specific module
- `/docs:generate --open` - Open docs in browser after generation

**IMPORTANT**: Ensure code comments are comprehensive before generating documentation.
