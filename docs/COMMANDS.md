# Slash Commands Reference

Complete reference for all 20 slash commands in Claude Code Starter Boilerplate.

## Table of Contents

- [Overview](#overview)
- [Command Categories](#command-categories)
- [Development Commands](#development-commands-dev)
- [Git Commands](#git-commands-git)
- [Code Quality Commands](#code-quality-commands-quality)
- [Documentation Commands](#documentation-commands-docs)
- [AI Enhancement Commands](#ai-enhancement-commands-ai)
- [Command Chaining](#command-chaining)
- [Custom Commands](#custom-commands)

---

## Overview

Slash commands are instructions that expand into detailed prompts for Claude. They provide:

- **Consistency** - Standardized workflows across projects
- **Best practices** - Embedded coding standards
- **Efficiency** - Complex tasks with simple commands
- **Automation** - Multi-step processes in one command

### How Slash Commands Work

1. You type: `/dev:setup`
2. Claude reads: `.claude/commands/dev/setup.md`
3. Claude executes: The detailed instructions in that file

### Command Syntax

```bash
/category:command [arguments]

Examples:
/dev:setup                    # No arguments
/git:branch feature-name      # With argument
/quality:test --coverage      # With flags
```

---

## Command Categories

| Category | Count | Purpose |
|----------|-------|---------|
| `/dev:*` | 5 | Development workflow (setup, build, serve) |
| `/git:*` | 4 | Git operations (commit, branch, PR) |
| `/quality:*` | 5 | Code quality (lint, format, test, review) |
| `/docs:*` | 3 | Documentation (generate, update) |
| `/ai:*` | 3 | AI-powered enhancement (refactor, explain) |

**Total: 20 commands**

---

## Development Commands (/dev:)

### `/dev:init`

Initialize a new project with auto-detected language and framework.

**When to use:**
- Starting a new project from scratch
- Setting up boilerplate structure
- Creating standard files (README, .gitignore, etc.)

**What it does:**
1. Detects desired language/framework from context or asks
2. Creates standard directory structure
3. Generates config files (package.json, pyproject.toml, Cargo.toml, etc.)
4. Creates .gitignore with appropriate patterns
5. Initializes git repository if not present
6. Creates basic README.md

**Example:**
```
/dev:init

# Claude will ask:
"What language/framework? (node/python/rust/go/java)"

# Then create appropriate structure
```

**Supports:**
- Node.js (npm/yarn/pnpm)
- Python (pip/poetry/pipenv)
- Rust (cargo)
- Go (modules)
- Java (maven/gradle)

---

### `/dev:setup`

Install all project dependencies using auto-detected package manager.

**When to use:**
- After cloning a repository
- Setting up development environment
- Installing dependencies after changes

**What it does:**
1. Auto-detects package manager:
   - `package.json` → npm/yarn/pnpm
   - `requirements.txt` or `pyproject.toml` → pip/poetry
   - `Cargo.toml` → cargo
   - `go.mod` → go modules
   - `pom.xml` or `build.gradle` → maven/gradle
2. Runs appropriate install command
3. Verifies installation success
4. Reports any errors with troubleshooting tips

**Example:**
```
/dev:setup

# Claude detects npm and runs:
npm install

# Or detects poetry and runs:
poetry install
```

**Also handles:**
- Pre-commit hooks (`pre-commit install`)
- Git submodules (`git submodule update --init`)
- Development tools installation

---

### `/dev:serve`

Start the development server for the project.

**When to use:**
- Starting local development
- Testing changes in browser/runtime
- Running hot-reload development mode

**What it does:**
1. Detects development server command:
   - Node.js: `npm run dev` or `npm start`
   - Python: `python manage.py runserver` or `flask run`
   - Rust: `cargo run`
   - Go: `go run .`
2. Starts server in background or foreground
3. Shows server URL and port
4. Monitors for startup errors

**Example:**
```
/dev:serve

# Claude runs:
npm run dev

# Output:
🚀 Server running at: http://localhost:3000
```

**Options:**
- Specify port: `/dev:serve --port 8080`
- Production mode: `/dev:serve --prod`

---

### `/dev:build`

Build the project for production.

**When to use:**
- Creating production artifacts
- Testing production build
- Preparing for deployment

**What it does:**
1. Detects build command:
   - Node.js: `npm run build`
   - Python: `python setup.py build` or `poetry build`
   - Rust: `cargo build --release`
   - Go: `go build`
   - Java: `mvn package` or `gradle build`
2. Runs build with production optimizations
3. Reports build size and location
4. Checks for build warnings/errors

**Example:**
```
/dev:build

# Claude runs:
npm run build

# Output:
✅ Build complete
📦 Output: dist/ (2.3 MB)
⚠️  3 warnings (non-critical)
```

**Options:**
- Clean build: `/dev:build --clean`
- Watch mode: `/dev:build --watch`

---

### `/dev:clean`

Clean build artifacts, caches, and temporary files.

**When to use:**
- Build is stale or corrupted
- Clearing disk space
- Troubleshooting build issues
- Before fresh build

**What it does:**
1. Detects and removes:
   - Build outputs (`dist/`, `build/`, `target/`)
   - Package caches (`node_modules/.cache`, `.cache/`)
   - Python caches (`__pycache__/`, `*.pyc`)
   - Test caches (`.pytest_cache/`, `coverage/`)
2. Optionally removes dependency directories
3. Reports space freed

**Example:**
```
/dev:clean

# Claude removes:
dist/
.cache/
__pycache__/
.pytest_cache/

🧹 Cleaned 450 MB
```

**Options:**
- Deep clean: `/dev:clean --deep` (includes node_modules)
- Dry run: `/dev:clean --dry-run` (show what would be removed)

---

## Git Commands (/git:)

### `/git:branch`

Create a new feature branch with proper naming convention.

**When to use:**
- Starting new feature development
- Creating bugfix branches
- Following branching strategy

**What it does:**
1. Checks current git status
2. Ensures working tree is clean (or stashes changes)
3. Updates main/master branch
4. Creates branch with naming convention
5. Pushes to remote with tracking

**Naming conventions:**
- `feature/description` - New features
- `fix/description` - Bug fixes
- `refactor/description` - Code refactoring
- `docs/description` - Documentation changes
- `test/description` - Test additions

**Example:**
```
/git:branch user-authentication

# Claude creates:
feature/user-authentication

# Or for bugfix:
/git:branch fix-login-error

# Claude creates:
fix/fix-login-error
```

**Options:**
- Specify type: `/git:branch feature user-auth`
- From branch: `/git:branch my-feature --from develop`

---

### `/git:commit`

Create a structured commit using Conventional Commits format.

**When to use:**
- Committing changes with clear message
- Following commit conventions
- Maintaining clean git history

**What it does:**
1. Shows `git status` and `git diff`
2. Analyzes changes to determine type
3. Generates commit message following convention
4. Stages appropriate files (excludes sensitive files)
5. Creates commit with generated message
6. Verifies commit success

**Conventional Commits format:**
```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `refactor`: Code refactoring (no feature change)
- `test`: Adding tests
- `chore`: Maintenance tasks
- `perf`: Performance improvements
- `ci`: CI/CD changes

**Example:**
```
/git:commit

# Claude analyzes changes and creates:
feat(auth): add user authentication with JWT

- Implement login/logout endpoints
- Add JWT token generation
- Create auth middleware
- Add user session management

Closes #123
```

**Options:**
- Specify type: `/git:commit --type fix`
- Skip hooks: `/git:commit --no-verify` (not recommended)

---

### `/git:sync`

Sync branch with remote and resolve conflicts.

**When to use:**
- Before creating PR
- After main branch updates
- Resolving merge conflicts
- Keeping branch up-to-date

**What it does:**
1. Fetches latest from remote
2. Shows divergence (ahead/behind)
3. Attempts merge or rebase
4. Detects conflicts
5. Helps resolve conflicts if present
6. Pushes synced branch

**Example:**
```
/git:sync

# Claude runs:
git fetch origin
git merge origin/main

# Or with rebase:
git rebase origin/main

# If conflicts:
⚠️  Conflicts detected in:
  - src/user.js
  - tests/user.test.js

Let me help resolve these...
```

**Options:**
- Use rebase: `/git:sync --rebase`
- From branch: `/git:sync --from develop`
- Force push: `/git:sync --force` (after rebase)

---

### `/git:pr`

Create a pull request with comprehensive description.

**When to use:**
- Ready to merge feature
- Requesting code review
- Creating PR with full context

**What it does:**
1. Checks branch is pushed to remote
2. Analyzes all commits in branch
3. Reviews all code changes
4. Generates comprehensive PR description:
   - Summary of changes
   - What/why/how
   - Testing instructions
   - Breaking changes
   - Related issues
5. Creates PR via GitHub CLI or provides template

**Example:**
```
/git:pr

# Claude analyzes 5 commits and generates:

## Summary
Add user authentication system with JWT tokens

## Changes
- ✨ New `/login` and `/logout` endpoints
- 🔒 JWT token generation and validation
- 🛡️  Auth middleware for protected routes
- 📝 User session management
- ✅ 15 new tests (100% coverage)

## Testing
1. Run tests: `npm test`
2. Start server: `npm start`
3. Test login: `curl -X POST http://localhost:3000/login -d '{"username":"test","password":"test"}'`
4. Verify token in response
5. Test protected endpoint with token

## Breaking Changes
- ⚠️  `/api/user` now requires authentication header

## Related Issues
Closes #123, Relates to #98

---

# Then creates PR with this description
```

**Options:**
- Draft PR: `/git:pr --draft`
- Target branch: `/git:pr --base develop`
- Assign reviewers: `/git:pr --reviewers @user1,@user2`

---

## Code Quality Commands (/quality:)

### `/quality:review`

Comprehensive code review with best practices and suggestions.

**When to use:**
- Before committing changes
- After completing feature
- Regular code quality checks
- Learning best practices

**What it does:**
1. Analyzes all modified files
2. Checks code quality dimensions:
   - **Readability** - Clear names, comments, structure
   - **Maintainability** - DRY, SOLID, patterns
   - **Performance** - Efficiency, algorithms, complexity
   - **Security** - Vulnerabilities, input validation, secrets
   - **Testing** - Test coverage, edge cases
   - **Documentation** - Comments, docs, examples
3. Provides severity levels (critical/major/minor/suggestion)
4. Suggests specific improvements with code examples

**Example:**
```
/quality:review

# Claude reviews code and reports:

📊 Code Review Summary: src/user.js

✅ Strengths:
  - Clear function names
  - Good test coverage (95%)
  - Proper error handling

⚠️  Issues Found:

[MAJOR] Security: SQL Injection Risk (line 42)
  const query = `SELECT * FROM users WHERE id = ${userId}`;

  Fix: Use parameterized query
  const query = 'SELECT * FROM users WHERE id = ?';
  db.query(query, [userId]);

[MINOR] Performance: Unnecessary loop (line 78)
  users.forEach(u => console.log(u.name));

  Suggestion: Use map for transformation
  const names = users.map(u => u.name);

[SUGGESTION] Readability: Magic number (line 103)
  if (age > 18) { ... }

  Consider: const MINIMUM_AGE = 18;
```

**Options:**
- Specific file: `/quality:review src/user.js`
- Focus area: `/quality:review --focus security`
- Brief mode: `/quality:review --brief`

---

### `/quality:lint`

Run all configured linters on the project.

**When to use:**
- Before committing
- Checking code style
- Finding potential bugs
- Enforcing standards

**What it does:**
1. Detects linters by language:
   - JavaScript/TypeScript: ESLint, StandardJS
   - Python: Pylint, Flake8, Ruff
   - Rust: Clippy
   - Go: golangci-lint, go vet
   - Java: Checkstyle
2. Runs all available linters
3. Aggregates and categorizes issues
4. Suggests fixes for auto-fixable issues

**Example:**
```
/quality:lint

# Claude runs:
npm run lint (or eslint .)
pylint src/

# Output:
📋 Lint Results

ESLint: 12 issues (3 errors, 9 warnings)
  src/user.js:42:5 - error - 'userId' is not defined
  src/user.js:78:12 - warning - Unexpected console.log

Pylint: 8.5/10
  src/api.py:15:0 - C0103: Variable name "X" doesn't conform to snake_case

✨ 5 issues can be auto-fixed with --fix
```

**Options:**
- Auto-fix: `/quality:lint --fix`
- Specific file: `/quality:lint src/user.js`
- Severity: `/quality:lint --max-warnings 0`

---

### `/quality:format`

Auto-format all code files with configured formatters.

**When to use:**
- Before committing
- After writing new code
- Enforcing consistent style
- Batch formatting changes

**What it does:**
1. Detects formatters by language:
   - JavaScript/TypeScript: Prettier, StandardJS
   - Python: Black, autopep8, YAPF
   - Rust: rustfmt
   - Go: gofmt, goimports
   - Java: google-java-format
2. Formats all files in project
3. Reports files changed
4. Shows formatting statistics

**Example:**
```
/quality:format

# Claude runs:
prettier --write .
black src/

# Output:
✨ Formatting complete

Files formatted: 23
  JavaScript: 15 files
  Python: 8 files

Changes:
  src/user.js - 12 lines changed
  src/api.py - 5 lines changed
```

**Options:**
- Check only: `/quality:format --check` (don't modify)
- Specific file: `/quality:format src/user.js`
- Specific language: `/quality:format --lang python`

---

### `/quality:test`

Execute full test suite with coverage reporting.

**When to use:**
- Before committing
- After code changes
- Verifying functionality
- Checking test coverage

**What it does:**
1. Detects test framework:
   - JavaScript: Jest, Mocha, Vitest
   - Python: pytest, unittest
   - Rust: `cargo test`
   - Go: `go test`
   - Java: JUnit (Maven/Gradle)
2. Runs all tests with coverage
3. Reports results with statistics
4. Highlights failing tests
5. Shows coverage by file/function

**Example:**
```
/quality:test

# Claude runs:
npm test -- --coverage
pytest --cov=src tests/

# Output:
🧪 Test Results

Tests: 127 passed, 3 failed, 130 total
Duration: 12.4s

Coverage:
  Overall: 87.5%
  src/user.js: 95.2%
  src/api.js: 78.3%
  src/utils.js: 92.1%

Failed Tests:
  ❌ user.test.js › UserService › should handle invalid email
     Expected: 400, Received: 500

  ❌ api.test.js › POST /users › should reject duplicate
     TypeError: Cannot read property 'id' of undefined
```

**Options:**
- Watch mode: `/quality:test --watch`
- Specific test: `/quality:test user.test.js`
- Update snapshots: `/quality:test --update-snapshots`
- Verbose: `/quality:test --verbose`

---

### `/quality:security`

Run security vulnerability scan on code and dependencies.

**When to use:**
- Before releases
- After adding dependencies
- Regular security audits
- Finding vulnerabilities

**What it does:**
1. Scans dependencies:
   - JavaScript: `npm audit`, Snyk
   - Python: `safety`, `pip-audit`
   - Rust: `cargo audit`
   - Go: `govulncheck`
2. Analyzes code for vulnerabilities:
   - SQL injection
   - XSS vulnerabilities
   - Hardcoded secrets
   - Insecure functions
   - OWASP Top 10 issues
3. Reports severity and fixes
4. Suggests remediation steps

**Example:**
```
/quality:security

# Claude runs:
npm audit
safety check
snyk test

# Output:
🔒 Security Scan Results

Dependencies: 3 vulnerabilities found

[HIGH] Regular Expression Denial of Service in lodash
  Package: lodash@4.17.19
  Fix: Upgrade to lodash@4.17.21
  Run: npm install lodash@4.17.21

[MODERATE] Prototype Pollution in minimist
  Package: minimist@1.2.5
  Fix: Upgrade to minimist@1.2.6

Code Analysis: 2 issues found

[CRITICAL] SQL Injection Risk (src/user.js:42)
  const query = `SELECT * FROM users WHERE id = ${userId}`;
  Use parameterized queries instead.

[HIGH] Hardcoded Secret (src/config.js:15)
  const API_KEY = "sk_live_abc123xyz";
  Move to environment variable.

💡 Run: /quality:security --fix
   To automatically fix dependency issues
```

**Options:**
- Auto-fix: `/quality:security --fix` (updates dependencies)
- Severity: `/quality:security --min-severity high`
- Report only: `/quality:security --report-only` (no fixes)

---

## Documentation Commands (/docs:)

### `/docs:generate`

Generate API documentation from code comments and structure.

**When to use:**
- After adding public APIs
- Before releases
- Updating documentation
- Creating API reference

**What it does:**
1. Detects documentation tools:
   - JavaScript: JSDoc, TypeDoc
   - Python: Sphinx, pydoc
   - Rust: `cargo doc`
   - Go: `godoc`
   - Java: Javadoc
2. Extracts documentation from:
   - Function/class comments
   - Type annotations
   - Examples in docstrings
3. Generates HTML/Markdown docs
4. Creates navigation structure

**Example:**
```
/docs:generate

# Claude runs:
npm run docs (or jsdoc src/)
sphinx-build -b html docs/ docs/_build/

# Output:
📚 Documentation generated

Files: 45 pages
Output: docs/_build/html/
Index: docs/_build/html/index.html

Modules documented:
  - UserService (12 methods)
  - AuthService (8 methods)
  - Database (15 methods)

✅ Open: file:///.../docs/_build/html/index.html
```

**Options:**
- Format: `/docs:generate --format markdown`
- Output dir: `/docs:generate --output docs/api/`
- Private APIs: `/docs:generate --include-private`

---

### `/docs:readme`

Update README.md based on recent changes and project state.

**When to use:**
- After major changes
- Before releases
- When README is outdated
- Adding new features

**What it does:**
1. Analyzes current README.md
2. Detects project changes:
   - New dependencies
   - New scripts in package.json
   - New features in code
   - Changed API endpoints
3. Suggests updates:
   - Installation instructions
   - Usage examples
   - API documentation
   - Configuration options
4. Rewrites sections as needed

**Example:**
```
/docs:readme

# Claude analyzes project and suggests:

📝 README Updates Needed

Current README: Last updated 3 months ago

Detected changes:
  ✨ New feature: User authentication (not documented)
  📦 New dependency: jsonwebtoken (not in README)
  🔧 New script: npm run migrate (not listed)
  🌐 New endpoint: POST /api/login (not documented)

Suggested updates:
  1. Add authentication section to Usage
  2. Update installation with new env variables
  3. Add API endpoints table
  4. Update scripts section

Apply updates? [Y/n]
```

**Options:**
- Sections: `/docs:readme --section installation`
- Template: `/docs:readme --template minimal`
- Dry run: `/docs:readme --dry-run`

---

### `/docs:changelog`

Generate CHANGELOG entries from commits.

**When to use:**
- Preparing releases
- Documenting changes
- Creating release notes
- Keeping changelog current

**What it does:**
1. Analyzes commits since last tag/release
2. Groups by Conventional Commits type:
   - Features (feat)
   - Bug fixes (fix)
   - Breaking changes (BREAKING)
   - Other (chore, docs, refactor)
3. Generates changelog in Keep a Changelog format
4. Adds to CHANGELOG.md or creates new
5. Suggests version bump (semver)

**Example:**
```
/docs:changelog

# Claude analyzes 23 commits and generates:

## [1.2.0] - 2025-11-11

### Added
- User authentication with JWT tokens (#123)
- Password reset functionality (#145)
- Email verification on signup (#156)

### Fixed
- Login error with special characters (#142)
- Session timeout not working (#151)
- Memory leak in auth middleware (#159)

### Changed
- Updated authentication flow (BREAKING)
- Improved error messages (#147)

### Security
- Fixed SQL injection in user query (#163)

---

Suggested version: 1.2.0 → 1.3.0 (minor bump)
Breaking changes detected: Consider 2.0.0

Update CHANGELOG.md? [Y/n]
```

**Options:**
- Version: `/docs:changelog --version 1.3.0`
- Since: `/docs:changelog --since v1.2.0`
- Unreleased: `/docs:changelog --unreleased`

---

## AI Enhancement Commands (/ai:)

### `/ai:context`

Load comprehensive project context for complex AI tasks.

**When to use:**
- Before large refactoring
- Understanding unfamiliar codebase
- Planning complex features
- Architectural decisions

**What it does:**
1. Analyzes entire project structure
2. Identifies:
   - Programming languages used
   - Frameworks and libraries
   - Architecture patterns
   - Key files and modules
   - Dependencies and their purposes
3. Creates context map:
   - Entry points
   - Core modules
   - Utilities
   - Tests
   - Configuration
4. Loads relevant files into context

**Example:**
```
/ai:context

# Claude analyzes project:

📊 Project Context Analysis

Languages: JavaScript (60%), Python (30%), TypeScript (10%)
Framework: Express.js + React
Architecture: RESTful API + SPA

Directory structure:
  src/
    ├── api/          → REST endpoints (15 files)
    ├── services/     → Business logic (8 files)
    ├── models/       → Data models (12 files)
    ├── utils/        → Helper functions (6 files)
    └── middleware/   → Express middleware (4 files)

  client/
    ├── components/   → React components (32 files)
    ├── pages/        → Page components (8 files)
    ├── hooks/        → Custom hooks (5 files)
    └── api/          → API client (3 files)

Key dependencies:
  - express@4.18.2 → Web framework
  - jsonwebtoken@9.0.2 → Authentication
  - prisma@5.1.0 → Database ORM
  - react@18.2.0 → UI library

Entry points:
  - Backend: src/index.js
  - Frontend: client/src/App.jsx

I've loaded the key files into context. What would you like to work on?
```

**Options:**
- Focus: `/ai:context --focus backend`
- Depth: `/ai:context --depth 2` (directory levels)
- Include: `/ai:context --include tests`

---

### `/ai:refactor`

Intelligent refactoring with best practices.

**When to use:**
- Code is messy or duplicated
- Improving code quality
- Applying design patterns
- Modernizing old code

**What it does:**
1. Analyzes code structure and patterns
2. Identifies refactoring opportunities:
   - Code duplication (DRY violations)
   - Long functions (>50 lines)
   - Complex conditions (high cyclomatic complexity)
   - God objects (too many responsibilities)
   - Primitive obsession
   - Feature envy
3. Suggests specific refactorings:
   - Extract method/function
   - Extract class/module
   - Introduce parameter object
   - Replace conditional with polymorphism
   - Move method to appropriate class
4. Applies refactoring with explanation
5. Ensures tests still pass

**Example:**
```
/ai:refactor src/user.js

# Claude analyzes and suggests:

🔧 Refactoring Opportunities in src/user.js

[1] Extract Method (lines 42-87)
  Function: createUser (46 lines, complexity: 12)
  Issue: Handles validation, database, email sending

  Suggestion: Extract to 3 functions:
    - validateUserInput()
    - saveUserToDatabase()
    - sendWelcomeEmail()

  Benefit: Single Responsibility, easier testing

[2] Code Duplication (lines 103-125, 156-178)
  Duplicate validation logic in 2 places

  Suggestion: Extract to validateInput(rules, data)

  Benefit: DRY, consistent validation

[3] Magic Numbers (lines 67, 89, 134)
  Hardcoded: 18, 100, 3600

  Suggestion:
    const MINIMUM_AGE = 18;
    const MAX_USERNAME_LENGTH = 100;
    const SESSION_TIMEOUT = 3600;

Apply refactorings? [all/1/2/3/n]
```

**Options:**
- Specific refactoring: `/ai:refactor --type extract-method`
- Dry run: `/ai:refactor --dry-run`
- Aggressive: `/ai:refactor --aggressive` (more changes)

---

### `/ai:explain`

Explain complex code sections in detail.

**When to use:**
- Understanding unfamiliar code
- Onboarding new team members
- Documenting complex logic
- Learning new patterns

**What it does:**
1. Analyzes specified code section
2. Explains:
   - What the code does (functionality)
   - Why it's structured this way (rationale)
   - How it works (step-by-step)
   - Patterns and techniques used
   - Dependencies and interactions
   - Potential gotchas
3. Provides simplified examples
4. Suggests improvements if applicable

**Example:**
```
/ai:explain src/auth.js:42-87

# Claude explains:

📖 Code Explanation: src/auth.js (lines 42-87)

## What it does
This function implements JWT-based authentication middleware for Express.js.

## How it works

1. **Extract token** (lines 42-48)
   ```javascript
   const token = req.headers.authorization?.split(' ')[1];
   ```
   Gets token from "Authorization: Bearer <token>" header
   Using optional chaining (?.) to safely access

2. **Verify token** (lines 50-58)
   ```javascript
   const decoded = jwt.verify(token, process.env.JWT_SECRET);
   ```
   Verifies signature using secret key
   Throws error if invalid/expired

3. **Load user** (lines 60-72)
   ```javascript
   const user = await User.findById(decoded.userId);
   ```
   Fetches user from database using ID from token
   Checks if user still exists

4. **Attach to request** (lines 74-78)
   ```javascript
   req.user = user;
   next();
   ```
   Makes user available to route handlers

5. **Error handling** (lines 80-87)
   ```javascript
   catch (error) { ... }
   ```
   Returns 401 for invalid tokens
   Returns 500 for server errors

## Patterns used
- **Middleware pattern** - Express.js middleware
- **Error handling** - Try-catch with specific error codes
- **Async/await** - For database operations

## Dependencies
- jsonwebtoken - JWT verification
- User model - Database access

## Potential issues
⚠️  No rate limiting - vulnerable to brute force
💡  Consider caching user lookups
```

**Options:**
- Level: `/ai:explain --level beginner` (or intermediate/advanced)
- Focus: `/ai:explain --focus security`
- Examples: `/ai:explain --with-examples`

---

## Command Chaining

You can chain multiple commands for complex workflows:

```bash
# Full quality check before commit
/quality:lint && /quality:format && /quality:test && /quality:review

# Complete release workflow
/quality:test && /docs:changelog && /dev:build && /git:pr

# Setup new environment
/dev:setup && /dev:build && /quality:test

# Full documentation update
/docs:generate && /docs:readme && /docs:changelog
```

**Note:** Commands run sequentially. Later commands only run if earlier ones succeed.

---

## Custom Commands

### Creating Custom Commands

Add new commands in `.claude/commands/<category>/<name>.md`:

```markdown
---
description: "Brief description (shown in /help)"
---

# Your Command Name

Detailed instructions for Claude to follow when this command is invoked.

## Steps

1. First, do this...
2. Then, check that...
3. Finally, output...

## Example

Show example of expected output

## Important

Any critical notes or warnings
```

### Command Structure

**Frontmatter (required):**
```yaml
---
description: "One-line description"
---
```

**Body (instructions for Claude):**
- Clear step-by-step instructions
- Examples of expected behavior
- Error handling guidance
- Output format specification

### Example Custom Command

**`.claude/commands/quality/dependency-check.md`:**

```markdown
---
description: "Check for outdated dependencies"
---

# Check Dependencies

Scan project for outdated dependencies and security issues.

## Steps

1. Detect package manager (npm/pip/cargo/go)

2. Run appropriate command:
   - npm: `npm outdated`
   - pip: `pip list --outdated`
   - cargo: `cargo outdated`
   - go: `go list -u -m all`

3. For each outdated package:
   - Show current version
   - Show latest version
   - Show changelog link
   - Highlight breaking changes

4. Run security audit:
   - npm: `npm audit`
   - pip: `safety check`
   - cargo: `cargo audit`

5. Summarize:
   - Total outdated: X packages
   - Security issues: Y vulnerabilities
   - Recommended updates

## Output Format

```
📦 Dependency Check Results

Outdated: 5 packages
  express: 4.17.1 → 4.18.2 (minor update)
  react: 17.0.2 → 18.2.0 (major update, BREAKING)

Security: 2 vulnerabilities
  [HIGH] lodash@4.17.19 (upgrade to 4.17.21)

💡 Run: npm update (for minor updates)
⚠️  Manual review needed for: react (major)
```

## Usage

```
/quality:dependency-check
```

---

## Troubleshooting Commands

### Command Not Found

```bash
# Check command file exists
ls .claude/commands/category/name.md

# Check frontmatter format
head -n 5 .claude/commands/category/name.md

# Should show:
# ---
# description: "..."
# ---
```

### Command Not Working

1. **Check Claude Code version** - Commands require 2025.1+
2. **Verify file structure** - Must be in `.claude/commands/`
3. **Check frontmatter** - Must have `description` field
4. **Restart Claude** - Reload command definitions

### Command Output Unclear

Edit command file to:
- Add more specific instructions
- Include output format examples
- Add error handling steps
- Clarify expected behavior

---

## Best Practices

### When to Use Commands

✅ **Good:**
- Repeated workflows
- Complex multi-step tasks
- Enforcing standards
- Team consistency

❌ **Avoid:**
- One-off unique tasks
- Simple single-step operations
- When you need flexibility

### Combining Commands

Combine commands for powerful workflows:

```bash
# Pre-commit checklist
/quality:lint --fix
/quality:format
/quality:test
/quality:review
/git:commit

# Release workflow
/quality:test
/quality:security
/docs:generate
/docs:changelog
/dev:build
/git:pr
```

### Command Arguments

Pass arguments naturally:

```bash
# Specific file
/quality:review src/user.js

# With flags
/quality:test --coverage --watch

# Multiple arguments
/git:branch feature user-authentication
```

---

## Additional Resources

- [CLAUDE.md](../CLAUDE.md) - Project instructions
- [SETUP.md](SETUP.md) - Installation guide
- [HOOKS.md](HOOKS.md) - Hooks reference
- [SKILLS.md](SKILLS.md) - Skills system

---

**Version:** 1.0.0
**Last Updated:** 2025-11-11
