# Claude Code Starter Boilerplate

> A comprehensive, language-agnostic starter template featuring all the latest Claude Code capabilities for maximum AI-assisted development productivity.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-2025-purple)](https://claude.ai/code)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

## Features

- **Intelligent Hooks** - Automated code quality, security validation, and prompt enhancement
- **20+ Slash Commands** - Pre-built workflows for development, git, quality checks, and documentation
- **GitHub Actions** - AI-powered PR reviews, issue handling, and automated documentation
- **Expert Skills** - Code review and testing expertise modules
- **MCP Integration** - Ready-to-use Model Context Protocol server configurations
- **Language Agnostic** - Auto-detects your tech stack and adapts accordingly
- **Production Ready** - Battle-tested hooks and workflows from 2025 best practices

## Quick Start

### 1. Installation

```bash
# Clone this repository (or use as GitHub template)
git clone https://github.com/yourusername/claude-starter.git
cd claude-starter

# Run setup wizard
./scripts/setup-wizard.sh
```

### 2. Essential Commands

```bash
# Initialize project
/dev:init

# Install dependencies
/dev:setup

# Run tests
/quality:test

# Create commit
/git:commit

# Create PR
/git:pr
```

### 3. Start Coding

Open Claude Code in your project directory and start coding! The hooks will automatically:
- Enhance your prompts with project context
- Validate security before operations
- Auto-format and lint code after edits
- Run quality checks on completion

## Project Structure

```
claude-starter/
├── .claude/
│   ├── settings.json              # Hook and permission configuration
│   ├── CLAUDE.md                  # Project context for AI
│   ├── commands/                  # 20+ slash commands
│   │   ├── dev/                   # Development commands
│   │   ├── git/                   # Git workflow commands
│   │   ├── quality/               # Code quality commands
│   │   ├── docs/                  # Documentation commands
│   │   └── ai/                    # AI enhancement commands
│   ├── hooks/                     # Automated event handlers
│   │   ├── session-start.py       # Session initialization
│   │   ├── user-prompt-submit.py  # Prompt enhancement
│   │   ├── pre-tool-use.py        # Security validation
│   │   ├── post-tool-use.py       # Auto quality checks
│   │   ├── stop.py                # Final validation
│   │   └── notification.py        # Desktop notifications
│   └── skills/                    # Expert knowledge modules
│       ├── code-review/           # Code review expertise
│       └── testing/               # Testing expertise
├── .github/workflows/             # GitHub Actions
│   ├── claude-pr-review.yml       # AI PR reviews
│   ├── claude-issue-handler.yml   # Issue automation
│   └── claude-docs-update.yml     # Documentation sync
├── docs/                          # Comprehensive documentation
├── scripts/                       # Setup and utility scripts
├── templates/                     # Reusable templates
└── README.md                      # This file
```

## Slash Commands Reference

### Development (`/dev:`)
- `/dev:init` - Initialize new project with auto-detection
- `/dev:setup` - Install dependencies
- `/dev:serve` - Start development server
- `/dev:build` - Build for production
- `/dev:clean` - Clean build artifacts

### Git Operations (`/git:`)
- `/git:commit` - Create conventional commit
- `/git:pr` - Generate and create pull request
- `/git:sync` - Sync with remote
- `/git:branch` - Create feature branch

### Code Quality (`/quality:`)
- `/quality:review` - Comprehensive code review
- `/quality:lint` - Run linters
- `/quality:format` - Auto-format code
- `/quality:test` - Run test suite
- `/quality:security` - Security vulnerability scan

### Documentation (`/docs:`)
- `/docs:generate` - Generate API documentation
- `/docs:readme` - Update README
- `/docs:changelog` - Generate changelog

### AI Enhancement (`/ai:`)
- `/ai:context` - Load full project context
- `/ai:refactor` - Intelligent refactoring
- `/ai:explain` - Explain complex code

## Hooks System

### Automatic Workflows

Hooks run automatically at specific points in your workflow:

**session-start** → Displays project context and git status
**user-prompt-submit** → Enhances prompts with context
**pre-tool-use** → Blocks dangerous operations
**post-tool-use** → Auto-formats and lints code
**stop** → Validates completion and sends notifications

### Security Features

The `pre-tool-use` hook protects against:
- Dangerous bash commands (`rm -rf /`, `sudo rm`, etc.)
- Modifications to sensitive files (.env, credentials, keys)
- Writes to system directories
- All security events are logged

### Quality Automation

The `post-tool-use` hook automatically:
- Formats code (Prettier, Black, rustfmt, etc.)
- Runs linters (ESLint, pylint, clippy, etc.)
- Suggests improvements
- Logs all quality checks

## GitHub Actions Integration

### PR Review Workflow
Automatically reviews pull requests for:
- Code quality issues
- Security vulnerabilities
- Performance problems
- Best practice violations

Trigger: Opening/updating PR or commenting `@claude`

### Issue Handler Workflow
Automatically generates implementation plans for issues:
- Analyzes requirements
- Suggests technical approach
- Creates feature branches
- Provides step-by-step plan

Trigger: Labeling issue with `claude` or commenting `@claude`

### Documentation Update Workflow
Keeps documentation in sync with code:
- Weekly automatic updates
- Updates API docs
- Refreshes README examples
- Generates changelog entries

Trigger: Weekly schedule or manual dispatch

## MCP Server Configuration

Recommended MCP servers to enhance Claude Code:

### Essential Servers
- **GitHub MCP** - PR and issue management
- **Sequential Thinking** - Complex problem breakdown
- **Filesystem MCP** - Enhanced file operations

### Optional Servers
- **Context7** - Library documentation access
- **Postgres MCP** - Database queries
- **Puppeteer MCP** - Web automation

See [docs/MCP_SERVERS.md](docs/MCP_SERVERS.md) for setup instructions.

## Configuration

### Project Settings (`.claude/settings.json`)
```json
{
  "hooks": {
    "sessionStart": { "enabled": true },
    "userPromptSubmit": { "enabled": true },
    "preToolUse": { "enabled": true },
    "postToolUse": { "enabled": true }
  },
  "permissions": {
    "bash": "ask",
    "write": "ask",
    "edit": "auto"
  }
}
```

### User Settings (`~/.claude.json`)
MCP server configuration (keeps API keys private):
```json
{
  "mcpServers": {
    "github": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_TOKEN": "your_token" }
    }
  }
}
```

## Language Support

This boilerplate automatically adapts to your project:

| Language | Auto-Detected | Formatter | Linter | Test Runner |
|----------|--------------|-----------|--------|-------------|
| JavaScript/TypeScript | ✅ | Prettier | ESLint | Jest/Vitest |
| Python | ✅ | Black | Pylint/Flake8 | pytest |
| Rust | ✅ | rustfmt | Clippy | cargo test |
| Go | ✅ | gofmt | golint | go test |
| Java | ✅ | google-java-format | Checkstyle | JUnit |
| Ruby | ✅ | RuboCop | RuboCop | RSpec |
| PHP | ✅ | PHP-CS-Fixer | PHPCS | PHPUnit |
| C/C++ | ✅ | clang-format | clang-tidy | GTest |

## Best Practices

### Before Coding
1. Run `/dev:setup` to ensure dependencies are installed
2. Review `CLAUDE.md` for project conventions
3. Create feature branch with `/git:branch`

### During Development
1. Let hooks handle formatting and linting
2. Use `/quality:review` for code review
3. Run `/quality:test` after changes

### Before Committing
1. Run `/quality:review` for final check
2. Ensure all tests pass with `/quality:test`
3. Use `/git:commit` for conventional commits
4. Create PR with `/git:pr`

## Documentation

- [Setup Guide](docs/SETUP.md) - Detailed installation and configuration
- [Hooks Reference](docs/HOOKS.md) - Complete hooks documentation
- [Commands Guide](docs/COMMANDS.md) - All slash commands explained
- [MCP Servers](docs/MCP_SERVERS.md) - MCP integration guide

## Customization

### Adding Custom Commands
Create `.claude/commands/custom/mycommand.md`:
```markdown
---
description: My custom command
---

# My Custom Command

Instructions for Claude to execute this command...
```

Usage: `/custom:mycommand`

### Adding Custom Hooks
Create `.claude/hooks/custom-hook.py` and register in `settings.json`

### Extending Skills
Add new skills in `.claude/skills/[skill-name]/SKILL.md`

## Troubleshooting

### Hooks Not Running
1. Ensure hooks are executable: `chmod +x .claude/hooks/*.py`
2. Check Python is installed: `python3 --version`
3. Verify settings.json configuration

### Commands Not Found
1. Restart Claude Code to reload commands
2. Check file names match command structure
3. Verify markdown frontmatter is correct

### GitHub Actions Failing
1. Add `ANTHROPIC_API_KEY` to repository secrets
2. Verify `GITHUB_TOKEN` has correct permissions
3. Check workflow file syntax

See [docs/SETUP.md#troubleshooting](docs/SETUP.md#troubleshooting) for more help.

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

- Built on [Claude Code](https://claude.ai/code) by Anthropic
- Inspired by the Claude Code community
- Incorporates 2025 best practices
- Based on research from official Claude Code documentation

## Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/claude-starter/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/claude-starter/discussions)
- **Documentation**: [docs/](docs/)

---

**Made with Claude Code** | **Star this repo if it helps you!**
