# Claude Code Starter Boilerplate

## Project Overview

This is a **language-agnostic starter boilerplate** for Claude Code, incorporating all the latest 2025 features and best practices. It provides intelligent automation, code quality enforcement, and productivity enhancements for any programming language or framework.

## Purpose

Provide a production-ready Claude Code setup with:
- Automated code quality checks
- Security validation
- Intelligent prompt enhancement
- Comprehensive slash commands
- **Modular Skills system** (New 2025 feature!)
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

### Setup (/setup:)
- `/setup:wizard` - Interactive intelligent project setup wizard (Recommended for first-time setup)

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

## Skills (New in 2025!)

**Skills** are modular, reusable capabilities that extend Claude Code with specialized expertise and workflows. Released in October 2025, Skills represent a powerful new way to enhance Claude's abilities with domain-specific knowledge and automation.

### What Are Skills?

Skills are organized folders containing:
- **Instructions**: Prompts and guidelines for specific tasks
- **Scripts**: Executable code for automation
- **Resources**: Reference files, templates, and documentation
- **Configuration**: Metadata and invocation rules

### Key Features

- **Model-Invoked**: Claude automatically decides when to use a Skill based on your request and the Skill's description
- **Marketplace Available**: Install Skills from the `anthropics/skills` repository
- **Custom Skills**: Create your own Skills for team-specific workflows
- **Automatic Loading**: Skills load automatically when relevant to the task
- **Available to**: Pro, Max, Team, and Enterprise users

### How to Use Skills

Skills are invoked automatically by Claude when needed. You don't need to explicitly call them - just describe what you want to do, and Claude will use the appropriate Skill if available.

**Example:**
```
You: "Set up a session start hook for this project"
Claude: [Automatically invokes the session-start-hook Skill]
```

### Installing Skills

**From Marketplace:**
```bash
# Browse available Skills
ls ~/.claude/skills/

# Skills are typically installed via Claude Code plugins
# Check the anthropics/skills repository for available Skills
```

**Manual Installation:**
```bash
# Create a custom Skill
mkdir -p ~/.claude/skills/my-custom-skill
cd ~/.claude/skills/my-custom-skill

# Add Skill configuration
cat > skill.json <<EOF
{
  "name": "my-custom-skill",
  "description": "Brief description of what this Skill does",
  "version": "1.0.0"
}
EOF

# Add Skill instructions
cat > instructions.md <<EOF
# My Custom Skill Instructions
[Your detailed instructions here]
EOF
```

### Available Skills (Project-Specific)

Check your `~/.claude/skills/` directory to see installed Skills:
- **setup-wizard**: Intelligent project setup and configuration wizard (Install with `.claude/skills/setup-wizard/install.sh`)
- **session-start-hook**: Create and develop startup hooks for Claude Code sessions
- _More Skills will appear here as you install them_

**Recommended:** Install the setup-wizard skill for seamless project configuration using natural language!

### Creating Custom Skills

**Skill Structure:**
```
~/.claude/skills/
└── your-skill-name/
    ├── skill.json          # Metadata and configuration
    ├── instructions.md     # Main Skill prompt
    ├── scripts/           # Executable scripts
    │   └── setup.sh
    └── resources/         # Templates and reference files
        └── template.txt
```

**Best Practices for Skills:**
1. **Clear Description**: Write descriptive metadata so Claude knows when to invoke
2. **Focused Purpose**: Each Skill should do one thing well
3. **Self-Contained**: Include all necessary resources within the Skill
4. **Tested**: Verify Skills work across different scenarios
5. **Documented**: Provide clear instructions and examples

### Skills vs. Slash Commands

| Feature | Skills | Slash Commands |
|---------|--------|----------------|
| **Invocation** | Automatic by Claude | Manual by user |
| **Scope** | Broad, complex workflows | Specific, defined tasks |
| **Flexibility** | Highly adaptable | Fixed behavior |
| **Use Case** | Domain expertise | Quick utilities |

### When to Use Skills

Use Skills for:
- Complex, multi-step workflows
- Domain-specific expertise (e.g., security, DevOps)
- Team-wide best practices and patterns
- Repetitive tasks that need intelligent adaptation
- Specialized tooling and integrations

### Skill Development Tips

1. **Start Simple**: Begin with basic instructions, expand as needed
2. **Include Examples**: Show expected inputs and outputs
3. **Error Handling**: Provide guidance for edge cases
4. **Version Control**: Track Skill changes like code
5. **Share with Team**: Publish useful Skills to your team repository

### Resources

- **Skills Marketplace**: `anthropics/skills` on GitHub
- **Documentation**: Check `~/.claude/skills/README.md`
- **Community Skills**: Explore shared Skills from other developers
- **Skill Templates**: Use starter templates for common patterns

---

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

## RAG Integration (Advanced)

This project supports **Retrieval-Augmented Generation (RAG)** through Archon integration.

### What is RAG?

RAG enhances AI responses by:
- **Retrieving** relevant context from a vector database
- **Augmenting** prompts with that context automatically
- **Generating** more accurate, project-specific answers

### Setup

1. **Install Archon** (RAG knowledge base)
   ```bash
   git clone -b stable https://github.com/coleam00/Archon.git
   cd Archon && docker-compose up -d
   ```

2. **Configure MCP** in `~/.claude.json`
   ```json
   {
     "mcpServers": {
       "archon": {
         "type": "http",
         "url": "http://localhost:8051"
       }
     }
   }
   ```

3. **Populate Knowledge Base**
   - Open http://localhost:3737
   - Add project documentation
   - Add API specifications
   - Add code examples

### Benefits

With RAG enabled:
- ✅ Claude automatically searches your docs
- ✅ Context-aware code suggestions
- ✅ Follows your specific patterns
- ✅ Includes relevant examples from your docs

### Optional: RAG-Enhanced Hooks

Copy example hooks from `examples/rag-integration/hooks/`:
- `rag-prompt-enhance.py` - Auto-inject context into prompts
- Automatic documentation lookup
- No manual searching needed

### Slash Commands

Available RAG commands (copy from `examples/rag-integration/commands/`):
- `/knowledge:search` - Query documentation
- `/knowledge:add` - Add new docs to knowledge base

**Full RAG Guide**: See `docs/RAG_INTEGRATION.md`

## External Context

Import additional configuration and documentation:
@.claude/commands/
@docs/

## Project-Specific Notes

_This section will be auto-populated based on your specific project. Add custom instructions, patterns, or conventions here using the `#` key in Claude Code._

## Quick Start

### First-Time Setup

If this is your first time using this project, set up your environment:

**Interactive Setup (Recommended):**
```
/setup:wizard
```
This will guide you through configuration with explanations and help you understand all features.

**Quick Automated Setup:**
Run `./scripts/setup-wizard.sh` from terminal for fast, offline setup.

**Natural Language Setup (After Installing Skill):**
Just say "Set up this project" and the setup wizard skill will automatically activate.

See [docs/SETUP_WIZARD.md](docs/SETUP_WIZARD.md) for all setup options.

### After Setup

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
- Skills Guide: `docs/SKILLS.md`
- MCP Setup: `docs/MCP_SERVERS.md`
- Setup Guide: `docs/SETUP.md`

---

**Remember**: This boilerplate enforces quality and security automatically. Trust the hooks, use the slash commands, and leverage Skills for maximum productivity with the latest 2025 Claude Code features!
