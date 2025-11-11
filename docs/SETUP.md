# Setup Guide

Complete installation and configuration guide for the Claude Code Starter Boilerplate.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Verification](#verification)
5. [Language-Specific Setup](#language-specific-setup)
6. [Troubleshooting](#troubleshooting)
7. [Next Steps](#next-steps)

---

## Prerequisites

### Required Software

Before starting, ensure you have the following installed:

#### Claude Code
```bash
# Install Claude Code CLI
npm install -g @anthropic-ai/claude-code

# Or use npx (no installation required)
npx @anthropic-ai/claude-code
```

**Get API Key**: https://console.anthropic.com/settings/keys

#### Git
```bash
# Verify git is installed
git --version

# If not installed:
# Ubuntu/Debian
sudo apt-get install git

# macOS
brew install git

# Windows
# Download from https://git-scm.com/download/win
```

#### Language Runtimes (Install Based on Your Project)

**Node.js** (for JavaScript/TypeScript projects):
```bash
# Verify installation
node --version
npm --version

# Install via nvm (recommended)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install --lts
```

**Python** (for Python projects):
```bash
# Verify installation
python --version  # or python3 --version
pip --version

# Install Python 3.10+
# Ubuntu/Debian
sudo apt-get install python3 python3-pip

# macOS
brew install python@3.10
```

**Rust** (for Rust projects):
```bash
# Verify installation
rustc --version
cargo --version

# Install via rustup
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

**Go** (for Go projects):
```bash
# Verify installation
go version

# Install (download from https://go.dev/dl/)
# Or use package manager:
brew install go  # macOS
```

---

## Installation

### Step 1: Clone or Use This Boilerplate

#### Option A: Start New Project
```bash
# Clone this repository
git clone https://github.com/yourusername/claude-starter.git my-project
cd my-project

# Remove existing git history
rm -rf .git

# Initialize new repository
git init
git add .
git commit -m "Initial commit from Claude Code starter"
```

#### Option B: Add to Existing Project
```bash
# Navigate to your existing project
cd your-existing-project

# Download boilerplate files
curl -L https://github.com/yourusername/claude-starter/archive/main.zip -o claude-starter.zip
unzip claude-starter.zip

# Copy .claude directory and configuration files
cp -r claude-starter-main/.claude .
cp claude-starter-main/CLAUDE.md .
cp claude-starter-main/.gitignore .  # Merge with existing if needed

# Clean up
rm -rf claude-starter-main claude-starter.zip
```

### Step 2: Install Project Dependencies

Use the automated setup command:
```bash
# Using Claude Code
claude /dev:setup

# Or manually based on your project type:
npm install           # Node.js
pip install -r requirements.txt  # Python
cargo build          # Rust
go mod download      # Go
bundle install       # Ruby
composer install     # PHP
mvn install          # Java/Maven
```

### Step 3: Configure Claude Code

#### Set Up API Key

**Option A: Environment Variable**
```bash
# Add to ~/.bashrc or ~/.zshrc
export ANTHROPIC_API_KEY="sk-ant-..."

# Reload shell
source ~/.bashrc  # or source ~/.zshrc
```

**Option B: Claude Configuration File**
```bash
# Create or edit ~/.claude.json
{
  "apiKey": "sk-ant-...",
  "defaultModel": "claude-sonnet-4-5-20250929"
}
```

#### Configure Project Settings

Edit `.claude/settings.json` in your project:
```json
{
  "hooks": {
    "session-start": ".claude/hooks/session-start.py",
    "user-prompt-submit": ".claude/hooks/user-prompt-submit.py",
    "pre-tool-use": ".claude/hooks/pre-tool-use.py",
    "post-tool-use": ".claude/hooks/post-tool-use.py",
    "stop": ".claude/hooks/stop.py"
  },
  "commands": {
    "directory": ".claude/commands"
  }
}
```

**Note**: The boilerplate includes `.claude/settings.json` with defaults. For local customization, create `.claude/settings.local.json` (gitignored).

### Step 4: Make Hooks Executable

```bash
# Grant execute permissions to all hook scripts
chmod +x .claude/hooks/*.py
chmod +x .claude/hooks/*.sh

# Verify permissions
ls -l .claude/hooks/
```

### Step 5: Install Hook Dependencies (if needed)

Some hooks may require additional Python packages:
```bash
# Install Python dependencies for hooks
pip install python-dotenv requests

# Or create a requirements file for hooks
cat > .claude/requirements.txt << EOF
python-dotenv>=1.0.0
requests>=2.31.0
EOF

pip install -r .claude/requirements.txt
```

---

## Configuration

### Project Customization

#### Update CLAUDE.md

Edit `CLAUDE.md` in your project root to add project-specific instructions:

```markdown
## Project-Specific Notes

### Architecture
- Using microservices pattern
- API gateway on port 3000
- Database: PostgreSQL 14

### Development Conventions
- Branch naming: feature/*, bugfix/*, hotfix/*
- Commit messages: Use conventional commits
- Code style: Prettier with custom config

### Environment Variables Required
- DATABASE_URL
- API_KEY
- REDIS_URL
```

#### Configure Git Hooks (Optional)

If using pre-commit hooks:
```bash
# Install pre-commit
pip install pre-commit

# Install git hooks
pre-commit install

# Test hooks
pre-commit run --all-files
```

#### Set Up Environment Variables

Create `.env` file (never commit this):
```bash
# Copy example environment file
cp .env.example .env

# Edit with your values
nano .env
```

Example `.env`:
```
# Application
NODE_ENV=development
PORT=3000

# Database
DATABASE_URL=postgresql://localhost/mydb

# API Keys (use MCP servers for these)
# GITHUB_TOKEN=  # Configured in ~/.claude.json MCP servers
# ANTHROPIC_API_KEY=  # Configured globally
```

---

## Verification

### Test Claude Code Setup

```bash
# Start Claude Code in your project
claude

# In Claude Code, test basic commands:
> /dev:setup
> /quality:test
> /quality:lint
```

### Verify Hooks Are Working

**Test Session Start Hook**:
```bash
# Start new Claude Code session
claude

# You should see:
# ╔══════════════════════════════════════════════════════════════╗
# ║         Claude Code Session Started                          ║
# ╚══════════════════════════════════════════════════════════════╝
```

**Test Security Hook**:
```bash
# In Claude Code, try a dangerous command:
> Run: rm -rf /

# You should see:
# 🛡️  SECURITY BLOCK: Attempting to recursively delete from root directory
```

**Test Prompt Enhancement**:
```bash
# Type a vague request
> fix the bug

# The hook will enhance it with context:
# "fix the bug in [detected file] following [coding standards]"
```

### Verify Commands

Test all slash commands:
```bash
# Development commands
/dev:init
/dev:setup
/dev:build
/dev:serve
/dev:clean

# Git commands
/git:branch feature/test
/git:commit
/git:sync
/git:pr

# Quality commands
/quality:review
/quality:test
/quality:lint
/quality:format
/quality:security

# Documentation commands
/docs:generate
/docs:readme
/docs:changelog

# AI commands
/ai:context
/ai:refactor
/ai:explain
```

---

## Language-Specific Setup

### Node.js / TypeScript

```bash
# Install dependencies
npm install

# Install dev dependencies
npm install -D eslint prettier typescript @types/node

# Setup TypeScript
npx tsc --init

# Add scripts to package.json
{
  "scripts": {
    "dev": "nodemon src/index.ts",
    "build": "tsc",
    "test": "jest",
    "lint": "eslint src/**/*.ts",
    "format": "prettier --write src/**/*.ts"
  }
}
```

### Python

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development tools
pip install black pylint pytest mypy

# Setup pre-commit (optional)
pre-commit install
```

### Rust

```bash
# Build project
cargo build

# Install development tools
rustup component add clippy rustfmt

# Setup cargo-watch for auto-rebuild
cargo install cargo-watch

# Add to .cargo/config.toml
[alias]
dev = "watch -x run"
```

### Go

```bash
# Download dependencies
go mod download

# Install development tools
go install golang.org/x/tools/gopls@latest
go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest

# Setup .air.toml for hot reload (optional)
curl -sSfL https://raw.githubusercontent.com/cosmtrek/air/master/install.sh | sh -s
air init
```

---

## Troubleshooting

### Common Issues

#### Issue: "Hook failed with exit code 127"

**Cause**: Hook script not executable or shebang missing

**Solution**:
```bash
# Make hooks executable
chmod +x .claude/hooks/*.py

# Verify Python is available
which python3

# Check shebang in hooks
head -n 1 .claude/hooks/session-start.py
# Should be: #!/usr/bin/env python3
```

#### Issue: "Command not found: /dev:setup"

**Cause**: Commands directory not configured

**Solution**:
```bash
# Verify settings.json
cat .claude/settings.json

# Ensure commands directory is set:
{
  "commands": {
    "directory": ".claude/commands"
  }
}
```

#### Issue: "ANTHROPIC_API_KEY not set"

**Cause**: API key not configured

**Solution**:
```bash
# Set environment variable
export ANTHROPIC_API_KEY="sk-ant-..."

# Or add to ~/.claude.json
echo '{"apiKey": "sk-ant-..."}' > ~/.claude.json
```

#### Issue: "git: command not found"

**Cause**: Git not installed

**Solution**:
```bash
# Install git
# Ubuntu/Debian
sudo apt-get install git

# macOS
brew install git

# Verify
git --version
```

#### Issue: "Permission denied" errors

**Cause**: Insufficient permissions

**Solution**:
```bash
# Fix hook permissions
chmod +x .claude/hooks/*.py
chmod +x .claude/hooks/*.sh

# Check file ownership
ls -la .claude/hooks/

# Fix ownership if needed
sudo chown -R $USER:$USER .claude/
```

#### Issue: Hooks not running

**Cause**: Hooks not enabled or path incorrect

**Solution**:
```bash
# Check settings.json
cat .claude/settings.json

# Verify hook files exist
ls -la .claude/hooks/

# Test hook manually
python3 .claude/hooks/session-start.py

# Enable verbose logging
export CLAUDE_DEBUG=1
claude
```

---

## Next Steps

### 1. Configure MCP Servers

See [MCP_SERVERS.md](MCP_SERVERS.md) for detailed setup.

Quick start:
```bash
# Edit ~/.claude.json
{
  "mcpServers": {
    "github": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token"
      }
    }
  }
}
```

### 2. Explore Slash Commands

See [COMMANDS.md](COMMANDS.md) for complete reference.

Try essential commands:
- `/dev:setup` - Install dependencies
- `/quality:test` - Run tests
- `/quality:review` - Code review
- `/git:commit` - Create commit

### 3. Understand Hooks

See [HOOKS.md](HOOKS.md) for detailed documentation.

Key hooks:
- **session-start**: Loads project context
- **pre-tool-use**: Security validation
- **post-tool-use**: Auto-formatting
- **stop**: Final validation

### 4. Customize for Your Project

1. Update `CLAUDE.md` with project-specific instructions
2. Add custom slash commands in `.claude/commands/`
3. Modify hooks to fit your workflow
4. Configure linters and formatters

### 5. Set Up CI/CD

Example GitHub Actions workflow (`.github/workflows/ci.yml`):
```yaml
name: CI
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm ci
      - run: npm test
      - run: npm run lint
```

---

## Additional Resources

- **Claude Code Documentation**: https://docs.claude.com/claude-code
- **MCP Protocol**: https://modelcontextprotocol.io
- **Hooks Guide**: [HOOKS.md](HOOKS.md)
- **Commands Reference**: [COMMANDS.md](COMMANDS.md)
- **MCP Setup**: [MCP_SERVERS.md](MCP_SERVERS.md)

---

## Getting Help

If you encounter issues:

1. **Check logs**:
   ```bash
   tail -f .claude/logs/security.log
   tail -f .claude/logs/hooks.log
   ```

2. **Enable debug mode**:
   ```bash
   export CLAUDE_DEBUG=1
   claude
   ```

3. **Verify configuration**:
   ```bash
   claude --check-config
   ```

4. **Community support**:
   - GitHub Issues: https://github.com/anthropics/claude-code/issues
   - Discord: https://discord.gg/anthropic
   - Documentation: https://docs.claude.com

---

**Ready to start coding!** 🚀

Run `/dev:setup` in Claude Code to begin.
