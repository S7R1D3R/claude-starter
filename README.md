# Claude Code Starter Boilerplate

A ready-to-use template that supercharges your development with AI automation, code quality tools, and intelligent workflows for any programming language.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-2025-purple)](https://claude.ai/code)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

## What is This?

This is a **starter template** that adds powerful AI capabilities to your coding projects. Think of it as a smart assistant that:
- Automatically checks your code quality
- Prevents security mistakes
- Formats and organizes your code
- Helps you write better commits and pull requests
- Works with **any programming language** (JavaScript, Python, Rust, Go, Java, etc.)

## How to Use This

### Step 1: Get the Template

**Option A: Start a new project**
```bash
git clone https://github.com/yourusername/claude-starter.git my-project
cd my-project
./scripts/setup-wizard.sh
```

**Option B: Add to an existing project**
```bash
# Copy the .claude folder to your existing project
cp -r /path/to/claude-starter/.claude /path/to/your-project/
cd /path/to/your-project
chmod +x .claude/hooks/*.py
```

### Step 2: Install Your Project Dependencies

The template auto-detects your language and suggests the right commands:

```bash
# Node.js / JavaScript / TypeScript
npm install

# Python
pip install -r requirements.txt

# Rust
cargo build

# Go
go mod download

# Or use the quick command:
# Just type in Claude Code: /dev:setup
```

### Step 3: Start Using Claude Code

Open Claude Code in your project:
```bash
claude-code
```

That's it! The template is now active and will automatically help you code better.

## What You Get

### Smart Slash Commands

Quick commands you can type to automate common tasks:

**Development:**
- `/dev:setup` - Install project dependencies
- `/dev:build` - Build your project
- `/dev:serve` - Start development server
- `/dev:clean` - Clean build files

**Git Workflows:**
- `/git:commit` - Create a well-formatted commit message
- `/git:pr` - Create a pull request with description
- `/git:branch` - Create a new feature branch
- `/git:sync` - Sync with remote repository

**Code Quality:**
- `/quality:test` - Run your test suite
- `/quality:lint` - Check code style
- `/quality:format` - Auto-format all code
- `/quality:review` - Get AI code review
- `/quality:security` - Scan for security issues

**Documentation:**
- `/docs:readme` - Update README
- `/docs:changelog` - Generate changelog
- `/docs:generate` - Create API docs

### Automatic Quality Checks

The template runs checks automatically as you code:

✅ **Security Validation** - Blocks dangerous commands before they run
✅ **Auto-Formatting** - Formats code after you write it
✅ **Smart Prompts** - Adds context to help Claude understand your project
✅ **Test Running** - Reminds you to test after changes

### GitHub Integration (Optional)

If you push to GitHub, you get:
- AI-powered code reviews on pull requests
- Automatic issue handling
- Documentation updates

*(Requires adding your `ANTHROPIC_API_KEY` to GitHub secrets)*

## Understanding the Template

### What's Inside?

```
your-project/
└── .claude/                    # All the magic lives here
    ├── commands/               # Slash commands (/dev:setup, /git:commit, etc.)
    ├── hooks/                  # Automation scripts (security, formatting, etc.)
    ├── skills/                 # AI expertise modules
    └── settings.json           # Configuration
```

### How It Works

1. **Hooks** run automatically when you code:
   - `session-start` - Shows project info when you start
   - `pre-tool-use` - Prevents dangerous commands
   - `post-tool-use` - Auto-formats your code
   - `stop` - Final checks before finishing

2. **Slash Commands** give you quick actions:
   - Type `/quality:test` instead of remembering test commands
   - Type `/git:commit` for well-formatted commits
   - Type `/dev:setup` to install dependencies

3. **Skills** add expert knowledge:
   - Code review expertise
   - Testing best practices
   - More coming soon!

## Common Tasks

### Running Tests
```bash
# In Claude Code, just type:
/quality:test

# Or manually:
npm test        # Node.js
pytest          # Python
cargo test      # Rust
go test ./...   # Go
```

### Creating a Commit
```bash
# In Claude Code:
/git:commit

# Claude will:
# 1. Check what changed
# 2. Write a clear commit message
# 3. Create the commit
```

### Creating a Pull Request
```bash
# In Claude Code:
/git:pr

# Claude will:
# 1. Review your changes
# 2. Write a detailed PR description
# 3. Create the pull request
```

### Code Review
```bash
# In Claude Code:
/quality:review

# You'll get:
# - Style suggestions
# - Security checks
# - Best practice recommendations
```

## Customization

### Turn Features On/Off

Edit `.claude/settings.json`:

```json
{
  "hooks": {
    "sessionStart": { "enabled": true },      // Session info
    "preToolUse": { "enabled": true },        // Security checks
    "postToolUse": { "enabled": false }       // Auto-formatting (turned off)
  }
}
```

### Add Your Own Commands

Create `.claude/commands/mycustom/hello.md`:

```markdown
---
description: Say hello
---

Print "Hello World!" to the user.
```

Now you can use `/mycustom:hello` in Claude Code!

## Supported Languages

Works automatically with:

- **JavaScript / TypeScript** (Node.js, React, Vue, etc.)
- **Python** (Django, Flask, FastAPI, etc.)
- **Rust** (Cargo projects)
- **Go** (Go modules)
- **Java** (Maven, Gradle)
- **Ruby** (Rails, Sinatra)
- **PHP** (Laravel, Symfony)
- **C / C++** (CMake, Make)

The template auto-detects your language and uses the right tools.

## Need Help?

### Quick Fixes

**Hooks not working?**
```bash
chmod +x .claude/hooks/*.py
python3 --version  # Must be 3.7+
```

**Commands not found?**
- Restart Claude Code
- Check `.claude/commands/` folder exists

**Want detailed docs?**
- [Complete Setup Guide](docs/SETUP.md)
- [Hooks Documentation](docs/HOOKS.md)
- [Commands Reference](docs/COMMANDS.md)

## Advanced Features

### GitHub Actions (Optional)

Set up AI-powered automation for your GitHub repo:

1. **Go to your GitHub repository settings**
2. **Add secret**: Settings → Secrets → New repository secret
   - Name: `ANTHROPIC_API_KEY`
   - Value: Your API key from [console.anthropic.com](https://console.anthropic.com)
3. **Enable workflows**: Settings → Actions → General → Allow all actions

Now you get:
- **Automatic PR reviews** - AI reviews every pull request
- **Issue planning** - Tag issues with `@claude` for implementation plans
- **Doc updates** - Weekly documentation sync

See [docs/SETUP.md](docs/SETUP.md#github-actions-setup) for details.

### MCP Servers (Optional)

Extend Claude with extra capabilities by installing MCP servers.

Quick install:
```bash
# GitHub integration
npm install -g @anthropic/mcp-server-github

# Enhanced thinking
npm install -g @anthropic/mcp-server-sequential-thinking
```

See [docs/MCP_SERVERS.md](docs/MCP_SERVERS.md) for configuration.

### RAG Integration (Advanced)

Add **Retrieval-Augmented Generation** to automatically provide context from your project documentation.

**What is RAG?**
RAG gives Claude instant access to your entire knowledge base using semantic search and vector embeddings.

**Quick Setup:**
```bash
# Install Archon (RAG knowledge base)
git clone -b stable https://github.com/coleam00/Archon.git
cd Archon
docker-compose up -d

# Configure MCP connection in ~/.claude.json
{
  "mcpServers": {
    "archon": {
      "type": "http",
      "url": "http://localhost:8051"
    }
  }
}

# Add your project docs
# Open http://localhost:3737 and upload documentation
```

**Benefits:**
- 🔍 Claude automatically searches your documentation
- 📚 Better answers based on your specific project
- 💡 Instant access to code examples from docs
- 🎯 Context-aware recommendations

**Full Guide**: [docs/RAG_INTEGRATION.md](docs/RAG_INTEGRATION.md)

## FAQ

**Q: Do I need to install Claude Code?**
A: Yes, this is a template for Claude Code. Get it at [claude.ai/code](https://claude.ai/code)

**Q: Will this work with my existing project?**
A: Absolutely! Just copy the `.claude` folder to your project.

**Q: What if I don't want auto-formatting?**
A: Disable it in `.claude/settings.json` - set `postToolUse.enabled` to `false`

**Q: Is this free?**
A: The template is free (MIT license). Claude Code requires a Claude subscription.

**Q: Can I customize the commands?**
A: Yes! Edit files in `.claude/commands/` or add your own.

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Quick contribution steps:
1. Fork this repo
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Resources

- **Full Documentation**: [docs/](docs/)
- **Changelog**: [CHANGELOG.md](CHANGELOG.md)
- **License**: [MIT License](LICENSE)
- **Issues**: [Report a bug](https://github.com/yourusername/claude-starter/issues)

## Credits

Built with ❤️ using [Claude Code](https://claude.ai/code) by Anthropic

---

**Found this helpful? Star the repo!** ⭐
