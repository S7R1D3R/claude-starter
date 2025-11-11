# Project Templates

Ready-to-use project templates for various languages and frameworks.

## Available Templates

### Python

#### `python-basic/`
Basic Python project with modern tooling:
- pyproject.toml (PEP 517/518)
- src layout
- pytest, black, pylint, mypy
- **Best for:** CLI tools, libraries, APIs

**Quick start:**
```bash
cp -r templates/python-basic/ my-project/
cd my-project
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

---

### JavaScript/TypeScript

#### `javascript-node/`
Node.js/Express with TypeScript:
- Express.js web framework
- TypeScript configuration
- Jest testing
- ESLint + Prettier
- **Best for:** REST APIs, web services, backends

**Quick start:**
```bash
cp -r templates/javascript-node/ my-project/
cd my-project
npm install
npm run dev
```

---

### Rust

#### `rust-basic/`
Standard Rust project:
- Cargo configuration
- Release optimizations
- Testing setup
- **Best for:** CLI tools, system programming, performance-critical apps

**Quick start:**
```bash
cp -r templates/rust-basic/ my-project/
cd my-project
cargo build
cargo run
```

---

## Using Templates

### Method 1: Copy Template

```bash
# Copy template to new project
cp -r templates/<template-name>/ /path/to/new-project/

# Navigate to project
cd /path/to/new-project/

# Initialize git
git init

# Install dependencies (see template README)
```

### Method 2: Use with Claude Code

```bash
# Start Claude Code
claude-code

# Ask Claude to initialize from template
> Initialize a new Python project using the python-basic template
```

### Method 3: Use /dev:init Command

```bash
# The /dev:init command can automatically use these templates
/dev:init

# Claude will ask which template to use
```

---

## Customizing Templates

### Modify Existing Template

1. Navigate to template directory
2. Edit files as needed
3. Update template README
4. Test the template

### Create New Template

1. Create directory in `templates/`:
   ```bash
   mkdir templates/my-template
   ```

2. Add template files:
   - README.md (required - usage instructions)
   - Configuration files (package.json, Cargo.toml, etc.)
   - Source code structure
   - .gitignore

3. Document:
   - Features
   - Dependencies
   - Quick start
   - Project structure

4. Test template:
   ```bash
   cp -r templates/my-template /tmp/test-project
   cd /tmp/test-project
   # Follow README instructions
   ```

---

## Template Requirements

Every template should include:

1. **README.md** - Clear usage instructions
2. **Configuration files** - Package manager, build tools
3. **.gitignore** - Appropriate ignores for language/framework
4. **Example code** - Basic working example
5. **Testing setup** - Test configuration and examples

### Optional but Recommended:

- LICENSE file
- CONTRIBUTING.md
- Example .env file
- Docker configuration
- CI/CD configuration

---

## Template Best Practices

### 1. Keep Templates Minimal

- Include only essential dependencies
- Avoid opinionated frameworks
- Let users add what they need

### 2. Use Modern Tools

- Use latest stable versions
- Follow current best practices
- Use standard project layouts

### 3. Document Well

- Clear, step-by-step instructions
- Explain what each file does
- Include common commands

### 4. Make it Runnable

- Template should work immediately after setup
- Include a simple "hello world" example
- All tests should pass

### 5. Follow Standards

- Use standard project structure for each language
- Follow naming conventions
- Use idiomatic code

---

## Future Templates

Planned templates (contributions welcome!):

- [ ] `python-fastapi/` - FastAPI web framework
- [ ] `python-django/` - Django web framework
- [ ] `javascript-react/` - React SPA
- [ ] `javascript-vue/` - Vue.js SPA
- [ ] `rust-actix/` - Actix web framework
- [ ] `go-basic/` - Go CLI/API
- [ ] `go-gin/` - Gin web framework
- [ ] `java-spring/` - Spring Boot
- [ ] `kotlin-basic/` - Kotlin project

---

## Contributing Templates

To contribute a new template:

1. **Create template directory** with all necessary files
2. **Test thoroughly** - Ensure it works from scratch
3. **Document clearly** - Include comprehensive README
4. **Submit PR** with:
   - Template files
   - Update to this README
   - Example usage

### Template Checklist

- [ ] README.md with usage instructions
- [ ] Configuration files (package.json, etc.)
- [ ] Example source code
- [ ] Test configuration and examples
- [ ] .gitignore
- [ ] Works from fresh copy
- [ ] All dependencies are current versions
- [ ] Follows language/framework best practices

---

## Support

If you have issues with templates:

1. Check template README for specific instructions
2. Verify all dependencies are installed
3. Check version compatibility
4. Open issue with:
   - Template name
   - Steps to reproduce
   - Error messages
   - Environment info (OS, language version)

---

**Version:** 1.0.0
**Last Updated:** 2025-11-11
