# Claude Code Starter Boilerplate

A ready-to-use template that supercharges your development with AI automation, code quality tools, intelligent workflows, and **RAG-powered documentation access** for any programming language.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-2025-purple)](https://claude.ai/code)
[![RAG Enabled](https://img.shields.io/badge/RAG-Archon-green)](https://github.com/coleam00/Archon)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

## What is This?

This is a **starter template** that adds powerful AI capabilities to your coding projects. Think of it as a smart assistant that:
- 🧙 **NEW: Skills System** - Modular AI expertise that auto-activates (Released Oct 2025!)
- 🔍 **Automatically searches your documentation** using RAG (Retrieval-Augmented Generation)
- ✅ Automatically checks your code quality
- 🛡️ Prevents security mistakes
- ✨ Formats and organizes your code
- 📝 Helps you write better commits and pull requests
- 🌐 Works with **any programming language** (JavaScript, Python, Rust, Go, Java, etc.)

### ⭐ NEW: Skills System (Oct 2025)

**Modular AI expertise** that extends Claude Code with specialized capabilities:
- **Auto-Invoked**: Just ask naturally - skills activate automatically
- **setup-wizard**: Intelligent project configuration (included!)
- **Domain Expertise**: Add skills for security, testing, DevOps, and more
- **Team Sharing**: Create custom skills with your team's knowledge
- **Marketplace Ready**: Install community skills or create your own

**Example:** Say *"Set up this project"* and the setup-wizard skill auto-activates!

### ⭐ NEW: Docker MCP Toolkit Integration

**One-click MCP server deployment** is now available!
- 200+ pre-built MCP servers in a curated catalog
- Visual UI management in Docker Desktop
- Secure credential handling with zero config files
- Containerized isolation prevents dependency conflicts

### ⭐ NEW: RAG Integration with Archon

Claude now has **instant access to your entire knowledge base**:
- Semantic search across all project documentation
- Automatic context injection for better answers
- Code examples from docs available instantly
- Vector-based relevance matching

No more manually searching docs or copy-pasting context!

## Quick Start

Choose your setup path:

### 🤖 Option A: Automated Setup Wizard (2 minutes) ⭐ **NEW!**
AI-powered wizard that automatically detects and configures everything.

### 🚀 Option B: Basic Manual Setup (5 minutes)
Get started with hooks and commands only.

### 🐳 Option C: Docker MCP Toolkit (10 minutes)
One-click MCP server deployment with visual management.

### 🎯 Option D: Full Setup with RAG (15 minutes) ⭐ **Advanced**
Get everything including RAG-powered documentation access.

---

## 🤖 Option A: Automated Setup Wizard ⭐ **ONE-TIME ONBOARDING**

**⚠️ Important:** The setup wizard is for **INITIAL PROJECT SETUP ONLY**. Run it once when you first add Claude Code to your project. After setup, use slash commands (`/dev:setup`, `/git:commit`, etc.) and hooks for daily development.

Choose the method that fits your workflow best!

### 1. Get the Template

```bash
git clone https://github.com/yourusername/claude-starter.git my-project
cd my-project
```

### 2. Choose Your Setup Method (First-Time Only)

#### 💬 Interactive Slash Command (Recommended)
**Best for:** Learning, first-time setup, understanding features
**No API key required** - Uses your Claude Code session!

```bash
# Start Claude Code
claude-code

# Then run:
/setup:wizard
```

Claude will interactively guide you through configuration with explanations. Ask questions as you go!

#### 🤖 Auto-Invoked Skill (Natural Language)
**Best for:** Natural language onboarding, first-time setup

```bash
# Install the skill once
.claude/skills/setup-wizard/install.sh

# Then on a NEW/UNCONFIGURED project, just talk naturally:
"Set up this project for TypeScript"
"Configure Claude Code for this repository"
```

**Note:** The skill automatically detects if your project is already configured and offers to update/enhance instead of re-running full setup.

#### 🧠 Python Agent (Complex Projects)
**Best for:** Autonomous setup, dependency installation, complex projects

```bash
python3 scripts/wizard/setup_agent.py
```

#### ⚡ Shell Script (CI/CD & Quick Setup)
**Best for:** Offline setup, CI/CD pipelines, fast automated setup

```bash
./scripts/setup-wizard.sh
```

**Not sure which to use?** See [docs/SETUP_WIZARD.md](docs/SETUP_WIZARD.md) for detailed comparison.

### 3. What the Wizard Does

The wizard automatically:
- ✅ Detects your programming languages and frameworks
- ✅ Identifies package managers (npm, pip, cargo, etc.)
- ✅ Configures hooks and slash commands
- ✅ Makes all scripts executable
- ✅ Creates necessary directories
- ✅ Optionally installs dependencies
- ✅ Validates the setup
- ✅ Provides personalized recommendations

### 4. Start Coding

```bash
claude-code
```

The AI wizard provides intelligent, context-aware setup with personalized recommendations!

**See the full guide:** [docs/SETUP_WIZARD.md](docs/SETUP_WIZARD.md)

---

## 🚀 Option B: Basic Manual Setup

### 1. Get the Template

**For new projects:**
```bash
git clone https://github.com/yourusername/claude-starter.git my-project
cd my-project
```

**For existing projects:**
```bash
# Copy the .claude folder to your project
cp -r /path/to/claude-starter/.claude /path/to/your-project/
cd /path/to/your-project
chmod +x .claude/hooks/*.py
```

### 2. Install Dependencies

```bash
# Node.js
npm install

# Python
pip install -r requirements.txt

# Rust
cargo build

# Go
go mod download

# Or let Claude detect and run the right command:
# claude-code → type: /dev:setup
```

### 3. Start Claude Code

```bash
claude-code
```

✅ You're ready! The template will automatically assist with code quality, security, and formatting.

---

## 🐳 Option C: Docker MCP Toolkit Setup

The easiest way to add powerful MCP servers to Claude Code!

### 1. Install Docker Desktop 4.40+

Download from https://www.docker.com/products/docker-desktop/

```bash
# Verify installation
docker --version
# Must be 4.40 or newer
```

### 2. Enable MCP Toolkit

1. Open Docker Desktop
2. Go to **Settings** → **Beta Features**
3. Enable **"Enable Docker MCP Toolkit"**
4. Click **Apply & Restart**

### 3. Get the Template

```bash
git clone https://github.com/yourusername/claude-starter.git my-project
cd my-project
chmod +x .claude/hooks/*.py
```

### 4. Add MCP Servers

1. In Docker Desktop, click **MCP Toolkit** in the sidebar
2. Go to the **Catalog** tab
3. Search and add these essential servers:
   - **Filesystem Official** - File access (grant `/path/to/my-project`)
   - **GitHub Official** - Repository management (OAuth)
   - **Docker Hub Official** - Container management (optional)
   - **Brave Search Official** - Web research (API key required)

4. For each server, click the **+** icon and complete the configuration wizard

### 5. Connect Claude Code

1. In MCP Toolkit, go to **Clients** tab
2. Find **"Claude Code (CLI)"**
3. Click **Connect**
4. Choose **project-scoped** configuration

### 6. Verify Setup

```bash
cd my-project
claude mcp list

# Expected output:
# ✓ MCP_DOCKER (connected)
#   - filesystem
#   - github
#   - docker-hub
```

### 7. Start Coding!

```bash
claude-code
```

✅ **Done!** You now have enterprise-grade MCP servers with:
- Secure file operations
- GitHub integration
- Docker management
- Web search capabilities
- All managed visually in Docker Desktop!

**Full Guide**: See [docs/DOCKER_MCP_TOOLKIT.md](docs/DOCKER_MCP_TOOLKIT.md) for advanced configuration.

---

## 🎯 Option D: Full Setup with RAG (Advanced)

Get the complete experience with RAG-powered documentation access!

### 1. Get the Template

```bash
# Clone the starter
git clone https://github.com/yourusername/claude-starter.git my-project
cd my-project
chmod +x .claude/hooks/*.py
```

### 2. Install Archon (RAG Backend)

```bash
# Clone Archon in a separate location
cd ~
git clone -b stable https://github.com/coleam00/Archon.git
cd Archon

# Setup environment
cp .env.example .env
```

**Edit `.env` with your credentials:**
```bash
nano .env
```

Add:
```env
# Get these from https://supabase.com (free tier works!)
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key

# Use OpenAI or local Ollama
OPENAI_API_KEY=your_openai_key  # Or leave empty for Ollama
```

**Start Archon services:**
```bash
docker-compose up -d

# Verify all services are running
docker-compose ps
# Should show: archon-frontend, archon-server, archon-mcp, archon-agents
```

### 3. Configure Claude Code MCP

Edit `~/.claude.json` (create if it doesn't exist):

```json
{
  "mcpServers": {
    "archon": {
      "type": "http",
      "url": "http://localhost:8051",
      "description": "RAG knowledge base for project context"
    }
  }
}
```

### 4. Populate Your Knowledge Base

Open Archon UI:
```bash
open http://localhost:3737
# Or visit: http://localhost:3737 in your browser
```

**Add documentation sources:**

1. **Create a project** for your codebase
2. **Add sources**:
   - 📄 Upload PDFs (API docs, architecture diagrams)
   - 🌐 Crawl websites (framework docs, references)
   - 📦 Index repositories (your project README, docs/)
3. **Wait for processing** (watch the progress bar)
4. **Verify** in the Knowledge tab

**Example sources to add:**
- Your project's README and `/docs` folder
- Framework documentation (React, Django, etc.)
- API specifications
- Architecture diagrams and design docs

### 5. (Optional) Enable RAG-Enhanced Hooks

For automatic context injection on every prompt:

```bash
cd my-project
cp examples/rag-integration/hooks/rag-prompt-enhance.py .claude/hooks/
chmod +x .claude/hooks/rag-prompt-enhance.py
```

Edit `.claude/settings.json`:
```json
{
  "hooks": {
    "userPromptSubmit": {
      "command": ".claude/hooks/rag-prompt-enhance.py",
      "enabled": true
    }
  }
}
```

### 6. (Optional) Add Knowledge Commands

```bash
mkdir -p .claude/commands/knowledge
cp examples/rag-integration/commands/knowledge-search.md .claude/commands/knowledge/search.md
cp examples/rag-integration/commands/knowledge-add.md .claude/commands/knowledge/add.md
```

Now you can use:
- `/knowledge:search <query>` - Search documentation
- `/knowledge:add <source>` - Add new docs

### 7. Start Claude Code

```bash
cd my-project
claude-code
```

### 8. Test RAG Integration

Try asking Claude:
```
> How do I implement authentication in this framework?
```

Claude will:
1. 🔍 Automatically search your knowledge base
2. 📚 Find relevant documentation
3. 💡 Provide context-specific answers with code examples
4. ✨ Reference your actual project docs

🎉 **You're all set!** Claude now has instant access to your entire knowledge base.

---

## What's the Difference?

| Feature | Basic Setup | Docker MCP Toolkit | Full Setup with RAG |
|---------|-------------|-------------------|---------------------|
| **Hooks & Commands** | ✅ | ✅ | ✅ |
| **Code Quality** | ✅ | ✅ | ✅ |
| **Security Checks** | ✅ | ✅ | ✅ |
| **MCP Servers** | ❌ Manual | ✅ Visual UI | ✅ + RAG |
| **File Operations** | Basic | ✅ MCP-powered | ✅ MCP-powered |
| **GitHub Integration** | Manual | ✅ One-click | ✅ One-click |
| **Doc Search** | ❌ Manual | ❌ | ✅ Automatic |
| **Context Injection** | ❌ | ❌ | ✅ |
| **Code Examples** | ❌ | ❌ | ✅ From your docs |
| **Credential Security** | N/A | ✅ Docker secrets | ✅ Docker secrets |
| **Visual Management** | ❌ | ✅ Docker Desktop | ✅ Docker Desktop |
| **Setup Time** | 5 min | 10 min | 15 min |

💡 **Recommendations**:
- **Just starting?** → Basic Setup
- **Want professional MCP management?** → Docker MCP Toolkit ⭐
- **Need documentation search?** → Full Setup with RAG

## What You Get

### Smart Slash Commands

Quick commands you can type to automate common tasks:

**Setup:**
- `/setup:wizard` - Interactive intelligent project setup wizard ⭐ **NEW!**

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

**MCP Management** (with Docker MCP Toolkit):
- `/mcp:setup-docker` - Guided Docker MCP Toolkit setup
- `/mcp:status` - Check status of all MCP servers

**Knowledge Base** (with RAG setup):
- `/knowledge:search` - Search your documentation
- `/knowledge:add` - Add new docs to knowledge base

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

3. **Skills** add expert knowledge ⭐ **NEW 2025!**:
   - **setup-wizard**: Intelligent project configuration (auto-invoked)
   - **session-start-hook**: Session startup customization
   - Custom skills: Add your team's expertise
   - Marketplace skills: Install from community
   - Skills auto-activate based on your requests - just ask naturally!

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

## Skills System ⭐ **NEW in 2025!**

**Skills** are modular AI expertise modules released in October 2025 that extend Claude Code with specialized capabilities. Think of them as plug-and-play AI assistants for specific tasks.

### What Are Skills?

Skills are organized folders containing:
- **Instructions**: Expert knowledge and workflows for specific domains
- **Scripts**: Optional automation code
- **Resources**: Templates, examples, and reference files
- **Metadata**: Configuration for when and how the skill activates

### Key Features

✨ **Auto-Invoked**: Claude automatically uses skills based on your natural language requests
🎯 **Context-Aware**: Skills understand your project type and adapt
🔧 **Composable**: Multiple skills work together seamlessly
📦 **Marketplace Ready**: Install community skills or create your own

### Built-In Skills

This boilerplate includes:

#### 🧙 **setup-wizard** (For Initial Onboarding)
Intelligent project setup and configuration wizard for first-time Claude Code setup.

**Installation:**
```bash
.claude/skills/setup-wizard/install.sh
```

**Usage (On NEW/Unconfigured Projects):**
```
# Just talk naturally - it auto-activates on unconfigured projects!
"Set up this project for TypeScript"
"Configure Claude Code for this repository"
"Initialize my development environment"
```

**What it does:**
- **Checks** if project is already configured (won't re-run on configured projects)
- Detects your programming languages and frameworks
- Recommends optimal Claude Code configurations
- Installs dependencies and sets up tools
- Configures hooks, MCP servers, and GitHub Actions
- Provides personalized recommendations

**Smart Detection:** If project is already configured, offers to update/enhance instead of full setup.

#### 🚀 **session-start-hook**
Creates and develops startup hooks for Claude Code sessions.

**Usage:**
```
"Help me create a session start hook"
"Set up a hook for my repository"
```

### Installing Skills

**From This Boilerplate:**
```bash
# Install the setup wizard skill
.claude/skills/setup-wizard/install.sh

# Choose symlink (auto-updates) or copy (standalone)
```

**From Marketplace** (Coming Soon):
```bash
# Browse available skills
claude skills browse

# Install a skill
claude skills install <skill-name>
```

### Creating Custom Skills

**Quick Start:**
```bash
mkdir -p ~/.claude/skills/my-custom-skill
cd ~/.claude/skills/my-custom-skill

# Create skill metadata
cat > skill.json <<EOF
{
  "name": "my-custom-skill",
  "displayName": "My Custom Skill",
  "description": "Brief description for auto-invocation",
  "version": "1.0.0",
  "triggers": ["keyword1", "keyword2"],
  "capabilities": ["What this skill does"]
}
EOF

# Create skill instructions
cat > instructions.md <<EOF
# My Custom Skill

You are an expert in [domain]. Help the user with [specific task].

## Your Process
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Guidelines
- [Guideline 1]
- [Guideline 2]
EOF
```

**Skill Structure:**
```
~/.claude/skills/
└── your-skill-name/
    ├── skill.json          # Metadata and triggers
    ├── instructions.md     # Main skill prompt
    ├── scripts/           # Optional automation
    │   └── helper.sh
    └── resources/         # Templates and references
        └── template.txt
```

### How Skills Work

1. **You make a request** in natural language
2. **Claude analyzes** your request against all installed skills
3. **Relevant skills activate** automatically
4. **Skills provide** specialized knowledge and workflows
5. **You get better results** with domain expertise

**Example:**
```
You: "Set up this TypeScript project with all best practices"

Claude: [setup-wizard skill auto-activates]
        I'll configure this TypeScript project optimally!

        Detected:
        - TypeScript 5.0
        - React 18
        - npm package manager

        Recommended setup:
        ✓ ESLint + Prettier
        ✓ Jest for testing
        ✓ All quality hooks
        ✓ GitHub Actions

        Proceeding with configuration...
```

### Skills vs Slash Commands vs Hooks

| Feature | Skills | Slash Commands | Hooks |
|---------|--------|----------------|-------|
| **Invocation** | Auto (natural language) | Manual (type /command) | Automatic (on events) |
| **Scope** | Broad, adaptive | Specific, fixed | Event-triggered |
| **Complexity** | High (multi-step workflows) | Medium (single actions) | Low (automation) |
| **Customization** | Full AI reasoning | Template-based | Scripted |
| **Use Case** | Expert guidance | Quick utilities | Background automation |

### Best Practices

✅ **Do:**
- Install skills for domains you work in frequently
- Create team skills for shared workflows
- Use descriptive triggers in skill.json
- Version control your custom skills
- Share useful skills with the community

❌ **Don't:**
- Install too many overlapping skills
- Create skills for simple one-off tasks (use slash commands instead)
- Hardcode credentials in skills
- Skip testing your custom skills

### Learn More

- **Skills Guide**: [docs/SKILLS.md](docs/SKILLS.md)
- **Setup Wizard Guide**: [docs/SETUP_WIZARD.md](docs/SETUP_WIZARD.md)
- **Skill Marketplace**: Coming Soon
- **Community Skills**: Check `anthropics/skills` on GitHub

---

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

### Additional MCP Servers

Beyond Archon RAG, you can add other MCP servers for extended capabilities:

**GitHub Integration:**
```bash
npm install -g @anthropic/mcp-server-github
```

**Enhanced Thinking:**
```bash
npm install -g @anthropic/mcp-server-sequential-thinking
```

See [docs/MCP_SERVERS.md](docs/MCP_SERVERS.md) for full configuration guide.

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

**Q: Do I need RAG/Archon to use this template?**
A: No! RAG is optional. The basic setup (hooks + commands) works great without it. RAG adds documentation search capabilities.

**Q: Is Archon hard to set up?**
A: Not at all! It takes ~15 minutes and uses Docker. You'll need a free Supabase account and optionally an OpenAI API key (or use local Ollama).

**Q: What's the benefit of RAG?**
A: Claude can automatically search your documentation and provide context-specific answers. It's like having your entire knowledge base instantly available.

**Q: Can I use RAG without Archon?**
A: Archon is our recommended RAG solution, but you could integrate other vector databases. See [docs/RAG_INTEGRATION.md](docs/RAG_INTEGRATION.md) for details.

**Q: Does RAG work offline?**
A: If you use Ollama for embeddings instead of OpenAI, yes! The entire stack runs locally.

**Q: RAG isn't working, what should I check?**
A: Verify these:
1. Archon services running: `docker-compose ps`
2. MCP configured in `~/.claude.json`
3. Knowledge base populated (check http://localhost:3737)
4. Restart Claude Code after MCP changes

## Troubleshooting

### Archon Not Connecting

```bash
# Check services
cd ~/Archon
docker-compose ps

# View logs
docker-compose logs archon-mcp

# Restart
docker-compose restart
```

### RAG Hook Not Enhancing Prompts

```bash
# Test manually
echo '{"type": "userPromptSubmit", "prompt": "test"}' | \
  python3 .claude/hooks/rag-prompt-enhance.py

# Check permissions
chmod +x .claude/hooks/rag-prompt-enhance.py

# Verify in settings
cat .claude/settings.json | grep -A 3 userPromptSubmit
```

### No Search Results

1. **Add documentation** to Archon (http://localhost:3737)
2. **Wait for indexing** to complete
3. **Try broader search terms**
4. **Check relevance threshold** in hook configuration

For more help, see:
- [RAG Integration Guide](docs/RAG_INTEGRATION.md)
- [Archon Documentation](https://github.com/coleam00/Archon)
- [MCP Setup Guide](docs/MCP_SERVERS.md)

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

Built with ❤️ using:
- [Claude Code](https://claude.ai/code) by Anthropic
- [Archon RAG](https://github.com/coleam00/Archon) by @coleam00

Special thanks to the Archon team for building an amazing RAG solution!

---

**Found this helpful? Star the repo!** ⭐

**Want RAG-powered coding?** See the [Full Setup with RAG](#-option-b-full-setup-with-rag-recommended) guide above!
