# Setup Wizard Guide

Complete guide to the Claude Code Starter automated setup wizards.

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Wizard Options](#wizard-options)
- [Basic Wizard](#basic-wizard)
- [AI-Powered Wizard](#ai-powered-wizard)
- [What Gets Configured](#what-gets-configured)
- [Installation Options](#installation-options)
- [Troubleshooting](#troubleshooting)
- [Advanced Usage](#advanced-usage)

---

## Overview

The Claude Code Starter boilerplate includes **three setup wizards** to help you configure your development environment:

1. **Shell Wizard** (`setup-wizard.sh`) - Fast bash script for basic setup
2. **Basic Python Wizard** (`setup-agent.py`) - Interactive Python wizard with auto-detection
3. **AI-Powered Wizard** (`setup-agent.py --ai`) - Intelligent wizard using Claude Agent SDK

Choose the wizard that best fits your needs and environment.

---

## Quick Start

### Option 1: Shell Wizard (Fastest)

```bash
./scripts/setup-wizard.sh
```

**Best for:** Quick setup, CI/CD environments, minimal dependencies

### Option 2: Basic Python Wizard (Recommended)

```bash
python scripts/setup-agent.py
```

**Best for:** Interactive setup with intelligent project detection

### Option 3: AI-Powered Wizard (Most Advanced)

```bash
# Install Claude Agent SDK first
pip install claude-agent-sdk

# Run AI wizard
python scripts/setup-agent.py --ai
```

**Best for:** Personalized recommendations and intelligent configuration

---

## Wizard Options

### Comparison Table

| Feature | Shell Wizard | Basic Python Wizard | AI-Powered Wizard |
|---------|-------------|-------------------|------------------|
| **Speed** | ⚡⚡⚡ Instant | ⚡⚡ Fast | ⚡ Moderate |
| **Project Detection** | Basic | Advanced | Intelligent |
| **Interactivity** | None | Prompts | Conversational |
| **Recommendations** | Generic | Specific | Personalized |
| **Dependencies** | Bash, Python | Python 3.10+ | Python 3.10+, SDK, API key |
| **Offline Support** | ✅ Yes | ✅ Yes | ❌ No (requires API) |
| **Intelligence** | Rule-based | Detection-based | AI-powered |

---

## Basic Wizard

### Features

The Basic Python Wizard (`setup-agent.py`) provides:

- **Automatic project detection** - Analyzes your codebase to detect:
  - Programming languages (JavaScript, Python, Rust, Go, etc.)
  - Package managers (npm, pip, cargo, go mod, maven, etc.)
  - Frameworks (React, Vue, Django, FastAPI, etc.)
  - Existing tools (ESLint, Prettier, Jest, Pytest, etc.)

- **Interactive configuration** - Asks about:
  - Hook preferences (session-start, pre-tool-use, post-tool-use, etc.)
  - MCP server setup
  - GitHub Actions enablement
  - RAG integration
  - Skills system preferences

- **Automated installation** - Handles:
  - Git initialization
  - Hook permissions
  - Directory creation
  - Dependency installation (based on detected package managers)
  - MCP server configuration

- **Validation** - Tests:
  - Hook execution
  - Python availability
  - Git configuration
  - MCP server connectivity

- **Recommendations** - Provides:
  - Language-specific tips
  - Productivity recommendations
  - Tool suggestions

### Usage

```bash
# Run basic wizard
python scripts/setup-agent.py

# Or with explicit mode
python scripts/setup-agent.py --help
```

### Configuration Flow

```
┌─────────────────────────────────────┐
│  Phase 1: Project Discovery         │
│  • Detect languages                 │
│  • Find package managers            │
│  • Identify frameworks              │
│  • Check existing tools             │
└─────────────────────────────────────┘
            ↓
┌─────────────────────────────────────┐
│  Phase 2: Interactive Configuration │
│  • Hook settings                    │
│  • Slash commands                   │
│  • MCP servers                      │
│  • GitHub Actions                   │
│  • RAG integration                  │
└─────────────────────────────────────┘
            ↓
┌─────────────────────────────────────┐
│  Phase 3: Installation              │
│  • Initialize Git                   │
│  • Set permissions                  │
│  • Install dependencies             │
│  • Configure MCP                    │
│  • Setup GitHub Actions             │
└─────────────────────────────────────┘
            ↓
┌─────────────────────────────────────┐
│  Phase 4: Validation                │
│  • Test hooks                       │
│  • Verify tools                     │
│  • Check MCP servers                │
└─────────────────────────────────────┘
            ↓
┌─────────────────────────────────────┐
│  Phase 5: Recommendations           │
│  • Language-specific tips           │
│  • Productivity suggestions         │
│  • Advanced features                │
└─────────────────────────────────────┘
```

---

## AI-Powered Wizard

### Overview

The AI-Powered Wizard uses the **Claude Agent SDK** to provide an intelligent, conversational setup experience.

### Prerequisites

1. **Python 3.10+**
2. **Claude Agent SDK**
   ```bash
   pip install claude-agent-sdk
   ```
3. **Anthropic API Key**
   ```bash
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```

### Features

#### Intelligent Analysis

Claude analyzes your project and provides:
- **Project type identification** - Understands what you're building
- **Framework detection** - Recognizes patterns and best practices
- **Tool recommendations** - Suggests relevant MCP servers and hooks
- **Configuration optimization** - Tailors settings to your workflow

#### Natural Conversation

Instead of rigid prompts, have a conversation:
```
Wizard: I notice you're building a React application with TypeScript.
        Would you like me to configure ESLint and Prettier?

You: Yes, and also set up Jest for testing

Wizard: Great! I'll also recommend the GitHub MCP server for PR
        management. This will enable Claude to help with code reviews.
```

#### Personalized Recommendations

Based on your project, Claude suggests:
- Optimal hook configurations
- Useful MCP servers
- Productivity workflows
- Security best practices
- Testing strategies

### Usage

```bash
# Set API key
export ANTHROPIC_API_KEY="sk-ant-..."

# Run AI wizard
python scripts/setup-agent.py --ai
```

### Example Session

```
╔══════════════════════════════════════════════════════════════╗
║   Claude Code Starter - AI-Powered Setup Wizard             ║
║   Using Claude Agent SDK for Intelligent Configuration      ║
╚══════════════════════════════════════════════════════════════╝

🔍 Gathering project context...
✅ Context gathered: 47 files analyzed

🤖 Claude is analyzing your project...

Claude's Analysis:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Based on your project structure, I can see this is a TypeScript/Node.js
project with React. Here's what I recommend:

1. Project Type: React web application with TypeScript
2. Detected: npm, ESLint, Prettier, Jest
3. Recommended Features:
   • Enable all hooks for code quality enforcement
   • Setup GitHub MCP server for PR management
   • Configure session-start hook for git context
   • Enable post-tool-use hook for auto-formatting

4. MCP Servers to Install:
   • @anthropic-ai/mcp-server-github - PR and issue management
   • @anthropic-ai/mcp-server-sequential-thinking - Complex problems

5. Specific Recommendations:
   • Add pre-commit hooks for ESLint and Prettier
   • Enable strict TypeScript checking
   • Configure Jest with coverage reporting
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 Executing setup based on recommendations...
   • Making hooks executable
   • Creating .claude/logs directory
   • Configuring settings.json
   • Installing project dependencies
   • Configuring MCP servers

✅ Setup executed successfully

💡 Getting personalized recommendations...

Recommendations:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
For your React TypeScript project, here are specific productivity tips:

1. Use `/quality:review` before each commit to catch potential issues
   early. This is especially important for TypeScript projects.

2. Enable `post-tool-use` hook to auto-format with Prettier after
   every file edit. This keeps your code style consistent.

3. Use `/ai:refactor` when working with complex component logic.
   Claude can suggest React best practices and performance optimizations.

4. Leverage the GitHub MCP server with `/git:pr` to generate
   comprehensive PR descriptions that highlight component changes.

5. For complex state management, use `/ai:explain` to understand
   existing patterns before making changes.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ Intelligent setup complete!
```

---

## What Gets Configured

### Directory Structure

```
project-root/
├── .claude/
│   ├── hooks/              # Executable hook scripts
│   ├── commands/           # Slash command definitions
│   ├── skills/             # Skills modules
│   ├── settings.json       # Main configuration
│   └── logs/               # Hook and security logs
├── .github/
│   └── workflows/          # GitHub Actions (if enabled)
└── scripts/
    └── wizard/             # Setup wizard code
```

### Configuration Files

#### `.claude/settings.json`

The wizard configures:
- Hook enablement and matchers
- Tool permissions
- Session preferences
- MCP server configuration

#### `.claude/settings.local.json` (optional)

User-specific overrides:
- Personal preferences
- Local API keys
- Custom hook behavior

### Installed Components

#### Hooks (if enabled)

- `session-start.py` - Load project context on startup
- `user-prompt-submit.py` - Enhance prompts with context
- `pre-tool-use.py` - Security validation before tool execution
- `post-tool-use.py` - Auto-format and test after edits
- `stop.py` - Final validation before session ends

#### Slash Commands

- `/dev:*` - Development commands (init, setup, build, serve, clean)
- `/git:*` - Git operations (commit, pr, sync, branch)
- `/quality:*` - Code quality (review, lint, format, test, security)
- `/docs:*` - Documentation (generate, readme, changelog)
- `/ai:*` - AI enhancement (context, refactor, explain)

#### Skills (if enabled)

Pre-installed skills from `.claude/skills/`:
- `code-review` - Comprehensive code review capabilities
- `testing` - Test generation and validation

---

## Installation Options

### Dependency Installation

The wizard can automatically install dependencies based on detected package managers:

#### JavaScript/TypeScript
```bash
npm install      # If package.json and package-lock.json exist
yarn install     # If yarn.lock exists
pnpm install     # If pnpm-lock.yaml exists
```

#### Python
```bash
pip install -r requirements.txt  # If requirements.txt exists
poetry install                    # If poetry.lock exists
```

#### Rust
```bash
cargo build
```

#### Go
```bash
go mod download
```

### MCP Server Installation

If MCP servers are enabled, the wizard can install:

```bash
# GitHub MCP Server
npm install -g @anthropic-ai/mcp-server-github

# Sequential Thinking MCP Server
npm install -g @anthropic-ai/mcp-server-sequential-thinking

# Filesystem MCP Server
npm install -g @anthropic-ai/mcp-server-filesystem
```

**Note:** You'll need to add API keys and configuration manually in `~/.claude/config.json` or `.claude/settings.json`.

---

## Troubleshooting

### Common Issues

#### 1. Python Version Too Old

**Error:**
```
SyntaxError: invalid syntax
```

**Solution:**
```bash
# Check version
python3 --version  # Should be 3.10+

# Install Python 3.10+ (Ubuntu example)
sudo apt update
sudo apt install python3.11

# Use specific version
python3.11 scripts/setup-agent.py
```

#### 2. Claude Agent SDK Not Found

**Error:**
```
❌ Claude Agent SDK not installed
```

**Solution:**
```bash
pip install claude-agent-sdk

# Or use basic wizard instead
python scripts/setup-agent.py
```

#### 3. Missing ANTHROPIC_API_KEY

**Error:**
```
Error: ANTHROPIC_API_KEY environment variable is required
```

**Solution:**
```bash
# Set API key
export ANTHROPIC_API_KEY="sk-ant-your-key-here"

# Or add to ~/.bashrc / ~/.zshrc
echo 'export ANTHROPIC_API_KEY="sk-ant-your-key-here"' >> ~/.bashrc
source ~/.bashrc
```

#### 4. Hooks Not Executable

**Error:**
```
Permission denied: .claude/hooks/session-start.py
```

**Solution:**
```bash
# Make hooks executable
chmod +x .claude/hooks/*.py

# Or run wizard again
./scripts/setup-wizard.sh
```

#### 5. MCP Server Installation Fails

**Error:**
```
npm ERR! 404 Not Found
```

**Solution:**
```bash
# Check npm registry
npm config get registry

# Install with explicit version
npm install -g @anthropic-ai/mcp-server-github@latest

# Or skip MCP setup and configure manually later
```

---

## Advanced Usage

### Customizing the Wizard

#### Extend Basic Wizard

Edit `scripts/wizard/setup_agent.py` to add custom detection:

```python
def _detect_custom_framework(self) -> bool:
    """Detect your custom framework"""
    return (self.project_root / "custom.config.js").exists()
```

#### Extend AI Wizard

Modify the prompts in `scripts/wizard/intelligent_setup_agent.py`:

```python
prompt = f"""
Analyze my project with these additional considerations:
- We use a monorepo structure
- We have custom deployment pipelines
- We prefer functional programming patterns

{json.dumps(self.project_context, indent=2)}
"""
```

### Running Programmatically

```python
from wizard.setup_agent import SetupWizardAgent
import asyncio

async def custom_setup():
    agent = SetupWizardAgent(project_root="/path/to/project")

    # Override configuration
    agent.config = {
        "hooks": {"enabled": True, "all": True},
        "mcp_servers": {"enabled": False},
        # ... custom config
    }

    # Run specific phases
    await agent.phase_discovery()
    await agent.phase_installation()

asyncio.run(custom_setup())
```

### Silent Mode (Non-Interactive)

For CI/CD or automated setups:

```bash
# Basic wizard will auto-accept defaults if stdin is not a TTY
./scripts/setup-wizard.sh < /dev/null

# Or use environment variables
export WIZARD_AUTO_CONFIRM=1
python scripts/setup-agent.py
```

### Logging and Debugging

Enable verbose logging:

```bash
# Set log level
export WIZARD_LOG_LEVEL=DEBUG

# Run wizard
python scripts/setup-agent.py

# Check logs
cat .claude/logs/setup.log
```

---

## Next Steps

After running the setup wizard:

1. **Review Configuration**
   ```bash
   cat .claude/settings.json
   ```

2. **Test Hooks**
   ```bash
   python .claude/hooks/session-start.py
   ```

3. **Try Slash Commands**
   - Start Claude Code
   - Run `/dev:setup` to verify installation
   - Try `/quality:test` if you have tests

4. **Customize Settings**
   - Create `.claude/settings.local.json` for personal preferences
   - Review `docs/HOOKS.md` for hook customization
   - See `docs/COMMANDS.md` for slash command options

5. **Explore Advanced Features**
   - Set up MCP servers (see `docs/MCP_SERVERS.md`)
   - Configure RAG integration (see `docs/RAG_INTEGRATION.md`)
   - Install additional Skills (see `docs/SKILLS.md`)

---

## Resources

- **Setup Guide:** `docs/SETUP.md` - Detailed manual setup instructions
- **Hooks Guide:** `docs/HOOKS.md` - Hook development and customization
- **Commands Guide:** `docs/COMMANDS.md` - Slash command reference
- **Skills Guide:** `docs/SKILLS.md` - Skills system documentation
- **MCP Guide:** `docs/MCP_SERVERS.md` - MCP server configuration

---

## Feedback

Found an issue with the setup wizard or have suggestions?

1. Check existing issues: [GitHub Issues](https://github.com/your-org/claude-starter/issues)
2. Open a new issue with:
   - Wizard type used (shell, basic, or AI)
   - Python version (`python3 --version`)
   - Error messages and logs
   - Operating system

---

**Happy coding with Claude! 🚀**
