# Claude Code Starter Boilerplate

## Project Overview

This is a **language-agnostic starter boilerplate** for Claude Code, incorporating all the latest 2025 features and best practices. It provides intelligent automation, code quality enforcement, and productivity enhancements for any programming language or framework.

## Purpose

Provide a production-ready Claude Code setup with:
- Automated code quality checks
- Security validation
- Intelligent prompt enhancement
- Comprehensive slash commands
- GitHub Actions integration
- MCP server configurations

## Tech Stack Detection

This boilerplate **automatically detects** your project's:
- Primary programming language(s)
- Package manager (npm, pip, cargo, go mod, maven, etc.)
- Testing framework
- Build tools
- Linting/formatting tools

## Development Workflow

### Essential Commands

**Installation:**
```bash
# The /dev:setup command will auto-detect and run the appropriate command
npm install     # Node.js
pip install -r requirements.txt  # Python
cargo build     # Rust
go mod download # Go
mvn install     # Java/Maven
```

**Testing:**
```bash
# Use /quality:test or run manually
npm test        # Node.js
pytest          # Python
cargo test      # Rust
go test ./...   # Go
mvn test        # Java/Maven
```

**Linting & Formatting:**
```bash
# Use /quality:lint and /quality:format
npm run lint    # Node.js/ESLint
black .         # Python
cargo clippy    # Rust
golint ./...    # Go
```

**Building:**
```bash
# Use /dev:build
npm run build   # Node.js
python setup.py build  # Python
cargo build --release  # Rust
go build        # Go
mvn package     # Java/Maven
```

## Code Standards

### Commit Convention
- Use **Conventional Commits**: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`
- Write clear, descriptive commit messages
- Reference issue numbers when applicable

### Code Quality Rules
- **IMPORTANT**: Always run tests before committing
- Keep functions under 50 lines when possible
- Write self-documenting code with clear names
- Add comments for complex logic
- Document all public APIs
- Follow language-specific style guides

### Testing Requirements
- Write unit tests for new features
- Maintain >80% code coverage
- Test edge cases and error conditions
- Use meaningful test descriptions

### Security Guidelines
- NEVER commit secrets, API keys, or credentials
- Use environment variables for configuration
- Validate all user inputs
- Follow OWASP Top 10 security practices
- Run security audits before releases

## Architecture Patterns

### Project Structure
```
project-root/
├── src/           # Source code
├── tests/         # Test files
├── docs/          # Documentation
├── .claude/       # Claude Code configuration
├── .github/       # GitHub Actions workflows
└── README.md      # Project documentation
```

### Best Practices
- Separate concerns (business logic, UI, data access)
- Use dependency injection
- Follow SOLID principles
- Keep configurations externalized
- Maintain single source of truth

## AI Assistant Instructions

### Before Making Changes
1. **ALWAYS** understand the full context by reading relevant files
2. **NEVER** make assumptions about project structure
3. Use `/ai:context` for complex tasks requiring broad understanding
4. Check for existing patterns and conventions in the codebase

### During Development
1. Write clean, maintainable, and well-documented code
2. Follow the existing code style and patterns
3. Add appropriate error handling
4. Consider edge cases and potential bugs
5. **IMPORTANT**: Run `/quality:test` after code changes

### Before Committing
1. **MANDATORY**: Run `/quality:review` to check code quality
2. Ensure all tests pass with `/quality:test`
3. Format code with `/quality:format`
4. Run `/quality:lint` to check for issues
5. Use `/git:commit` for structured commits

### Security Awareness
- **NEVER** disable security hooks without explicit permission
- **ALWAYS** validate file operations in sensitive directories
- **BLOCK** any dangerous commands (rm -rf, sudo rm, chmod 777)
- **VERIFY** all external dependencies before installation

## Available Slash Commands

### Development (/dev:)
- `/dev:init` - Initialize new project with auto-detection
- `/dev:setup` - Install dependencies based on detected stack
- `/dev:serve` - Start development server
- `/dev:build` - Build project for production
- `/dev:clean` - Clean build artifacts and caches

### Git Operations (/git:)
- `/git:commit` - Create conventional commit with auto-generated message
- `/git:pr` - Generate PR with comprehensive description
- `/git:sync` - Sync with remote and resolve conflicts
- `/git:branch` - Create feature branch with naming convention

### Code Quality (/quality:)
- `/quality:review` - Comprehensive code review with suggestions
- `/quality:lint` - Run all configured linters
- `/quality:format` - Auto-format all code files
- `/quality:test` - Execute full test suite
- `/quality:security` - Run security vulnerability scan

### Documentation (/docs:)
- `/docs:generate` - Generate API documentation from code
- `/docs:readme` - Update README with latest changes
- `/docs:changelog` - Generate CHANGELOG entries

### AI Enhancement (/ai:)
- `/ai:context` - Load comprehensive project context
- `/ai:refactor` - Intelligent refactoring with best practices
- `/ai:explain` - Explain complex code sections in detail

## Hooks & Automation

This project includes intelligent hooks that run automatically:

### Session Start
- Loads git status and recent commits
- Displays project context
- Checks for uncommitted changes
- Initializes language-specific tools

### Prompt Enhancement (Pre-Submit)
- Adds relevant project context
- Injects coding standards
- Appends error logs if applicable
- Structures vague requests

### Security Validation (Pre-Tool-Use)
- Blocks dangerous operations
- Protects sensitive files
- Validates file paths
- Logs security events

### Quality Automation (Post-Tool-Use)
- Auto-formats modified code
- Runs relevant linters
- Executes affected tests
- Suggests commit messages

### Final Validation (Stop)
- Verifies all tests pass
- Checks for TODO/FIXME comments
- Ensures documentation is updated
- Sends completion notifications

## External Context

Import additional configuration and documentation:
@.claude/commands/
@docs/

## Project-Specific Notes

_This section will be auto-populated based on your specific project. Add custom instructions, patterns, or conventions here using the `#` key in Claude Code._

## Quick Start

1. Run `/dev:setup` to install dependencies
2. Run `/quality:test` to verify setup
3. Start coding with AI assistance
4. Use `/quality:review` before committing
5. Use `/git:commit` to create structured commits
6. Use `/git:pr` to create pull requests

## Support

- Documentation: See `docs/` directory
- Hooks Guide: `docs/HOOKS.md`
- Commands Reference: `docs/COMMANDS.md`
- MCP Setup: `docs/MCP_SERVERS.md`
- Setup Guide: `docs/SETUP.md`

---

**Remember**: This boilerplate enforces quality and security automatically. Trust the hooks and use the slash commands for maximum productivity!
