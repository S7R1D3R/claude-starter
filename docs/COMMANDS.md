# Commands Guide

Complete reference for all slash commands in the Claude Code Starter Boilerplate.

## Table of Contents

1. [Overview](#overview)
2. [Development Commands (/dev:)](#development-commands-dev)
3. [Git Commands (/git:)](#git-commands-git)
4. [Quality Commands (/quality:)](#quality-commands-quality)
5. [Documentation Commands (/docs:)](#documentation-commands-docs)
6. [AI Commands (/ai:)](#ai-commands-ai)
7. [Creating Custom Commands](#creating-custom-commands)
8. [Command Best Practices](#command-best-practices)

---

## Overview

Slash commands are shortcuts that execute predefined prompts to streamline common development tasks. They provide:

- **Consistency**: Standardized workflows across team
- **Automation**: Complex tasks simplified to single commands
- **Context**: Pre-loaded knowledge about your project
- **Efficiency**: Save time on repetitive tasks

### How to Use Commands

```bash
# In Claude Code, type slash followed by command name
/dev:setup
/quality:test
/git:commit
```

### Command Structure

Commands are stored in `.claude/commands/` as Markdown files:

```
.claude/commands/
├── dev/
│   ├── init.md
│   ├── setup.md
│   ├── build.md
│   ├── serve.md
│   └── clean.md
├── git/
│   ├── commit.md
│   ├── pr.md
│   ├── sync.md
│   └── branch.md
├── quality/
│   ├── review.md
│   ├── test.md
│   ├── lint.md
│   ├── format.md
│   └── security.md
├── docs/
│   ├── generate.md
│   ├── readme.md
│   └── changelog.md
└── ai/
    ├── context.md
    ├── refactor.md
    └── explain.md
```

---

## Development Commands (/dev:)

Manage project setup, building, and development workflow.

### /dev:init

**Initialize new project with auto-detected language and framework.**

**Usage:**
```
/dev:init
/dev:init --language python
/dev:init --framework react
```

**What it does:**
1. Detects project type (Node.js, Python, Rust, Go, etc.)
2. Creates necessary configuration files
3. Sets up directory structure
4. Initializes git repository (if needed)
5. Installs basic dependencies

**Example output:**
```
🚀 Initializing new project...

Detected: Node.js + TypeScript + React
Creating structure:
  ✓ src/
  ✓ tests/
  ✓ docs/
  ✓ .gitignore
  ✓ tsconfig.json
  ✓ package.json

Next steps:
  1. Run /dev:setup to install dependencies
  2. Run /dev:serve to start development server
```

---

### /dev:setup

**Install project dependencies based on auto-detected package manager.**

**Usage:**
```
/dev:setup
/dev:setup npm          # Force specific package manager
/dev:setup --production # Production mode only
```

**Auto-detection priority:**
1. `package.json` → `npm install` or `yarn install`
2. `requirements.txt` → `pip install -r requirements.txt`
3. `Pipfile` → `pipenv install`
4. `pyproject.toml` → `poetry install` or `pip install -e .`
5. `Cargo.toml` → `cargo build`
6. `go.mod` → `go mod download`
7. `pom.xml` → `mvn install`
8. `build.gradle` → `gradle build`
9. `Gemfile` → `bundle install`
10. `composer.json` → `composer install`

**Additional setup:**
- Git submodules: `git submodule update --init --recursive`
- Pre-commit hooks: `pre-commit install` (if configured)
- Database setup: Checks for migration files

**Example:**
```
📦 Setting up project dependencies...

Detected: package.json (npm)
Running: npm install

✓ Installed 234 packages in 12.3s
✓ Git submodules initialized
✓ Pre-commit hooks installed

Next: Run /dev:serve to start development
```

---

### /dev:build

**Build the project for production.**

**Usage:**
```
/dev:build
/dev:build --production
/dev:build --watch
```

**Detects and runs:**
- **Node.js**: `npm run build` or `yarn build`
- **TypeScript**: `tsc`
- **Python**: `python setup.py build` or `poetry build`
- **Rust**: `cargo build --release`
- **Go**: `go build`
- **Java**: `mvn package` or `gradle build`

**Output:**
```
🔨 Building project for production...

Command: npm run build
Build tool: Webpack 5

✓ Compiled successfully in 8.2s
✓ Bundle size: 245 KB (gzipped: 89 KB)
✓ Output: dist/

Build artifacts:
  dist/index.html
  dist/main.js
  dist/styles.css
```

---

### /dev:serve

**Start the development server for the project.**

**Usage:**
```
/dev:serve
/dev:serve --port 3000
/dev:serve --watch
```

**Detects and runs:**
- **Node.js**: `npm run dev` or `npm start`
- **Python**: `python app.py` or `flask run` or `uvicorn main:app --reload`
- **Rust**: `cargo run`
- **Go**: `go run main.go`
- **Ruby**: `rails server`
- **PHP**: `php -S localhost:8000`

**Example:**
```
🚀 Starting development server...

Framework: Next.js
Command: npm run dev

✓ Server running on http://localhost:3000
✓ Hot reload enabled
✓ Type checking active

Press Ctrl+C to stop
```

---

### /dev:clean

**Clean build artifacts and caches.**

**Usage:**
```
/dev:clean
/dev:clean --all        # Include dependencies
/dev:clean --cache-only # Only caches
```

**Removes:**
- Build outputs (`dist/`, `build/`, `target/`)
- Cache directories (`.cache/`, `__pycache__/`, `.next/`)
- Temporary files (`*.tmp`, `*.log`)
- Node modules (with `--all`)
- Python virtual environments (with `--all`)

**Example:**
```
🧹 Cleaning project...

Removing:
  ✓ dist/
  ✓ .next/cache/
  ✓ __pycache__/
  ✓ node_modules/.cache/
  ✓ *.log files

Freed: 1.2 GB

Run /dev:setup to reinstall dependencies
```

---

## Git Commands (/git:)

Streamline git operations with best practices built in.

### /git:commit

**Create a structured commit using conventional commits format.**

**Usage:**
```
/git:commit
/git:commit "feat: add user authentication"
/git:commit --amend
```

**Process:**
1. Runs `git status` to show changes
2. Runs `git diff --staged` to review changes
3. Analyzes changes to determine type
4. Generates conventional commit message
5. Creates commit with proper formatting

**Commit types:**
- `feat`: New feature or functionality
- `fix`: Bug fix
- `docs`: Documentation only changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `chore`: Build process, dependencies, tools
- `ci`: CI/CD configuration
- `build`: Build system or dependencies

**Message format:**
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Example:**
```
📝 Creating conventional commit...

Staged changes:
  M src/auth/login.ts
  A src/auth/oauth.ts
  M tests/auth.test.ts

Analysis: New OAuth authentication feature

Commit message:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
feat(auth): add OAuth2 authentication flow

Implemented OAuth2 authentication with Google
and GitHub providers. Includes token refresh
logic and secure session management.

Closes #123
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Commit created: a1b2c3d
```

---

### /git:pr

**Create a pull request with comprehensive description.**

**Usage:**
```
/git:pr
/git:pr --draft
/git:pr "Custom PR title"
```

**Prerequisites:**
- GitHub CLI (`gh`) installed
- Authenticated with GitHub

**Process:**
1. Verifies branch state
2. Analyzes ALL commits since branching from main
3. Generates comprehensive PR description
4. Creates PR using GitHub CLI

**PR template:**
```markdown
## Summary
Brief description of changes

## Changes
- Added X functionality
- Fixed Y bug
- Refactored Z component

## Motivation
Why are these changes needed?

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Manual testing completed
- [ ] No new linting errors

## Screenshots (if applicable)
Add screenshots for UI changes

## Breaking Changes
List any breaking changes

## Related Issues
Closes #issue_number
```

**Example:**
```
🔀 Creating pull request...

Branch: feature/oauth-auth
Base: main
Commits: 5

Analyzing changes:
  ✓ 8 files modified
  ✓ 234 lines added
  ✓ 67 lines removed

Generated PR:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Title: feat: Add OAuth2 authentication

## Summary
Implements OAuth2 authentication with multiple providers

## Changes
- Added OAuth2 flow for Google and GitHub
- Implemented token refresh mechanism
- Added secure session management
- Updated authentication tests

...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ PR created: https://github.com/user/repo/pull/123
```

---

### /git:sync

**Sync branch with remote and resolve conflicts.**

**Usage:**
```
/git:sync
/git:sync main          # Sync with specific branch
/git:sync --rebase      # Use rebase instead of merge
```

**Process:**
1. Fetches latest from remote
2. Shows incoming changes
3. Pulls/rebases changes
4. Handles merge conflicts (if any)
5. Pushes local commits

**Example:**
```
🔄 Syncing with remote...

Fetching: origin/main
Incoming changes:
  • c3d4e5f feat: add notifications
  • f6g7h8i fix: resolve memory leak

Pulling changes...
✓ Merged successfully
✓ No conflicts

Pushing local commits...
✓ 2 commits pushed

Branch is up to date with origin/main
```

---

### /git:branch

**Create a new feature branch with proper naming convention.**

**Usage:**
```
/git:branch feature/user-auth
/git:branch bugfix/login-error
/git:branch hotfix/security-patch
```

**Naming conventions:**
- `feature/*` - New features
- `bugfix/*` - Bug fixes
- `hotfix/*` - Critical production fixes
- `refactor/*` - Code refactoring
- `docs/*` - Documentation updates
- `test/*` - Test additions/updates

**Example:**
```
🌿 Creating new branch...

Branch name: feature/oauth-auth
Base: main

✓ Branch created
✓ Switched to feature/oauth-auth
✓ Tracking origin/feature/oauth-auth

Ready to start development!
```

---

## Quality Commands (/quality:)

Ensure code quality, testing, and security.

### /quality:review

**Comprehensive code review with best practices and suggestions.**

**Usage:**
```
/quality:review
/quality:review src/
/quality:review --all
```

**Review scope:**
1. Unstaged changes: `git diff`
2. Staged changes: `git diff --staged`
3. Recent commits: `git diff HEAD~1..HEAD`
4. Specific files: From arguments

**Review criteria:**

**Code Quality:**
- Clear, descriptive names
- Focused functions (one thing)
- DRY (Don't Repeat Yourself)
- No commented-out code
- No debug statements

**Best Practices:**
- Language-specific conventions
- Proper error handling
- Input validation
- Resource cleanup
- No hardcoded values

**Security:**
- No SQL injection vulnerabilities
- No XSS vulnerabilities
- No command injection risks
- No secrets in code
- Proper authentication/authorization

**Performance:**
- No unnecessary loops
- Efficient data structures
- No N+1 query problems
- Appropriate caching

**Example output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 CODE REVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Files reviewed: 5

📍 File: src/auth.js:42
❌ Issue: Function is too long (87 lines)
💡 Suggestion: Extract helper functions for authentication and validation
🔧 Priority: Medium

Before:
  function authenticate(user) {
    // 87 lines of mixed concerns
  }

After:
  function authenticate(user) {
    validateUser(user);
    const token = generateToken(user);
    return createSession(token);
  }

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📍 File: src/api.js:23
🔴 Issue: SQL injection vulnerability
💡 Suggestion: Use parameterized queries
🔧 Priority: CRITICAL

Before:
  const query = `SELECT * FROM users WHERE id = ${userId}`;

After:
  const query = 'SELECT * FROM users WHERE id = ?';
  db.execute(query, [userId]);

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Summary
Files reviewed: 5
Issues found: 12
  🔴 Critical: 1
  🟡 Major: 4
  🟢 Minor: 7

Overall assessment: NEEDS WORK

Recommendations:
1. Fix critical security issue in api.js
2. Improve error handling in auth.js
3. Add tests for new features
```

---

### /quality:test

**Run test suite and report results.**

**Usage:**
```
/quality:test
/quality:test src/auth
/quality:test --watch
/quality:test --coverage
/quality:test --verbose
```

**Auto-detects:**
- **JavaScript**: Jest, Vitest, Mocha, Cypress, Playwright
- **Python**: pytest, unittest, nose, tox
- **Rust**: cargo test
- **Go**: go test
- **Ruby**: RSpec, Minitest
- **Java**: Maven, Gradle, JUnit
- **PHP**: PHPUnit

**Example output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧪 RUNNING TESTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Test Framework: Jest
Command: npm test

✓ User Authentication (auth.test.js)
  ✓ should login with valid credentials
  ✓ should reject invalid password
  ✓ should handle session timeout

✗ Payment Processing (payment.test.js)
  ✓ should process valid payment
  ✗ should handle payment failure
    Expected: 400
    Received: 500

✓ API Integration (api.test.js)
  ✓ should fetch user data
  ✓ should handle network errors

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Results: 8 passed, 1 failed, 0 skipped
Time: 2.34s
Coverage: 87.3%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ TESTS FAILED

Fix before committing:
  • payment.test.js:23 - Incorrect error code check
```

---

### /quality:lint

**Run all configured linters.**

**Usage:**
```
/quality:lint
/quality:lint src/
/quality:lint --fix
```

**Detects and runs:**
- **JavaScript/TypeScript**: ESLint
- **Python**: pylint, flake8, mypy
- **Rust**: clippy
- **Go**: golint, go vet
- **Ruby**: rubocop
- **PHP**: phpcs
- **Java**: checkstyle

**Example:**
```
🔍 Running linters...

ESLint (JavaScript/TypeScript)
  ✓ 0 errors
  ⚠️  3 warnings

src/api.ts
  Line 42: Unused variable 'temp'
  Line 67: Console statement

Pylint (Python)
  ✓ 0 errors
  ⚠️  1 warning

src/utils.py
  Line 23: Line too long (105/100)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Summary: 0 errors, 4 warnings
Run /quality:lint --fix to auto-fix
```

---

### /quality:format

**Auto-format all code files.**

**Usage:**
```
/quality:format
/quality:format src/
/quality:format --check  # Check only, don't modify
```

**Formatters:**
- **JavaScript/TypeScript**: Prettier
- **Python**: Black, autopep8
- **Rust**: rustfmt
- **Go**: gofmt, goimports
- **Ruby**: rubocop
- **PHP**: php-cs-fixer
- **Java**: google-java-format
- **C/C++**: clang-format

**Example:**
```
✨ Formatting code...

Prettier (JS/TS)
  ✓ Formatted 12 files

Black (Python)
  ✓ Formatted 5 files
  ✓ 234 lines reformatted

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ All files formatted successfully
```

---

### /quality:security

**Run security vulnerability scan on code and dependencies.**

**Usage:**
```
/quality:security
/quality:security --audit-only
/quality:security --fix
```

**Checks:**
- **Dependencies**: Known vulnerabilities
- **Code**: Security issues (SQL injection, XSS, etc.)
- **Secrets**: Exposed API keys, passwords
- **Permissions**: File permissions issues

**Tools used:**
- **Node.js**: npm audit, snyk
- **Python**: safety, bandit
- **Rust**: cargo audit
- **Go**: gosec
- **Ruby**: bundler-audit

**Example:**
```
🛡️  Running security scan...

Dependency Audit
  ✓ No known vulnerabilities

Code Analysis (bandit)
  ⚠️  1 issue found

src/auth.py:45
  Severity: HIGH
  Issue: Hardcoded password detected
  Fix: Use environment variables

Secret Detection
  ❌ 1 secret exposed

.env.example:12
  Type: API key
  Fix: Remove actual key, use placeholder

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔴 Security issues found: 2
Fix before committing!
```

---

## Documentation Commands (/docs:)

Generate and maintain project documentation.

### /docs:generate

**Generate API documentation from code comments and structure.**

**Usage:**
```
/docs:generate
/docs:generate src/api/
/docs:generate --format markdown
```

**Generates:**
- API endpoint documentation
- Function/class documentation
- Type definitions
- Usage examples

**Tools:**
- **JavaScript**: JSDoc, TypeDoc
- **Python**: Sphinx, pdoc
- **Rust**: rustdoc
- **Go**: godoc
- **Java**: Javadoc

---

### /docs:readme

**Update README.md based on recent changes and project state.**

**Usage:**
```
/docs:readme
/docs:readme --full-rewrite
```

**Updates:**
- Installation instructions
- Usage examples
- API changes
- New features
- Dependencies

---

### /docs:changelog

**Generate or update CHANGELOG based on commits.**

**Usage:**
```
/docs:changelog
/docs:changelog --version 2.0.0
```

**Process:**
1. Reads commit messages since last release
2. Groups by type (features, fixes, etc.)
3. Generates CHANGELOG entries
4. Follows Keep a Changelog format

**Example:**
```markdown
## [2.0.0] - 2025-11-11

### Added
- OAuth2 authentication flow (#123)
- User profile management (#145)

### Fixed
- Session timeout bug (#156)
- Memory leak in API client (#167)

### Changed
- Updated authentication flow (#123)
```

---

## AI Commands (/ai:)

Advanced AI-powered code assistance.

### /ai:context

**Load comprehensive project context for complex AI tasks.**

**Usage:**
```
/ai:context
/ai:context --deep
```

**Loads:**
- Project structure
- Key files and configurations
- Recent commits
- Dependencies
- Architecture patterns
- Coding conventions

**Use when:**
- Starting complex refactoring
- Planning large features
- Understanding unfamiliar codebase
- Making architectural decisions

---

### /ai:refactor

**Intelligent code refactoring with best practices.**

**Usage:**
```
/ai:refactor src/auth.js
/ai:refactor --extract-methods
/ai:refactor --solid
/ai:refactor --dry-run
```

**Refactoring techniques:**
- Extract Method
- Extract Class
- Rename
- Move Method
- Simplify Conditional
- Remove Dead Code

**SOLID principles:**
- Single Responsibility
- Open/Closed
- Liskov Substitution
- Interface Segregation
- Dependency Inversion

**See:** [COMMANDS.md - AI Refactor](#ai-commands-ai) for detailed examples

---

### /ai:explain

**Explain complex code sections in detail.**

**Usage:**
```
/ai:explain src/algorithm.js
/ai:explain --beginner
/ai:explain --architecture
```

**Explains:**
- What the code does
- Why it's written this way
- How it works (step-by-step)
- Potential improvements
- Edge cases handled

---

## Creating Custom Commands

### Step 1: Create Command File

```bash
# Create new command category
mkdir -p .claude/commands/custom

# Create command file
touch .claude/commands/custom/deploy.md
```

### Step 2: Write Command Prompt

```markdown
---
description: Deploy application to production
---

# Deploy to Production

Deploy the application to production environment with safety checks.

## Pre-deployment Checks

1. **Run tests**: Ensure all tests pass
   ```bash
   npm test
   ```

2. **Build project**: Create production build
   ```bash
   npm run build
   ```

3. **Check environment**: Verify production config
   ```bash
   echo $NODE_ENV
   ```

## Deployment Steps

1. **Backup current version**
   ```bash
   ssh production "backup-app.sh"
   ```

2. **Deploy new version**
   ```bash
   rsync -avz dist/ production:/var/www/app/
   ```

3. **Restart services**
   ```bash
   ssh production "systemctl restart app"
   ```

4. **Verify deployment**
   ```bash
   curl https://app.com/health
   ```

## Post-deployment

- Monitor logs for errors
- Check performance metrics
- Notify team in Slack

**IMPORTANT**: Always verify tests pass before deploying!
```

### Step 3: Use Command

```
/custom:deploy
```

### Command Template

```markdown
---
description: Short description of what this command does
---

# Command Title

Detailed description of the command.

## What it Does

1. Step one
2. Step two
3. Step three

## Usage

```bash
/category:command
/category:command --option
```

## Arguments

- `$ARGUMENTS` - Available to use in command

## Examples

Example output or usage scenarios

## Notes

Important notes or warnings
```

---

## Command Best Practices

### Do's ✅

1. **Be specific** - Clear, actionable instructions
2. **Auto-detect** - Automatically determine context when possible
3. **Provide examples** - Show expected input/output
4. **Handle errors** - Explain what to do when things fail
5. **Use arguments** - Accept parameters via `$ARGUMENTS`
6. **Show progress** - Keep user informed
7. **Suggest next steps** - What to do after command completes
8. **Document limitations** - Be clear about what command can/can't do
9. **Include checks** - Validate preconditions
10. **Format output** - Use clear, readable formatting

### Don'ts ❌

1. **Don't hardcode paths** - Use relative or detected paths
2. **Don't assume tools** - Check if tools are installed
3. **Don't skip validation** - Always verify inputs
4. **Don't ignore errors** - Handle failure cases
5. **Don't be vague** - Provide specific instructions
6. **Don't mix concerns** - Keep commands focused
7. **Don't skip documentation** - Always include description
8. **Don't forget cleanup** - Clean up temporary files
9. **Don't overcomplicate** - Keep commands simple
10. **Don't hardcode secrets** - Use environment variables

### Command Structure Tips

**Good command:**
```markdown
---
description: Clear, concise description
---

# Title

## Detection
- Auto-detect framework/tools
- Check prerequisites

## Execution
- Step-by-step instructions
- Error handling
- Progress feedback

## Output
- Clear results
- Next steps
- Links to related commands
```

**Poor command:**
```markdown
# Do something

Run this command.
```

---

## Quick Reference

### Most Used Commands

```bash
# Setup & Development
/dev:setup          # Install dependencies
/dev:serve          # Start dev server
/dev:build          # Build for production

# Quality Assurance
/quality:test       # Run tests
/quality:review     # Code review
/quality:lint       # Lint code
/quality:format     # Format code

# Git Workflow
/git:commit         # Create commit
/git:pr             # Create PR
/git:sync           # Sync with remote

# AI Assistance
/ai:refactor        # Refactor code
/ai:explain         # Explain code
/ai:context         # Load context
```

### Command Chaining

While commands can't be directly chained, you can:

**Sequential execution:**
```
/quality:lint
# Wait for completion, then:
/quality:format
# Wait for completion, then:
/quality:test
```

**Create custom combined command:**
```markdown
---
description: Full quality check
---

# Quality Check

Run all quality checks in sequence:

1. Lint: `/quality:lint`
2. Format: `/quality:format`
3. Test: `/quality:test`
4. Review: `/quality:review`
```

---

## Resources

- **Creating Commands**: https://docs.claude.com/claude-code/commands
- **Command Examples**: `.claude/commands/`
- **Setup Guide**: [SETUP.md](SETUP.md)
- **Hooks Guide**: [HOOKS.md](HOOKS.md)

---

**Happy commanding!** ⚡

Use `/help` to see all available commands in your session.
