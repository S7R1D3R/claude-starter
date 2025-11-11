---
description: Comprehensive code review with best practices and suggestions
---

# Code Review

Perform a thorough code review of recent changes or specified files.

## Review Scope

Determine what to review:
1. **Unstaged changes**: `git diff`
2. **Staged changes**: `git diff --staged`
3. **Recent commits**: `git diff HEAD~1..HEAD`
4. **Specific files**: From $ARGUMENTS

## Review Criteria

### 1. Code Quality
- [ ] Clear, descriptive variable and function names
- [ ] Functions are focused and do one thing
- [ ] Code is DRY (Don't Repeat Yourself)
- [ ] Appropriate use of language idioms
- [ ] No commented-out code
- [ ] No debug statements (console.log, print, etc.)

### 2. Best Practices
- [ ] Follows language-specific conventions
- [ ] Proper error handling
- [ ] Input validation
- [ ] Resource cleanup (close files, connections)
- [ ] Appropriate use of async/await or promises
- [ ] No hardcoded values (use constants/config)

### 3. Security
- [ ] No SQL injection vulnerabilities
- [ ] No XSS vulnerabilities
- [ ] No command injection risks
- [ ] Sensitive data not logged
- [ ] Proper authentication/authorization checks
- [ ] No secrets in code

### 4. Performance
- [ ] No unnecessary loops or iterations
- [ ] Efficient data structures
- [ ] No N+1 query problems
- [ ] Appropriate caching
- [ ] No memory leaks

### 5. Testing
- [ ] Edge cases handled
- [ ] Error cases handled
- [ ] Tests exist and pass
- [ ] Test coverage is adequate

### 6. Documentation
- [ ] Public APIs documented
- [ ] Complex logic explained
- [ ] TODOs have context
- [ ] README updated if needed

## Review Output Format

For each issue found, provide:

```
📍 File: path/to/file.js:42
❌ Issue: Function is too long (87 lines)
💡 Suggestion: Extract helper functions for authentication and validation
🔧 Priority: Medium

Before:
  [code snippet]

After:
  [improved code snippet]
```

## Severity Levels

- 🔴 **Critical**: Security issues, bugs, breaking changes
- 🟡 **Major**: Performance issues, code smells, best practice violations
- 🟢 **Minor**: Style issues, documentation, minor improvements

## Summary Report

After review, provide:
```
📊 Code Review Summary
━━━━━━━━━━━━━━━━━━━━━
Files reviewed: 5
Issues found: 12
  🔴 Critical: 1
  🟡 Major: 4
  🟢 Minor: 7

Overall assessment: GOOD / NEEDS WORK / READY

Recommendations:
1. Fix critical security issue in auth.js
2. Improve error handling in api.js
3. Add tests for new features
```

## Arguments

- `/quality:review` - Review staged changes
- `/quality:review src/` - Review specific directory
- `/quality:review --all` - Review all recent changes

**IMPORTANT**: Be thorough but constructive. Provide actionable suggestions, not just criticism.
