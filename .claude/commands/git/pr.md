---
description: Create a pull request with comprehensive description
---

# Create Pull Request

Generate and create a comprehensive pull request using GitHub CLI.

## Prerequisites

Check if `gh` (GitHub CLI) is installed:
```bash
which gh
```

If not installed, provide installation instructions.

## Process

### 1. Verify Branch State
```bash
git status
git log origin/main..HEAD --oneline
git diff origin/main...HEAD --stat
```

### 2. Analyze All Changes
Review the full diff since branching from main:
- What features were added?
- What bugs were fixed?
- What was refactored?
- Are there breaking changes?

### 3. Generate PR Description

Use this template:
```markdown
## Summary
<!-- Brief description of changes -->

## Changes
<!-- Bulleted list of main changes -->
- Added X functionality
- Fixed Y bug
- Refactored Z component

## Motivation
<!-- Why are these changes needed? -->

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Manual testing completed
- [ ] No new linting errors

## Screenshots (if applicable)
<!-- Add screenshots for UI changes -->

## Breaking Changes
<!-- List any breaking changes -->

## Related Issues
Closes #issue_number
```

### 4. Create PR Title
Format: `<type>: <concise summary>`

Examples:
- `feat: Add OAuth2 authentication`
- `fix: Resolve session timeout issue`
- `refactor: Improve database query performance`

### 5. Execute PR Creation
```bash
gh pr create --title "PR Title" --body "$(cat <<'EOF'
## Summary
...
EOF
)"
```

## Additional Options

- `--draft` - Create as draft PR
- `--base main` - Target branch (default: main)
- `--head feature-branch` - Source branch
- `--reviewer username` - Request reviewer
- `--label bug,enhancement` - Add labels

## Post-Creation

After creating PR:
1. Display the PR URL
2. Check if CI/CD workflows are running
3. Suggest next steps (request reviews, wait for checks)

## Arguments

- `/git:pr` - Interactive mode, generates description from commits
- `/git:pr --draft` - Create draft PR
- `/git:pr "Custom title"` - Use custom title

**IMPORTANT**: Analyze ALL commits since diverging from main, not just the latest one!
