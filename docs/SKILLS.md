# Claude Code Skills Guide

## Overview

Skills are a groundbreaking 2025 feature that extends Claude Code with modular, reusable capabilities. Think of Skills as specialized "experts" that Claude can consult automatically when needed, providing domain-specific knowledge and workflows.

**Released**: October 2025
**Available to**: Pro, Max, Team, and Enterprise users

---

## Table of Contents

1. [What Are Skills?](#what-are-skills)
2. [How Skills Work](#how-skills-work)
3. [Installing Skills](#installing-skills)
4. [Creating Custom Skills](#creating-custom-skills)
5. [Skill Structure](#skill-structure)
6. [Best Practices](#best-practices)
7. [Skills vs. Other Features](#skills-vs-other-features)
8. [Troubleshooting](#troubleshooting)
9. [Resources](#resources)

---

## What Are Skills?

Skills are organized collections of:

- **Instructions**: Detailed prompts and guidelines for specific tasks
- **Scripts**: Executable automation code
- **Resources**: Templates, reference files, and documentation
- **Metadata**: Configuration and invocation rules

### Key Characteristics

| Feature | Description |
|---------|-------------|
| **Model-Invoked** | Claude automatically decides when to use a Skill |
| **Context-Aware** | Skills load based on relevance to the current task |
| **Modular** | Each Skill is self-contained and independent |
| **Extensible** | Easy to create, modify, and share |
| **Team-Ready** | Share Skills across your organization |

---

## How Skills Work

### Automatic Invocation

Unlike slash commands that you call manually, Skills are invoked automatically by Claude when:

1. Your request matches the Skill's description
2. The task requires the Skill's domain expertise
3. The context suggests the Skill would be helpful

### Example Flow

```
User: "Set up session hooks for this project"
       ↓
Claude analyzes request
       ↓
Matches "session-start-hook" Skill description
       ↓
Automatically loads and uses the Skill
       ↓
Completes task with specialized knowledge
```

### No Explicit Calling Required

```bash
# ❌ Wrong - You don't call Skills like this
/session-start-hook

# ✅ Right - Just describe what you need
"I need to configure startup hooks for my project"
```

---

## Installing Skills

### Method 1: From the Marketplace

```bash
# Navigate to Skills directory
cd ~/.claude/skills/

# Clone from anthropics/skills repository
# (Check GitHub for available Skills)
git clone https://github.com/anthropics/skills/specific-skill-name

# Claude will automatically detect new Skills
```

### Method 2: Via Claude Code Plugins

Skills can be installed through Claude Code's plugin system. Check the Claude Code documentation for your platform-specific installation method.

### Method 3: Manual Installation

See [Creating Custom Skills](#creating-custom-skills) below.

### Verifying Installation

```bash
# List installed Skills
ls -la ~/.claude/skills/

# Expected output:
# drwxr-xr-x  session-start-hook/
# drwxr-xr-x  security-audit/
# drwxr-xr-x  your-custom-skill/
```

---

## Creating Custom Skills

### Quick Start

```bash
# Create Skill directory
mkdir -p ~/.claude/skills/my-awesome-skill
cd ~/.claude/skills/my-awesome-skill

# Create skill.json
cat > skill.json <<'EOF'
{
  "name": "my-awesome-skill",
  "description": "Brief description of what this Skill does - Claude uses this to decide when to invoke",
  "version": "1.0.0",
  "author": "Your Name",
  "tags": ["category", "type", "domain"]
}
EOF

# Create instructions
cat > instructions.md <<'EOF'
# My Awesome Skill

## Purpose
[What this Skill helps with]

## When to Use
[Scenarios where this Skill is helpful]

## Instructions
[Detailed step-by-step guidance for Claude]

## Examples
[Show expected inputs and outputs]

## Resources
[Links to documentation, tools, etc.]
EOF
```

### Directory Structure

```
~/.claude/skills/
└── my-awesome-skill/
    ├── skill.json              # Required: Metadata
    ├── instructions.md         # Required: Main prompt
    ├── README.md              # Optional: User documentation
    ├── scripts/               # Optional: Executable scripts
    │   ├── setup.sh
    │   ├── validate.py
    │   └── deploy.js
    ├── resources/             # Optional: Templates & references
    │   ├── template.txt
    │   ├── config.example.json
    │   └── reference.md
    └── tests/                 # Optional: Skill tests
        └── test_skill.sh
```

---

## Skill Structure

### skill.json (Required)

```json
{
  "name": "skill-name",
  "description": "Clear, specific description for Claude to understand when to invoke this Skill",
  "version": "1.0.0",
  "author": "Your Name",
  "license": "MIT",
  "tags": ["tag1", "tag2"],
  "dependencies": {
    "tools": ["bash", "git"],
    "languages": ["python>=3.8"]
  },
  "configuration": {
    "auto_invoke": true,
    "requires_approval": false
  }
}
```

### instructions.md (Required)

```markdown
# Skill Name

## Overview
Brief description of what this Skill does.

## Purpose
Detailed explanation of the Skill's goals.

## When Claude Should Use This Skill
- Scenario 1
- Scenario 2
- Scenario 3

## Instructions for Claude

### Step 1: [Action]
Detailed guidance...

### Step 2: [Action]
More guidance...

## Examples

### Example 1: [Use Case]
Input:
```
[Example input]
```

Output:
```
[Expected output]
```

## Edge Cases
- Edge case 1: How to handle...
- Edge case 2: What to do when...

## Resources
- [Link to docs]
- [Link to tools]
```

### Scripts (Optional)

```bash
# scripts/setup.sh
#!/bin/bash
set -euo pipefail

echo "Running Skill setup..."
# Your automation here
```

Make scripts executable:
```bash
chmod +x scripts/*.sh
```

### Resources (Optional)

Store templates, configuration examples, and reference materials:

```
resources/
├── template.config.json
├── example.env
├── reference-architecture.md
└── troubleshooting.md
```

---

## Best Practices

### 1. Clear Description

**Bad**:
```json
{
  "description": "Does stuff with code"
}
```

**Good**:
```json
{
  "description": "Creates and configures session start hooks for Claude Code that initialize project-specific tools and environment settings"
}
```

### 2. Focused Purpose

Each Skill should do **one thing well**. If your Skill tries to do too much, split it into multiple Skills.

**Bad**: A single "devops-everything" Skill
**Good**: Separate Skills for deployment, monitoring, logging, etc.

### 3. Self-Contained

Skills should include all necessary resources:

```
✅ Include templates in resources/
✅ Bundle required scripts
✅ Document external dependencies
✅ Provide fallback options

❌ Don't rely on external URLs
❌ Don't assume system tools exist
❌ Don't hard-code paths
```

### 4. Comprehensive Documentation

Your `instructions.md` should be detailed enough that Claude can:
- Understand when to use the Skill
- Follow the steps without ambiguity
- Handle edge cases gracefully
- Provide helpful output to the user

### 5. Testing

Test your Skills thoroughly:

```bash
# Create test scenarios
tests/
├── test_basic.sh
├── test_edge_cases.sh
└── test_error_handling.sh

# Run tests before deploying
./tests/test_basic.sh
```

### 6. Version Control

```bash
# Initialize git for your Skill
cd ~/.claude/skills/your-skill
git init
git add .
git commit -m "feat: initial Skill implementation"

# Tag versions
git tag v1.0.0
```

### 7. Meaningful Tags

```json
{
  "tags": [
    "git",           // Domain
    "automation",    // Type
    "hooks",         // Related feature
    "devops"        // Category
  ]
}
```

---

## Skills vs. Other Features

### Skills vs. Slash Commands

| Aspect | Skills | Slash Commands |
|--------|--------|----------------|
| **Invocation** | Automatic by Claude | Manual by user (`/command`) |
| **Complexity** | Complex, adaptive workflows | Simple, fixed operations |
| **Flexibility** | Highly flexible and context-aware | Predefined behavior |
| **Use Case** | Domain expertise, intelligent workflows | Quick utilities, shortcuts |
| **Learning Curve** | Lower (just describe what you need) | Higher (need to memorize commands) |

**Example:**

```bash
# Slash Command (Manual)
User: /git:commit
Claude: [Always runs the commit workflow]

# Skill (Automatic)
User: "Help me commit these changes with proper conventions"
Claude: [Automatically uses git-workflow Skill if available]
```

### Skills vs. Hooks

| Aspect | Skills | Hooks |
|--------|--------|-------|
| **Trigger** | User requests (via Claude's decision) | Events (session start, tool use, etc.) |
| **Purpose** | Provide expertise and workflows | Automate routine checks and actions |
| **Scope** | Task-specific | Event-driven |

**Use Together:**

A hook might invoke a Skill:
```bash
# .claude/hooks/session-start.sh
# This hook could trigger Claude to use a Skill
echo "Loading project context..."
```

### Skills vs. MCP Servers

| Aspect | Skills | MCP Servers |
|--------|--------|-------------|
| **What** | Instructions + Resources | Live API connections |
| **When** | Knowledge and workflows | External data access |
| **Example** | "How to deploy safely" | Live database queries |

**Complementary:**

Skills can leverage MCP servers to access external data while providing the intelligence to use that data effectively.

---

## Troubleshooting

### Skill Not Being Invoked

**Problem**: Claude isn't using your Skill

**Solutions**:
1. Check description clarity in `skill.json`
2. Verify Skill is in `~/.claude/skills/`
3. Ensure `skill.json` is valid JSON
4. Try being more specific in your request
5. Check that `auto_invoke: true` in configuration

```bash
# Verify Skill structure
cd ~/.claude/skills/your-skill
ls -la
cat skill.json | jq .  # Validate JSON
```

### Skill Errors During Execution

**Problem**: Skill loads but fails

**Solutions**:
1. Check `instructions.md` for clarity
2. Verify script permissions: `chmod +x scripts/*`
3. Test scripts independently
4. Add error handling to scripts
5. Review Claude's error messages

### Skill Conflicts

**Problem**: Multiple Skills match the same request

**Solutions**:
1. Make Skill descriptions more specific
2. Use different tags for different Skills
3. Add exclusion criteria in instructions
4. Consider merging similar Skills

---

## Resources

### Official Resources

- **Skills Marketplace**: `anthropics/skills` on GitHub
- **Claude Code Documentation**: Official docs for Skills feature
- **Community Forum**: Share and discuss Skills
- **Example Skills**: Reference implementations

### Skill Development

```bash
# Recommended directory structure
~/.claude/
├── skills/
│   ├── personal-skills/      # Your custom Skills
│   ├── team-skills/          # Team-shared Skills
│   └── marketplace-skills/   # Downloaded Skills
└── config.json
```

### Sharing Skills

To share a Skill with your team:

```bash
# Create a team Skills repository
git init team-claude-skills
cd team-claude-skills

# Add your Skills
cp -r ~/.claude/skills/your-skill .

# Push to team repo
git add .
git commit -m "feat: add your-skill"
git push origin main

# Team members install with:
# cd ~/.claude/skills
# git clone <team-repo-url>
```

### Example Skills

#### 1. Code Review Skill

```
code-review-skill/
├── skill.json
├── instructions.md
└── resources/
    └── review-checklist.md
```

#### 2. Security Audit Skill

```
security-audit-skill/
├── skill.json
├── instructions.md
├── scripts/
│   ├── scan.sh
│   └── report.py
└── resources/
    └── owasp-top-10.md
```

#### 3. Documentation Generator Skill

```
doc-generator-skill/
├── skill.json
├── instructions.md
├── scripts/
│   └── generate.js
└── resources/
    └── templates/
        ├── api-doc.md
        └── readme.md
```

---

## Advanced Topics

### Conditional Skill Loading

Configure when Skills should be available:

```json
{
  "configuration": {
    "auto_invoke": true,
    "requires_approval": false,
    "conditions": {
      "file_patterns": ["*.py", "*.js"],
      "project_types": ["web", "api"],
      "git_required": true
    }
  }
}
```

### Skill Composition

Skills can reference other Skills:

```markdown
# In instructions.md
## Prerequisites
This Skill works best when used after:
- `setup-environment` Skill
- `validate-dependencies` Skill

## Integration
This Skill can be combined with:
- `deploy` Skill for production releases
- `test-runner` Skill for validation
```

### Skill Analytics

Track Skill usage:

```bash
# Create a simple logging script
scripts/log-usage.sh
#!/bin/bash
echo "$(date): Skill invoked" >> ~/.claude/skills/your-skill/usage.log
```

---

## Quick Reference

### Skill Checklist

- [ ] Clear, descriptive `skill.json`
- [ ] Comprehensive `instructions.md`
- [ ] Scripts are executable (`chmod +x`)
- [ ] Templates in `resources/`
- [ ] Examples in documentation
- [ ] Error handling included
- [ ] Tested independently
- [ ] Version controlled (git)
- [ ] README for users
- [ ] Dependencies documented

### File Templates

See `/resources/skill-templates/` in this repository for:
- `skill.json` template
- `instructions.md` template
- Script templates
- Testing templates

---

## Getting Help

- Check Claude Code documentation
- Review existing Skills in marketplace
- Test Skills incrementally
- Share Skills for feedback
- Contribute to the Skills marketplace

---

**Happy Skill Building!** 🚀

Skills represent the future of AI-assisted development. By creating and sharing Skills, you're contributing to a collective intelligence that makes Claude Code more powerful for everyone.
