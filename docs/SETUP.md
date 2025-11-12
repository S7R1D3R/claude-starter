# Setup Guide

Complete installation and configuration guide for Claude Code Starter Boilerplate.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Detailed Installation](#detailed-installation)
- [Configuration](#configuration)
- [GitHub Actions Setup](#github-actions-setup)
- [MCP Servers Setup](#mcp-servers-setup)
- [Language-Specific Setup](#language-specific-setup)
- [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Required

- **Claude Code CLI** (2025 version with hooks support)
- **Git** (2.28 or later recommended)
- **Python 3.7+** (for hooks)

### Optional (Based on Your Stack)

- **Node.js 16+** & npm/yarn/pnpm (for JavaScript/TypeScript projects)
- **Python 3.8+** & pip (for Python projects)
- **Rust** & Cargo (for Rust projects)
- **Go 1.19+** (for Go projects)
- **Java 11+** & Maven/Gradle (for Java projects)

---

## Quick Start

```bash
# 1. Clone or initialize your project with this boilerplate
git clone <your-repo-url>
cd your-project

# 2. Run the setup wizard (auto-detects your stack)
./scripts/setup-wizard.sh

# 3. Install your project dependencies
# The wizard will suggest the right command, e.g.:
npm install          # Node.js
pip install -r requirements.txt  # Python
cargo build         # Rust
go mod download     # Go

# 4. Verify Claude Code configuration
ls -la .claude/

# 5. Start Claude Code session
claude-code
```

---

## Detailed Installation

### Step 1: Install Claude Code CLI

**macOS (Homebrew):**
```bash
brew install anthropic/tap/claude-code
```

**Linux:**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Verify installation:**
```bash
claude-code --version
```

### Step 2: Clone Boilerplate

**Option A: Start a new project**
```bash
git clone https://github.com/your-org/claude-starter.git my-project
cd my-project
rm -rf .git  # Remove boilerplate git history
git init     # Initialize your own repository
```

**Option B: Add to existing project**
```bash
cd your-existing-project
curl -fsSL https://raw.githubusercontent.com/your-org/claude-starter/main/scripts/setup-wizard.sh | bash
```

### Step 3: Review Configuration

```bash
# Check hooks are present
ls .claude/hooks/

# Check slash commands
ls .claude/commands/

# Review settings
cat .claude/settings.json
```

### Step 4: Install Python Dependencies (for hooks)

Hooks use standard library only, but verify Python is available:

```bash
python3 --version  # Should be 3.7+
```

### Step 5: Install Language-Specific Tools

Based on your project, install formatters and linters:

**JavaScript/TypeScript:**
```bash
npm install -D prettier eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin
```

**Python:**
```bash
pip install black pylint mypy
```

**Rust:**
```bash
rustup component add rustfmt clippy
```

**Go:**
```bash
go install golang.org/x/tools/cmd/goimports@latest
go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest
```

---

## Configuration

### Local Settings Override

Create `.claude/settings.local.json` to override defaults:

```json
{
  "hooks": {
    "sessionStart": {
      "enabled": true,
      "custom": {
        "showGitStatus": true,
        "showRecentCommits": 5
      }
    },
    "notification": {
      "enabled": true  // Enable desktop notifications
    }
  },
  "permissions": {
    "bash": "auto",    // Auto-approve bash commands (use with caution)
    "write": "ask"     // Always ask before writing files
  }
}
```

**Note:** `.claude/settings.local.json` is gitignored and won't be committed.

### Hook Configuration

Edit `.claude/settings.json` to enable/disable hooks:

```json
{
  "hooks": {
    "sessionStart": { "enabled": true },
    "userPromptSubmit": { "enabled": true },
    "preToolUse": {
      "enabled": true,
      "matchers": { "toolName": ["Bash", "Write", "Edit"] }
    },
    "postToolUse": {
      "enabled": true,
      "matchers": { "toolName": ["Write", "Edit"] }
    },
    "stop": { "enabled": true },
    "notification": { "enabled": false }
  }
}
```

### Disable Specific Security Checks

If you need to disable certain security validations (not recommended):

Edit `.claude/hooks/pre-tool-use.py` and comment out specific patterns.

**WARNING:** Only do this if you fully understand the security implications.

---

## GitHub Actions Setup

The boilerplate includes 3 GitHub Actions workflows that require configuration.

### Required Repository Secrets

1. **Navigate to your GitHub repository**
2. **Go to Settings → Secrets and variables → Actions**
3. **Add the following secrets:**

| Secret Name | Description | How to Get |
|------------|-------------|------------|
| `ANTHROPIC_API_KEY` | Your Anthropic API key | Get from [console.anthropic.com](https://console.anthropic.com) |
| `GITHUB_TOKEN` | Auto-provided by GitHub | Already available, no action needed |

### Workflows Included

#### 1. **claude-pr-review.yml**
- **Trigger:** PR creation/update or `@claude` comment
- **Purpose:** AI-powered code review
- **Setup:** Just add `ANTHROPIC_API_KEY` secret

#### 2. **claude-issue-handler.yml**
- **Trigger:** Issue labeled with `claude` or `@claude` comment
- **Purpose:** Generate implementation plans
- **Setup:** Just add `ANTHROPIC_API_KEY` secret

#### 3. **claude-docs-update.yml**
- **Trigger:** Weekly schedule or manual dispatch
- **Purpose:** Auto-update documentation
- **Setup:** Enable workflow permissions in repo settings

### Enable Workflow Permissions

1. Go to **Settings → Actions → General**
2. Scroll to **Workflow permissions**
3. Select **Read and write permissions**
4. Check **Allow GitHub Actions to create and approve pull requests**
5. Click **Save**

---

## MCP Servers Setup

MCP (Model Context Protocol) servers extend Claude with additional capabilities.

### Recommended MCP Servers

See [MCP_SERVERS.md](MCP_SERVERS.md) for detailed setup instructions.

**Quick install:**

```bash
# GitHub MCP Server (for PR/issue management)
npm install -g @anthropic/mcp-server-github

# Filesystem MCP Server (for file operations)
npm install -g @anthropic/mcp-server-filesystem

# Sequential Thinking MCP Server (for complex reasoning)
npm install -g @anthropic/mcp-server-sequential-thinking
```

**Configure in Claude Code:**

Edit `~/.claude/config.json` or `.claude/settings.json`:

```json
{
  "mcpServers": {
    "github": {
      "command": "mcp-server-github",
      "env": {
        "GITHUB_TOKEN": "your_github_token_here"
      }
    }
  }
}
```

---

## Language-Specific Setup

### JavaScript/TypeScript

**1. Install dependencies:**
```bash
npm install
```

**2. Configure formatters:**
```bash
npm install -D prettier eslint
echo '{"semi": true, "singleQuote": true}' > .prettierrc
```

**3. Configure tests:**
```bash
npm install -D jest @types/jest
npx jest --init
```

### Python

**1. Create virtual environment:**
```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate     # Windows
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Configure formatters:**
```bash
pip install black pylint mypy
```

**4. Configure tests:**
```bash
pip install pytest pytest-cov
```

**5. Create pytest.ini:**
```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
```

### Rust

**1. Build project:**
```bash
cargo build
```

**2. Install components:**
```bash
rustup component add rustfmt clippy
```

**3. Run tests:**
```bash
cargo test
```

### Go

**1. Download dependencies:**
```bash
go mod download
```

**2. Install tools:**
```bash
go install golang.org/x/tools/cmd/goimports@latest
go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest
```

**3. Run tests:**
```bash
go test ./...
```

---

## Troubleshooting

### Common Issues

#### 1. Hooks Not Running

**Symptom:** No hook output when starting Claude Code session

**Solution:**
```bash
# Check hooks are executable
chmod +x .claude/hooks/*.py

# Check Python is available
python3 --version

# Check settings.json has hooks enabled
cat .claude/settings.json | grep -A 2 "sessionStart"

# Test hook manually
python3 .claude/hooks/session-start.py '{"type": "sessionStart"}'
```

#### 2. Security Blocks Everything

**Symptom:** pre-tool-use hook blocks legitimate commands

**Solution:**
```bash
# Check security logs
cat .claude/logs/security.log

# Temporarily disable pre-tool-use hook
# Edit .claude/settings.json and set:
# "preToolUse": { "enabled": false }

# Or modify the dangerous_patterns list in pre-tool-use.py
```

#### 3. Formatters Not Running

**Symptom:** post-tool-use hook doesn't format code

**Solution:**
```bash
# Check formatter is installed
which black    # Python
which prettier # JavaScript
which rustfmt  # Rust

# Install missing formatter
pip install black
npm install -g prettier

# Check logs
cat .claude/logs/quality.log
```

#### 4. Session-Start Hook Slow

**Symptom:** Claude Code takes long to start

**Solution:**
```bash
# Optimize language detection in session-start.py
# The hook scans all files - can be slow on large projects

# Option 1: Disable session-start hook temporarily
# Edit .claude/settings.json:
# "sessionStart": { "enabled": false }

# Option 2: Use the optimized version (coming soon)
# Will cache results and skip node_modules/
```

#### 5. GitHub Actions Not Working

**Symptom:** Workflows fail with authentication errors

**Solution:**
```bash
# Check secrets are set
# Go to GitHub repo → Settings → Secrets and variables → Actions
# Verify ANTHROPIC_API_KEY is present

# Check workflow permissions
# Go to Settings → Actions → General → Workflow permissions
# Must be "Read and write permissions"

# Check workflow logs
# Go to Actions tab → Select failed workflow → View logs
```

#### 6. MCP Server Connection Failed

**Symptom:** Claude can't connect to MCP servers

**Solution:**
```bash
# Check MCP server is installed
which mcp-server-github

# Check configuration
cat ~/.claude/config.json

# Test MCP server manually
mcp-server-github --help

# Check environment variables
echo $GITHUB_TOKEN
```

#### 7. Python Version Issues

**Symptom:** Hooks fail with syntax errors

**Solution:**
```bash
# Check Python version (needs 3.7+)
python3 --version

# If too old, install newer version:
# macOS
brew install python@3.11

# Linux (Ubuntu)
sudo apt update
sudo apt install python3.11

# Update shebang in hooks if needed
sed -i '1s/.*/#!/usr/bin/env python3.11/' .claude/hooks/*.py
```

#### 8. Slash Commands Not Found

**Symptom:** `/dev:setup` says command not found

**Solution:**
```bash
# Check commands directory exists
ls .claude/commands/

# Check frontmatter format in command files
head -n 5 .claude/commands/dev/setup.md

# Should have:
# ---
# description: "Install dependencies"
# ---

# Restart Claude Code session
```

### Getting Help

If you encounter issues not covered here:

1. **Check logs:** `.claude/logs/` directory contains detailed logs
2. **Search issues:** Check the GitHub repository issues
3. **Create issue:** Open a new issue with:
   - Claude Code version (`claude-code --version`)
   - Operating system
   - Error messages from logs
   - Steps to reproduce

---

## Advanced Configuration

### Custom Hook Development

See [HOOKS.md](HOOKS.md) for detailed hook development guide.

### Custom Slash Commands

Create new commands in `.claude/commands/`:

```markdown
---
description: "Your command description"
---

# Your Command Name

Detailed instructions for Claude to follow...
```

### Pre-commit Hooks Integration

If you have `.pre-commit-config.yaml`:

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files  # Test
```

### Performance Tuning

For large projects:

1. **Disable session-start hook** or optimize language detection
2. **Use .claudeignore** to exclude large directories
3. **Cache formatter availability checks** in post-tool-use hook
4. **Disable notification hook** unless needed

---

## Security Best Practices

1. **Never commit secrets** - Use `.env` files (gitignored)
2. **Review hook security** - Understand what pre-tool-use blocks
3. **Use permissions wisely** - Set `bash: "ask"` for safety
4. **Audit security logs** - Check `.claude/logs/security.log` regularly
5. **Keep API keys secure** - Use GitHub Secrets for workflows

---

## Next Steps

After setup:

1. Read [CLAUDE.md](../CLAUDE.md) - Project instructions for Claude
2. Review [HOOKS.md](HOOKS.md) - Understand hook behavior
3. Check [COMMANDS.md](COMMANDS.md) - Learn all slash commands
4. Explore [SKILLS.md](SKILLS.md) - Understand Skills system
5. See [MCP_SERVERS.md](MCP_SERVERS.md) - Configure MCP servers

---

## Version Information

- **Boilerplate Version:** 1.0.0
- **Claude Code Version Required:** 2025.1 or later
- **Last Updated:** 2025-11-11
