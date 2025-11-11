---
description: Sync branch with remote and resolve conflicts
---

# Sync with Remote

Synchronize local branch with remote repository, handling conflicts safely.

## Process

### 1. Check Current State
```bash
git status
git fetch origin
git log HEAD..origin/$(git rev-parse --abbrev-ref HEAD) --oneline
```

### 2. Stash Local Changes (if any)
```bash
git stash push -m "Auto-stash before sync"
```

### 3. Pull Changes
Determine strategy:
- **Merge** (default): `git pull origin <branch>`
- **Rebase** (cleaner history): `git pull --rebase origin <branch>`

Check git config for pull strategy:
```bash
git config pull.rebase
```

### 4. Handle Conflicts

If conflicts occur:
1. List conflicted files
2. Show conflict markers
3. Offer to:
   - Abort and return to previous state
   - Help resolve conflicts interactively
   - Accept theirs/ours for specific files

### 5. Restore Stashed Changes
```bash
git stash pop
```

### 6. Handle Stash Conflicts
If stash conflicts with pulled changes, help resolve.

## Conflict Resolution

For each conflicted file:
1. Show the conflict
2. Explain both versions
3. Ask user preference or help merge manually
4. Mark as resolved: `git add <file>`

## Verification

After sync:
```bash
git status
git log --oneline -5
```

Report:
- Files changed
- Commits pulled
- Any conflicts resolved
- Current branch state

## Safety Features

- **Always** fetch before pulling
- **Stash** uncommitted changes first
- **Offer abort option** if conflicts are complex
- **Verify** clean state after sync

## Arguments

- `/git:sync` - Sync current branch
- `/git:sync --rebase` - Use rebase instead of merge
- `/git:sync main` - Sync with specific branch

**IMPORTANT**: Never lose user's work. Always stash and provide recovery options.
