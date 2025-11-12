# Setup Wizard Skill

An intelligent project setup assistant that automatically configures Claude Code for your development workflow.

## Overview

The Setup Wizard Skill provides:
- ✅ Automatic project detection (language, framework, tools)
- ✅ Intelligent configuration recommendations
- ✅ Interactive setup with sensible defaults
- ✅ Hooks, MCP servers, and GitHub Actions configuration
- ✅ Educational guidance for Claude Code features

## Installation

### Option 1: Copy to Claude Skills Directory

```bash
# Copy this skill to your Claude skills directory
cp -r .claude/skills/setup-wizard ~/.claude/skills/

# Or create a symlink for easier updates
ln -s "$(pwd)/.claude/skills/setup-wizard" ~/.claude/skills/setup-wizard
```

### Option 2: Use Installation Script

```bash
# From project root
.claude/skills/setup-wizard/install.sh
```

## Usage

### Auto-Invoked (Recommended)

The skill automatically activates when you say things like:
- "Set up this project"
- "Configure Claude Code for my app"
- "Help me get started with this codebase"
- "Initialize development environment"

### Manual Invocation via Slash Command

```bash
# Use the setup wizard slash command
/setup:wizard
```

## Features

### Project Detection

Automatically identifies:
- **Languages**: JavaScript, TypeScript, Python, Rust, Go, Java, C#, Ruby, PHP, and more
- **Frameworks**: React, Vue, Django, Flask, Spring, .NET, Rails, Laravel, etc.
- **Tools**: Package managers, test frameworks, linters, formatters, build tools

### Configuration Options

**Hooks** (recommended):
- Session start (project context loading)
- Prompt enhancement (auto-inject context)
- Security validation (block dangerous operations)
- Code quality automation (format, lint, test)
- Final validation (quality gates)

**MCP Servers**:
- Docker (container management)
- GitHub (issues, PRs, workflows)
- Archon RAG (knowledge base integration)
- Custom servers

**GitHub Actions**:
- Code quality checks
- Automated testing
- Security scanning
- Documentation generation

**RAG Integration**:
- Vector database for docs
- Automatic context retrieval
- Pattern recognition

### Smart Defaults

The wizard suggests optimal configurations based on:
- Project type (web app, library, CLI, microservice)
- Language ecosystem conventions
- Team vs. solo development
- Development stage (early vs. production)

## Example Sessions

### Quick Setup (Default Settings)

```
You: "Set up this project"

Wizard: "I've detected a TypeScript Next.js project with npm.

I recommend:
✓ All quality hooks
✓ Docker + GitHub MCP servers
✓ GitHub Actions for CI/CD

Use default settings? (yes/no)
```

You: "yes"

Wizard: [configures everything automatically]

"✅ Setup complete! Try:
- /quality:test to run tests
- /git:commit for structured commits
- /dev:serve to start the dev server"
```

### Custom Setup

```
You: "Configure Claude Code, but I only want basic hooks"

Wizard: "Got it! I'll set up minimal hooks for you.

Which hooks?
1. Session start (project context) - recommended
2. Security validation (safety checks) - recommended
3. Code quality automation - skip
4. Others - skip

Sound good?
```

You: "yes, and add Docker MCP"

Wizard: [configures selected features]

"✅ Configured:
- Session start hook
- Security validation hook
- Docker MCP server

MCP will require Docker Desktop. Want me to create setup instructions?"
```

## Configuration Files

The wizard manages these files:

```
.claude/
├── settings.json          # Main configuration (hooks, MCP, permissions)
├── hooks/                 # Hook scripts
│   ├── session-start.py
│   ├── user-prompt-submit.py
│   └── pre-tool-use.py
└── mcp/                   # MCP configurations
    ├── docker.json
    └── github.json

.github/workflows/         # GitHub Actions (if enabled)
    └── claude-quality.yml
```

## Troubleshooting

### Skill Not Activating

1. Verify installation:
   ```bash
   ls ~/.claude/skills/setup-wizard
   ```

2. Check skill.json syntax:
   ```bash
   cat ~/.claude/skills/setup-wizard/skill.json | python -m json.tool
   ```

3. Try manual slash command:
   ```bash
   /setup:wizard
   ```

### Configuration Errors

The wizard validates all changes before applying. If something fails:
- Error messages explain what went wrong
- Configurations are rolled back
- Alternative approaches are suggested

### MCP Server Issues

If MCP servers don't connect:
1. Check Docker Desktop is running (for Docker MCP)
2. Verify GitHub token is set (for GitHub MCP)
3. Check .claude/settings.json syntax
4. Restart Claude Code

### Hook Execution Failures

If hooks fail:
1. Check hook files are executable: `chmod +x .claude/hooks/*.py`
2. Verify Python is available: `python --version`
3. Check hook logs in Claude Code output
4. Temporarily disable problematic hooks in settings.json

## Advanced Usage

### Language-Specific Configurations

The wizard applies optimal settings for each language:

**TypeScript/JavaScript:**
- ESLint + Prettier
- Import sorting
- Unused code detection
- TypeScript strict mode

**Python:**
- Black + isort + mypy
- Virtual environment detection
- Type checking
- Dependency scanning

**Rust:**
- Clippy lints
- Rustfmt
- Cargo validation

**Go:**
- Gofmt + golint
- Go mod tidy
- Vet checks

### Custom Workflows

After setup, you can customize:

```json
// .claude/settings.json
{
  "hooks": {
    "sessionStart": {
      "command": ".claude/hooks/custom-start.sh",
      "enabled": true
    }
  }
}
```

### Team Setup

For team repositories:
1. Run wizard once to configure
2. Commit .claude/ to version control
3. Team members get automatic setup
4. Hooks enforce consistent quality

## Best Practices

✅ **Do:**
- Use default recommendations for new projects
- Enable all hooks for team projects
- Configure MCP servers for productivity
- Enable GitHub Actions for quality gates
- Customize after understanding defaults

❌ **Don't:**
- Disable security hooks without reason
- Skip validation steps
- Commit secrets to MCP configurations
- Override critical quality checks

## Integration with Other Tools

### With Slash Commands

After setup, use:
- `/dev:setup` - Install dependencies
- `/dev:build` - Build project
- `/quality:test` - Run tests
- `/quality:lint` - Lint code
- `/git:commit` - Create commits
- `/git:pr` - Create pull requests

### With Other Skills

Works alongside:
- Language-specific skills (TypeScript, Python, etc.)
- Testing skills (test generation, coverage)
- Security skills (vulnerability scanning)
- Documentation skills (API docs, README)

### With CI/CD

Wizard-configured GitHub Actions:
- Mirror local hook behavior
- Enforce quality on PRs
- Block merges on failures
- Generate reports

## Updates

To update the skill:

```bash
# If using symlink (recommended)
cd /path/to/claude-starter
git pull
# Skill automatically updated via symlink

# If copied
cd /path/to/claude-starter
git pull
cp -r .claude/skills/setup-wizard ~/.claude/skills/
```

## Support

- **Documentation**: See `/home/user/claude-starter/docs/SKILLS.md`
- **Examples**: Check `examples/` directory in project
- **Issues**: Report at project repository
- **Questions**: Ask Claude directly!

## Version

**Current Version**: 1.0.0

**Changelog**:
- 1.0.0: Initial release with full setup automation

## License

Same license as Claude Code Starter Boilerplate project.

---

**Pro Tip**: After setup, ask Claude questions like "Explain the hooks you configured" or "Show me how to use GitHub MCP" to learn more about your new setup!
