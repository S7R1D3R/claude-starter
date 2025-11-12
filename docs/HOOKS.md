# Hooks Reference Guide

Complete reference for all Claude Code hooks in this boilerplate.

## Table of Contents

- [Overview](#overview)
- [Hook Configuration](#hook-configuration)
- [Session Start Hook](#session-start-hook)
- [User Prompt Submit Hook](#user-prompt-submit-hook)
- [Pre-Tool-Use Hook](#pre-tool-use-hook)
- [Post-Tool-Use Hook](#post-tool-use-hook)
- [Stop Hook](#stop-hook)
- [Notification Hook](#notification-hook)
- [Logs and Debugging](#logs-and-debugging)
- [Custom Hook Development](#custom-hook-development)

---

## Overview

Hooks are Python scripts that execute at specific points during Claude Code sessions. They enable:

- **Automation** - Auto-format code, run linters, check git status
- **Safety** - Block dangerous commands, protect sensitive files
- **Enhancement** - Add context, improve prompts, validate inputs
- **Visibility** - Log actions, send notifications, track changes

### Hook Lifecycle

```
1. Session Start    → Display project context, check git status
2. Prompt Submit    → Enhance vague prompts, add context
3. Pre-Tool-Use     → Validate commands, block dangerous operations
4. Tool Execution   → (Claude uses tools)
5. Post-Tool-Use    → Auto-format, lint, test affected files
6. Stop             → Final validation, check for TODOs, notify
```

### Hook Types

| Hook | When | Purpose | Blocking |
|------|------|---------|----------|
| **session-start** | Session begins | Show context | No |
| **user-prompt-submit** | Before prompt sent | Enhance prompt | Yes (can block) |
| **pre-tool-use** | Before tool runs | Validate safety | Yes (can block) |
| **post-tool-use** | After tool succeeds | Quality checks | No |
| **stop** | Session ends | Final validation | No |
| **notification** | On events | Desktop alerts | No |

---

## Hook Configuration

Hooks are configured in `.claude/settings.json`:

```json
{
  "hooks": {
    "sessionStart": {
      "enabled": true
    },
    "userPromptSubmit": {
      "enabled": true
    },
    "preToolUse": {
      "enabled": true,
      "matchers": {
        "toolName": ["Bash", "Write", "Edit"]
      }
    },
    "postToolUse": {
      "enabled": true,
      "matchers": {
        "toolName": ["Write", "Edit"]
      }
    },
    "stop": {
      "enabled": true
    },
    "notification": {
      "enabled": false
    }
  }
}
```

### Matchers

Matchers control when hooks run:

- **toolName**: Only run for specific tools (`["Bash", "Write", "Edit"]`)
- **No matcher**: Run for all tool invocations

---

## Session Start Hook

**File:** `.claude/hooks/session-start.py`
**When:** Executes once when a new Claude Code session starts
**Blocking:** No

### Purpose

- Display project context and environment info
- Detect programming languages and package managers
- Show git status and recent commits
- List quick start commands
- Show active hooks status

### What It Does

1. **Language Detection**
   - Counts files by extension (.py, .js, .rs, .go, etc.)
   - Determines primary language(s)
   - Displays file count per language

2. **Package Manager Detection**
   - Checks for `package.json` (npm/yarn/pnpm)
   - Checks for `requirements.txt` or `pyproject.toml` (pip/poetry)
   - Checks for `Cargo.toml` (cargo)
   - Checks for `go.mod` (go modules)
   - Checks for `pom.xml` or `build.gradle` (maven/gradle)

3. **Git Status**
   - Shows current branch
   - Shows uncommitted files count
   - Displays last 5 commits
   - Shows remote tracking status

4. **Quick Start Commands**
   - Suggests installation commands
   - Suggests test commands
   - Suggests build commands

### Output Example

```
╔════════════════════════════════════════════════════════════════╗
║                   Claude Code Session Started                   ║
╚════════════════════════════════════════════════════════════════╝

📂 Project: /home/user/my-project
🔤 Language: JavaScript (127 files)
📦 Package Manager: npm (package.json found)

🌿 Git Branch: main
📝 Uncommitted Changes: 3 files

Recent Commits:
  abc1234 feat: add user authentication (2 hours ago)
  def5678 fix: resolve login bug (1 day ago)

💡 Quick Start:
   npm install  → Install dependencies
   npm test     → Run tests
   npm run build → Build project

🪝 Active Hooks: 5 enabled
```

### Configuration Options

No custom configuration. Disable in `settings.json` if too slow on large projects.

### Performance Notes

- Runs `find` commands for each language (13 total)
- Can be slow on large projects with many files
- Consider disabling if session start is slow
- Optimization planned in future update

---

## User Prompt Submit Hook

**File:** `.claude/hooks/user-prompt-submit.py`
**When:** Before user prompts are sent to Claude
**Blocking:** Yes (can reject dangerous prompts)

### Purpose

- Detect vague requests and suggest more specificity
- Append relevant context (recent errors, git status)
- Remind about running tests for implementation requests
- **Block dangerous prompts** (destructive requests)

### What It Does

1. **Vague Prompt Detection**
   - Detects prompts like "fix this", "improve code", "make it better"
   - Suggests being more specific
   - Appends reminder about context

2. **Context Enhancement**
   - Checks for recent error logs
   - Appends error context to prompt if relevant
   - Helps Claude understand current issues

3. **Test Reminders**
   - Detects implementation requests ("add feature", "create function")
   - Appends reminder to run tests after changes

4. **Git Status Context**
   - For commit-related prompts, appends git status
   - Helps Claude understand what files changed

5. **Dangerous Prompt Blocking**
   - Blocks prompts containing:
     - "delete everything"
     - "drop database"
     - "remove all files"
     - "format disk"
     - "destroy"
   - Returns error with explanation

### Vague Patterns Detected

- "fix", "fix this", "fix it"
- "improve", "improve this", "make better"
- "refactor", "clean up"
- "help", "help me"
- "debug", "debug this"

### Dangerous Patterns Blocked

- "delete everything", "remove all"
- "drop database", "drop table"
- "rm -rf /", "format disk"
- "destroy", "wipe"

### Output Example

**Before:**
```
User: fix this
```

**After (enhanced):**
```
User: fix this

[Context added by user-prompt-submit hook]
Note: Please be more specific about what needs to be fixed. Include:
- What file or function?
- What's the expected behavior?
- What's the actual behavior?

Recent errors detected:
  TypeError: Cannot read property 'name' of undefined
  at processUser (src/user.js:42)
```

### Configuration Options

Edit `.claude/hooks/user-prompt-submit.py` to:
- Add/remove vague patterns
- Add/remove dangerous patterns
- Customize enhancement messages

---

## Pre-Tool-Use Hook

**File:** `.claude/hooks/pre-tool-use.py`
**When:** BEFORE tools like Bash, Write, or Edit execute
**Blocking:** Yes (blocks dangerous operations)

### Purpose

**This is the security layer.** It validates all tool invocations before execution and blocks:
- Dangerous bash commands
- Writes to sensitive files
- Writes to system directories
- Destructive operations

### What It Does

1. **Bash Command Validation**
   - Checks every bash command for dangerous patterns
   - Blocks destructive commands
   - Logs all blocked attempts

2. **File Write Validation**
   - Checks file paths for sensitive locations
   - Blocks writes to .env, .pem, .key files
   - Blocks writes to system directories

3. **Security Logging**
   - Logs all blocked operations to `.claude/logs/security.log`
   - Includes timestamp, tool, command/path, reason

### Dangerous Bash Patterns Blocked

#### Destructive File Operations
- `rm -rf /`, `rm -rf ~`, `rm -rf *`
- `rm -rf .`, `rm -rf ..`

#### Dangerous Permissions
- `chmod 777`
- `chmod -R 777`

#### System Attacks
- `:(){ :|:& };:` (fork bomb)
- `curl ... | bash`, `wget ... | sh` (remote script piping)

#### Dangerous Device/Filesystem Operations
- `> /dev/sda`, `dd if=... of=/dev/...`
- `mkfs.`, `fdisk`, `parted`

### Sensitive Files Blocked

**File Extensions:**
- `.env`, `.env.local`, `.env.production`
- `.pem`, `.key`, `.crt`
- `id_rsa`, `id_ed25519`, `.ssh/`
- `credentials`, `secrets`, `token`
- `.aws/`, `.gcp/`, `.azure/`

**File Names:**
- `config.json` (in sensitive contexts)
- `database.yml`
- `docker-compose.yml` (with secrets)

### System Directories Protected

- `/etc/`, `/bin/`, `/usr/`, `/var/`, `/sys/`, `/proc/`
- `/boot/`, `/lib/`, `/lib64/`, `/sbin/`

### Output Example

**Blocked bash command:**
```json
{
  "block": true,
  "reason": "🚫 BLOCKED: Dangerous command detected: 'rm -rf /tmp/*'\n\nThis command is potentially destructive and has been blocked for safety.\nIf you need to remove files, please be more specific about which files to remove."
}
```

**Blocked file write:**
```json
{
  "block": true,
  "reason": "🚫 BLOCKED: Attempted write to sensitive file: '.env'\n\nThis file may contain secrets and should not be modified programmatically.\nPlease review and edit this file manually if needed."
}
```

### Security Log Format

`.claude/logs/security.log`:
```json
{
  "timestamp": "2025-11-11T10:30:45.123Z",
  "tool": "Bash",
  "command": "rm -rf /",
  "reason": "Matched dangerous pattern: rm -rf /",
  "blocked": true
}
```

### Configuration Options

**To disable specific checks** (NOT recommended):

Edit `.claude/hooks/pre-tool-use.py`:

```python
# Comment out patterns you want to allow:
dangerous_patterns = [
    # r'rm\s+-rf\s+/', # DISABLED: Allow rm -rf /
    r'chmod\s+777',
    # ... other patterns
]
```

**⚠️ WARNING:** Only disable security checks if you fully understand the risks.

---

## Post-Tool-Use Hook

**File:** `.claude/hooks/post-tool-use.py`
**When:** After Write/Edit tools complete successfully
**Blocking:** No (non-blocking, suggestions only)

### Purpose

- **Auto-format** code files after modification
- **Run linters** on changed files
- Log quality checks for audit trail

### What It Does

1. **Language Detection**
   - Determines language from file extension
   - Selects appropriate formatters/linters

2. **Auto-Formatting**
   - Tries multiple formatters per language
   - Falls back to alternatives if primary unavailable
   - Non-blocking: continues on failure

3. **Linting**
   - Runs linters on formatted files
   - Reports issues found
   - Non-blocking: doesn't prevent tool success

4. **Quality Logging**
   - Logs all formatting attempts to `.claude/logs/quality.log`
   - Includes success/failure status
   - Tracks which tools were used

### Supported Languages & Tools

#### JavaScript/TypeScript
- **Formatters:** prettier → standard → (skip)
- **Linters:** eslint → standard → (skip)

#### Python
- **Formatters:** black → autopep8 → yapf → (skip)
- **Linters:** pylint → flake8 → (skip)

#### Rust
- **Formatters:** rustfmt
- **Linters:** clippy

#### Go
- **Formatters:** gofmt → goimports
- **Linters:** golangci-lint → go vet

#### Java
- **Formatters:** google-java-format
- **Linters:** checkstyle

#### Ruby
- **Formatters:** rubocop (with --auto-correct)
- **Linters:** rubocop

#### PHP
- **Formatters:** php-cs-fixer
- **Linters:** phpcs

#### C/C++
- **Formatters:** clang-format
- **Linters:** clang-tidy

### Output Example

```
✨ Auto-formatted: src/user.js (prettier)
✅ Lint passed: src/user.js (eslint: 0 issues)
```

### Quality Log Format

`.claude/logs/quality.log`:
```json
{
  "timestamp": "2025-11-11T10:35:12.456Z",
  "file": "src/user.js",
  "language": "javascript",
  "formatter": "prettier",
  "formatter_success": true,
  "linter": "eslint",
  "linter_issues": 0,
  "linter_success": true
}
```

### Configuration Options

**To customize formatters:**

Edit `.claude/hooks/post-tool-use.py`:

```python
formatters = {
    'python': ['black', 'ruff'],  # Use ruff instead of autopep8
    'javascript': ['prettier'],    # Only use prettier
}
```

### Performance Notes

- Runs synchronously (blocks briefly while formatting)
- Each tool check calls `which <tool>` to verify availability
- Future optimization: cache tool availability per session

---

## Stop Hook

**File:** `.claude/hooks/stop.py`
**When:** When Claude Code completes all responses
**Blocking:** No (provides suggestions only)

### Purpose

- Final validation before session ends
- Check for uncommitted changes
- Scan for TODO comments in modified files
- Detect test frameworks and remind to run tests
- Send desktop notifications

### What It Does

1. **Git Status Check**
   - Counts uncommitted files
   - Lists changed files
   - Suggests running git status

2. **TODO Scanner**
   - Scans modified files for:
     - `TODO`, `FIXME`, `HACK`, `XXX`, `NOTE`
   - Lists findings with line numbers
   - Suggests addressing before committing

3. **Test Framework Detection**
   - Checks for `package.json` (npm test)
   - Checks for `pytest.ini` or test files (pytest)
   - Checks for `Cargo.toml` (cargo test)
   - Checks for `go.mod` (go test)
   - Suggests running tests if available

4. **Desktop Notifications**
   - Sends notification when session completes
   - Platform-specific (Linux, macOS)
   - Optional: disabled by default

5. **Completion Logging**
   - Logs session completion to `.claude/logs/completion.log`
   - Includes summary of findings

### Output Example

```
╔════════════════════════════════════════════════════════════════╗
║                    Session Complete Summary                     ║
╚════════════════════════════════════════════════════════════════╝

📝 Uncommitted Changes: 3 files
   - src/user.js
   - tests/user.test.js
   - README.md

📌 TODO Comments Found: 2
   - src/user.js:42: TODO: Add error handling
   - src/user.js:87: FIXME: Optimize this query

🧪 Test Framework: npm (package.json found)
   💡 Remember to run: npm test

🔔 Desktop notification sent!
```

### Completion Log Format

`.claude/logs/completion.log`:
```json
{
  "timestamp": "2025-11-11T10:40:00.789Z",
  "uncommitted_files": 3,
  "todo_comments": 2,
  "test_framework": "npm",
  "notification_sent": true
}
```

### Configuration Options

**Enable desktop notifications:**

Edit `.claude/settings.json`:
```json
{
  "hooks": {
    "notification": {
      "enabled": true
    }
  }
}
```

**Customize TODO patterns:**

Edit `.claude/hooks/stop.py`:
```python
todo_patterns = [
    'TODO',
    'FIXME',
    'HACK',
    'XXX',
    'BUG',      # Add BUG
    'OPTIMIZE', # Add OPTIMIZE
]
```

---

## Notification Hook

**File:** `.claude/hooks/notification.py`
**When:** Called by other hooks or on events
**Blocking:** No

### Purpose

Send desktop notifications for important events.

### Platform Support

#### Linux
- Uses `notify-send` (libnotify)
- Install: `sudo apt install libnotify-bin`

#### macOS
- Uses `osascript` (AppleScript, built-in)
- Fallback: `terminal-notifier` (install via brew)

#### Windows
- Not currently supported
- PRs welcome!

### Usage

Called by other hooks:
```python
import subprocess
subprocess.run([
    'python3',
    '.claude/hooks/notification.py',
    json.dumps({
        'type': 'notification',
        'title': 'Claude Code',
        'message': 'Session complete!'
    })
])
```

### Configuration

Enable in `.claude/settings.json`:
```json
{
  "hooks": {
    "notification": {
      "enabled": true
    }
  }
}
```

---

## Logs and Debugging

### Log Files

All hooks log to `.claude/logs/`:

| File | Purpose | Format |
|------|---------|--------|
| `security.log` | Blocked operations | JSON |
| `quality.log` | Formatting/linting | JSON |
| `completion.log` | Session summaries | JSON |

### Log Format

All logs use JSON format for easy parsing:

```json
{
  "timestamp": "2025-11-11T10:30:45.123Z",
  "level": "info",
  "hook": "pre-tool-use",
  "data": { ... }
}
```

### Viewing Logs

```bash
# View security blocks
cat .claude/logs/security.log | jq .

# View recent quality checks
tail -n 50 .claude/logs/quality.log | jq .

# Count blocked operations
grep '"blocked": true' .claude/logs/security.log | wc -l

# Find all TODO comments found
grep 'TODO' .claude/logs/completion.log
```

### Debugging Hooks

**Test hook manually:**
```bash
# Session start
python3 .claude/hooks/session-start.py '{"type": "sessionStart"}'

# Pre-tool-use (test bash command)
python3 .claude/hooks/pre-tool-use.py '{
  "type": "preToolUse",
  "tool": "Bash",
  "parameters": {"command": "ls -la"}
}'

# Post-tool-use (test formatting)
python3 .claude/hooks/post-tool-use.py '{
  "type": "postToolUse",
  "tool": "Write",
  "parameters": {"file_path": "test.py"}
}'
```

**Check hook output:**
```bash
# Should output JSON
python3 .claude/hooks/session-start.py '{"type": "sessionStart"}' | jq .

# Check exit code (0 = success, 2 = block)
python3 .claude/hooks/pre-tool-use.py '{"type": "preToolUse", "tool": "Bash", "parameters": {"command": "rm -rf /"}}'; echo $?
# Should print: 2 (blocked)
```

**Enable debug output:**

Add to hook file:
```python
import sys
print(f"DEBUG: Input: {input_data}", file=sys.stderr)
```

---

## Custom Hook Development

### Hook Interface

All hooks receive JSON input via stdin and return JSON via stdout:

**Input format:**
```json
{
  "type": "hookType",
  "tool": "ToolName",
  "parameters": { ... }
}
```

**Output format (non-blocking):**
```json
{
  "message": "Optional message to display",
  "metadata": { ... }
}
```

**Output format (blocking):**
```json
{
  "block": true,
  "reason": "Explanation of why blocked"
}
```

### Exit Codes

- `0` - Success (allow operation)
- `2` - Block operation (for blocking hooks only)
- Other - Error (treated as failure, operation continues)

### Example Hook

**`.claude/hooks/custom-hook.py`:**
```python
#!/usr/bin/env python3
import sys
import json

def main():
    # Read input
    input_data = json.loads(sys.stdin.read())

    # Your logic here
    if should_block(input_data):
        result = {
            "block": True,
            "reason": "Custom validation failed"
        }
        print(json.dumps(result))
        sys.exit(2)  # Block operation

    # Success
    result = {
        "message": "✅ Custom validation passed"
    }
    print(json.dumps(result))
    sys.exit(0)

if __name__ == '__main__':
    main()
```

**Register in `.claude/settings.json`:**
```json
{
  "hooks": {
    "customHook": {
      "enabled": true,
      "script": ".claude/hooks/custom-hook.py"
    }
  }
}
```

### Best Practices

1. **Always handle errors gracefully** - Don't crash
2. **Use timeouts** - Don't hang indefinitely
3. **Log important events** - Help debugging
4. **Be fast** - Hooks run synchronously
5. **Use exit codes correctly** - 0=success, 2=block
6. **Validate input** - Check JSON structure
7. **Return valid JSON** - Claude expects JSON output

### Testing Hooks

```bash
# Create test input
cat > /tmp/hook-input.json << 'EOF'
{
  "type": "preToolUse",
  "tool": "Bash",
  "parameters": {"command": "echo test"}
}
EOF

# Test hook
cat /tmp/hook-input.json | python3 .claude/hooks/pre-tool-use.py

# Check exit code
echo $?  # Should be 0 for success, 2 for block
```

---

## Security Considerations

### Trust Model

Hooks have **full access** to:
- File system
- Environment variables
- System commands

**⚠️ Only use trusted hooks from verified sources.**

### Hook Security Best Practices

1. **Review hook code** before enabling
2. **Use `.claude/settings.local.json`** for sensitive config (gitignored)
3. **Never hardcode secrets** in hooks
4. **Log security events** for audit trail
5. **Use allowlists** not denylists when possible
6. **Fail closed** - block on errors in security hooks

### Permissions

Hooks run with the same permissions as Claude Code:
- **Read access:** All files Claude can read
- **Write access:** All files Claude can write
- **Execute access:** All commands you can run

**Set appropriate `.claude/settings.json` permissions:**
```json
{
  "permissions": {
    "bash": "ask",   // Always ask before bash
    "write": "ask",  // Always ask before writes
    "edit": "auto"   // Auto-approve edits
  }
}
```

---

## Performance Optimization

### Slow Session Start?

If `session-start.py` is slow:

1. **Disable the hook temporarily:**
   ```json
   "sessionStart": { "enabled": false }
   ```

2. **Or optimize language detection** (see optimization section below)

### Slow Post-Tool-Use?

If `post-tool-use.py` is slow:

1. **Cache tool availability** (planned optimization)
2. **Disable for large files** (add size check)
3. **Use faster formatters** (e.g., ruff instead of black)

### Optimization Techniques

**Cache expensive checks:**
```python
import os
import time

CACHE = {}
CACHE_TTL = 300  # 5 minutes

def check_tool_cached(tool_name):
    now = time.time()
    if tool_name in CACHE:
        value, timestamp = CACHE[tool_name]
        if now - timestamp < CACHE_TTL:
            return value

    # Expensive check
    result = os.system(f'which {tool_name} >/dev/null 2>&1') == 0
    CACHE[tool_name] = (result, now)
    return result
```

---

## Troubleshooting

See [SETUP.md](SETUP.md#troubleshooting) for common hook issues and solutions.

---

## Additional Resources

- [CLAUDE.md](../CLAUDE.md) - Project instructions
- [SETUP.md](SETUP.md) - Installation guide
- [COMMANDS.md](COMMANDS.md) - Slash commands reference
- [Claude Code Documentation](https://docs.claude.com/claude-code) - Official docs

---

**Version:** 1.0.0
**Last Updated:** 2025-11-11
