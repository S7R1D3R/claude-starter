---
description: Create a structured commit using conventional commits format
---

# Create Conventional Commit

Create a well-structured commit message following the Conventional Commits specification.

## Process

### 1. Check Git Status
Run `git status` to see:
- Staged files
- Unstaged files
- Untracked files

### 2. Review Changes
Run `git diff --staged` to see exactly what will be committed.

### 3. Analyze Changes
Determine the commit type based on changes:
- **feat**: New feature or functionality
- **fix**: Bug fix
- **docs**: Documentation only changes
- **style**: Code style changes (formatting, missing semicolons, etc.)
- **refactor**: Code refactoring (neither fixes bug nor adds feature)
- **perf**: Performance improvements
- **test**: Adding or updating tests
- **chore**: Changes to build process, dependencies, or tools
- **ci**: Changes to CI/CD configuration
- **build**: Changes to build system or dependencies

### 4. Generate Commit Message Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Example**:
```
feat(auth): add OAuth2 authentication flow

Implemented OAuth2 authentication with Google and GitHub providers.
Includes token refresh logic and secure session management.

Closes #123
```

### 5. Create Commit
Execute: `git commit -m "<commit-message>"` using HEREDOC format:
```bash
git commit -m "$(cat <<'EOF'
feat(scope): subject line

Body explaining what and why.
EOF
)"
```

## Commit Message Rules

### Subject Line
- Max 50 characters
- Lowercase after type
- No period at the end
- Imperative mood ("add" not "added")

### Body (Optional but Recommended)
- Wrap at 72 characters
- Explain WHAT and WHY, not HOW
- Separate from subject with blank line

### Footer (Optional)
- Reference issues: `Closes #123`, `Fixes #456`
- Breaking changes: `BREAKING CHANGE: description`

## Examples

```
feat(api): add user profile endpoint

Implemented GET /api/users/:id endpoint with caching.
Includes validation and error handling.

Closes #45
```

```
fix(login): resolve session timeout issue

Fixed bug where sessions expired prematurely due to
incorrect cookie settings.

Fixes #78
```

```
docs(readme): update installation instructions

Added troubleshooting section and updated dependencies.
```

## Arguments

Accepts `$ARGUMENTS` for commit message: `/git:commit "feat: add feature"`

If no arguments, analyze changes and generate appropriate message.
