---
description: Create a new feature branch with proper naming convention
---

# Create Feature Branch

Create a new feature branch following naming conventions.

## Naming Conventions

### Standard Formats

1. **Feature**: `feature/<short-description>`
   - Example: `feature/user-authentication`

2. **Bug Fix**: `fix/<issue-or-description>`
   - Example: `fix/login-timeout`

3. **Hotfix**: `hotfix/<critical-issue>`
   - Example: `hotfix/security-patch`

4. **Refactor**: `refactor/<component>`
   - Example: `refactor/api-client`

5. **Docs**: `docs/<topic>`
   - Example: `docs/api-documentation`

6. **Chore**: `chore/<task>`
   - Example: `chore/update-dependencies`

### With Issue Numbers

If related to an issue:
- `feature/123-user-authentication`
- `fix/456-login-timeout`

## Process

### 1. Verify Clean State
```bash
git status
```

If uncommitted changes exist:
- Ask to commit or stash first
- Or create branch anyway and bring changes

### 2. Update Main Branch
```bash
git fetch origin
git checkout main
git pull origin main
```

### 3. Create and Checkout Branch
```bash
git checkout -b <branch-name>
```

### 4. Set Upstream
```bash
git push -u origin <branch-name>
```

### 5. Confirm Creation
```bash
git branch --show-current
git status
```

## Interactive Mode

If no branch name provided:
1. Ask for branch purpose (feature, fix, etc.)
2. Ask for short description
3. Check if related to an issue
4. Generate branch name
5. Confirm with user
6. Create branch

## Validation

Branch name should:
- Be lowercase
- Use hyphens (not underscores or spaces)
- Be descriptive but concise
- Follow team conventions

## Arguments

- `/git:branch feature/new-feature` - Create specific branch
- `/git:branch` - Interactive mode to generate name

## Post-Creation

After branch creation:
- Display current branch
- Show next steps (make changes, commit, push)
- Remind about /git:pr when ready
