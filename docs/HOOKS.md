# Hooks Reference

Complete documentation for all Claude Code hooks in this boilerplate.

## Table of Contents

1. [Overview](#overview)
2. [Hook Types](#hook-types)
3. [Session Start Hook](#session-start-hook)
4. [User Prompt Submit Hook](#user-prompt-submit-hook)
5. [Pre-Tool-Use Hook](#pre-tool-use-hook)
6. [Post-Tool-Use Hook](#post-tool-use-hook)
7. [Stop Hook](#stop-hook)
8. [Creating Custom Hooks](#creating-custom-hooks)
9. [Troubleshooting](#troubleshooting)
10. [Best Practices](#best-practices)

---

## Overview

Hooks are scripts that execute at specific points in the Claude Code workflow. They enable:

- **Automation**: Automatically format code, run linters, execute tests
- **Security**: Block dangerous operations before they execute
- **Context**: Add project-specific context to prompts
- **Validation**: Verify changes meet quality standards
- **Notifications**: Alert you when tasks complete

### Hook Execution Flow

```
1. Session Start Hook
   ↓
2. User types prompt
   ↓
3. User Prompt Submit Hook (can modify/block prompt)
   ↓
4. Claude processes prompt
   ↓
5. Pre-Tool-Use Hook (before each tool)
   ↓
6. Tool executes (Bash, Write, Edit, etc.)
   ↓
7. Post-Tool-Use Hook (after each tool)
   ↓
8. Claude completes response
   ↓
9. Stop Hook (final validation)
```

### Configuration

Hooks are configured in `.claude/settings.json`:

```json
{
  "hooks": {
    "session-start": ".claude/hooks/session-start.py",
    "user-prompt-submit": ".claude/hooks/user-prompt-submit.py",
    "pre-tool-use": ".claude/hooks/pre-tool-use.py",
    "post-tool-use": ".claude/hooks/post-tool-use.py",
    "stop": ".claude/hooks/stop.py"
  }
}
```

---

## Hook Types

### Available Hooks

| Hook | Trigger | Can Block | Use Case |
|------|---------|-----------|----------|
| **session-start** | Session begins | No | Load project context, display status |
| **user-prompt-submit** | Before prompt sent | Yes | Enhance prompts, add context |
| **pre-tool-use** | Before tool executes | Yes | Security validation, block dangerous ops |
| **post-tool-use** | After tool succeeds | No | Auto-format, lint, test |
| **stop** | Task completion | Yes* | Final validation, notifications |

*Can block but not recommended for stop hook

### Exit Codes

Hooks communicate results via exit codes:

- **0**: Success, continue normally
- **1**: Error (logged but doesn't block)
- **2**: Block operation (prevents tool/prompt execution)

### Input/Output

**Input** (via stdin):
```json
{
  "toolName": "Write",
  "parameters": {
    "file_path": "/path/to/file.js",
    "content": "..."
  },
  "userPrompt": "Create a new API endpoint"
}
```

**Output** (via stdout/stderr):
```json
{
  "decision": "block",
  "reason": "Security violation detected"
}
```

Or plain text for messages:
```
✅ File formatted with prettier
⚠️ 3 linting warnings found
```

---

## Session Start Hook

**File**: `.claude/hooks/session-start.py`

**Trigger**: When Claude Code session begins

**Purpose**: Initialize development environment, display project context

### What It Does

1. **Detects project language** by counting file extensions
2. **Identifies package manager** by looking for marker files
3. **Loads git information**:
   - Current branch
   - Uncommitted files count
   - Recent commits (last 3)
   - Unpushed commits
4. **Displays welcome message** with quick start tips

### Output Example

```
╔══════════════════════════════════════════════════════════════╗
║         Claude Code Session Started                          ║
╚══════════════════════════════════════════════════════════════╝

📁 Project: my-awesome-app
🔧 Language: TypeScript
📦 Package Manager: npm/yarn

🌿 Git Status:
   Branch: feature/new-api
   Uncommitted files: 3
   Unpushed commits: 2

📝 Recent Commits:
   • a1b2c3d feat: add user authentication
   • e4f5g6h fix: resolve CORS issue
   • i7j8k9l docs: update API documentation

💡 Quick Start:
   • /dev:setup   - Install dependencies
   • /quality:test - Run tests
   • /git:commit  - Create commit
   • /quality:review - Code review

⚙️  Hooks Active:
   ✓ Prompt Enhancement
   ✓ Security Validation
   ✓ Auto Quality Checks
   ✓ Final Validation

Ready to code! 🚀
```

### Key Functions

**detect_language()**: Counts files by extension, returns most common
**detect_package_manager()**: Checks for package.json, requirements.txt, etc.
**get_git_info()**: Executes git commands to gather repository status

### Customization

Edit `.claude/hooks/session-start.py` to:
- Add custom environment checks
- Display project-specific reminders
- Check for required tools/dependencies
- Validate configuration files

---

## User Prompt Submit Hook

**File**: `.claude/hooks/user-prompt-submit.py`

**Trigger**: After user submits prompt, before Claude sees it

**Purpose**: Enhance prompts with context, block dangerous requests

### What It Does

1. **Detects vague prompts** and suggests being more specific
2. **Adds error context** from recent log files
3. **Reminds about testing** for implementation requests
4. **Shows git status** for commit-related prompts
5. **Blocks dangerous patterns** (delete everything, drop database)

### Examples

#### Vague Prompt Enhancement

**User types**:
```
fix the bug
```

**Hook adds**:
```
⚠️  Vague request detected. Consider being more specific:
  • What specific functionality needs fixing?
  • What are the expected vs actual behaviors?
  • Are there error messages or symptoms?
```

#### Error Context Injection

**User types**:
```
The tests are failing
```

**Hook adds**:
```
📋 Recent Error Context:
Recent errors from .pytest_cache/v/cache/lastfailed:
  test_api.py::test_authentication - AssertionError
  test_api.py::test_authorization - KeyError: 'user_id'
```

#### Implementation Reminder

**User types**:
```
Add user registration endpoint
```

**Hook adds**:
```
💡 Reminder: Run /quality:test after implementation
```

#### Git Status Context

**User types**:
```
Create a commit
```

**Hook adds**:
```
🌿 Git Status: 5 uncommitted file(s)
   Tip: Use /git:commit for conventional commits
```

### Dangerous Pattern Blocking

**User types**:
```
Delete everything in the database
```

**Hook blocks with**:
```
⛔ Dangerous request detected: Requesting deletion of all files
Please be more specific and cautious.
```

### Key Functions

**enhance_prompt(prompt)**: Adds contextual information
**validate_prompt(prompt)**: Checks for dangerous patterns
**get_recent_errors()**: Reads error logs

### Customization

Add custom enhancements:
```python
# Check for specific project patterns
if 'deploy' in prompt.lower():
    enhancements.append(
        "⚠️  Deployment Request Detected\n"
        "  • Verify staging tests pass\n"
        "  • Check production readiness\n"
        "  • Review rollback plan\n"
    )
```

---

## Pre-Tool-Use Hook

**File**: `.claude/hooks/pre-tool-use.py`

**Trigger**: Before Claude executes any tool (Bash, Write, Edit)

**Purpose**: Security validation, prevent dangerous operations

### What It Does

1. **Validates bash commands** for dangerous patterns
2. **Protects sensitive files** (.env, credentials, keys)
3. **Blocks system directory modifications** (/etc, /bin, etc.)
4. **Logs security events** for audit trail

### Dangerous Command Patterns

The hook blocks:

```bash
rm -rf /              # Recursive delete from root
rm -rf ~              # Delete home directory
rm -rf *              # Delete all files
sudo rm               # Using sudo with rm
chmod 777             # Overly permissive permissions
chmod -R 777          # Recursive dangerous permissions
dd if=...of=/dev/     # Writing to device files
mkfs                  # Filesystem formatting
:(){ :|:& };:         # Fork bomb
curl ... | bash       # Piping remote scripts to shell
wget ... | sh         # Piping downloads to shell
```

### Sensitive File Protection

Protected file patterns:
```
.env
.env.*
*.pem
*.key
*credentials*
*secrets*
id_rsa
id_dsa
*.p12
*.pfx
config.json
```

### Sensitive Directories

Protected system paths:
```
/etc
/bin
/sbin
/usr/bin
/usr/sbin
/var
/boot
/sys
/proc
```

### Example Blocks

#### Dangerous Bash Command

**Claude tries**:
```bash
sudo rm -rf /var/log/*
```

**Hook blocks**:
```
🛡️  SECURITY BLOCK: Using sudo with rm command
Command: sudo rm -rf /var/log/*

This operation has been blocked for safety.
If you need to perform this action, please do it manually.
```

#### Sensitive File Write

**Claude tries**:
```
Write to .env file
```

**Hook blocks**:
```
🛡️  SECURITY BLOCK: Attempting to modify sensitive file
File: /project/.env

Sensitive files like credentials, keys, and .env files
should be modified manually to prevent accidental exposure.
Pattern matched: .env$
```

#### System Directory Modification

**Claude tries**:
```
Edit /etc/hosts
```

**Hook blocks**:
```
🛡️  SECURITY BLOCK: Attempting to modify system directory
Path: /etc/hosts
Protected directory: /etc

System directories should not be modified by AI.
Please perform this operation manually if necessary.
```

### Security Logging

All blocked operations are logged to `.claude/logs/security.log`:

```json
{
  "timestamp": "2025-11-11T10:30:45",
  "event_type": "bash_blocked",
  "details": {
    "command": "rm -rf /",
    "reason": "Attempting to recursively delete from root directory"
  }
}
```

### Key Functions

**check_bash_command(command)**: Validates bash commands
**check_file_operation(tool_name, parameters)**: Validates file writes
**log_security_event(type, details)**: Logs security events

### Customization

Add project-specific protections:
```python
# Protect production deployment files
SENSITIVE_FILES.append(r'deploy\.sh$')
SENSITIVE_FILES.append(r'production\.yaml$')

# Protect database migration files
SENSITIVE_DIRS.append('/database/migrations')
```

---

## Post-Tool-Use Hook

**File**: `.claude/hooks/post-tool-use.py`

**Trigger**: After Write/Edit tools complete successfully

**Purpose**: Automated code formatting and linting

### What It Does

1. **Auto-formats code** using language-specific formatters
2. **Runs linters** to detect code quality issues
3. **Logs quality checks** for audit
4. **Reports results** without blocking

### Supported Formatters

| Language | Formatters (in order of preference) |
|----------|-------------------------------------|
| Python | black, autopep8, yapf |
| JavaScript/TypeScript | prettier |
| JSX/TSX | prettier |
| Rust | rustfmt |
| Go | gofmt, goimports |
| Java | google-java-format |
| Ruby | rubocop -a |
| PHP | php-cs-fixer |
| C/C++ | clang-format |
| Swift | swiftformat |

### Supported Linters

| Language | Linters |
|----------|---------|
| Python | pylint, flake8, mypy |
| JavaScript/TypeScript | eslint |
| Rust | clippy |
| Go | golint, go vet |
| Java | checkstyle |
| Ruby | rubocop |
| PHP | phpcs |

### Example Output

#### Successful Format

```
============================================================
📋 Automated Quality Checks
============================================================
✓ Formatted with prettier
============================================================
```

#### Linting Issues Found

```
============================================================
📋 Automated Quality Checks
============================================================
✓ Formatted with black

⚠️  Linting issues found (pylint):
src/api.py:42:0: C0301: Line too long (105/100) (line-too-long)
src/api.py:67:4: W0612: Unused variable 'result' (unused-variable)
src/api.py:89:0: C0116: Missing function docstring (missing-function-docstring)
============================================================
```

### Tool Detection

The hook automatically detects which tools are installed:
```python
# Checks if formatter is available
which prettier  # Returns true if installed
which black     # Returns true if installed
```

Only uses tools that are actually installed on your system.

### Quality Logging

Actions logged to `.claude/logs/quality.log`:

```json
{
  "timestamp": "2025-11-11T10:35:12",
  "file": "src/api.ts",
  "actions": [
    {
      "tool": "prettier",
      "success": true,
      "message": "✓ Formatted with prettier"
    },
    {
      "linting": [
        {
          "tool": "eslint",
          "output": "src/api.ts:42:10 - Warning: Unused variable 'temp'"
        }
      ]
    }
  ]
}
```

### Key Functions

**format_file(file_path)**: Auto-formats based on extension
**lint_file(file_path)**: Runs linter checks
**check_tool_available(tool_cmd)**: Verifies tool installation

### Customization

Add custom formatters:
```python
# Add support for new language
FORMATTERS['.kt'] = ['ktlint']  # Kotlin
LINTERS['.kt'] = ['ktlint']

# Customize formatter command
def format_file(file_path):
    # ... existing code ...
    if formatter_cmd == 'ktlint':
        cmd = f"ktlint -F {file_path} 2>&1"
```

---

## Stop Hook

**File**: `.claude/hooks/stop.py`

**Trigger**: When Claude Code completes all responses

**Purpose**: Final validation, reminders, notifications

### What It Does

1. **Checks for uncommitted changes**
2. **Scans for TODO/FIXME comments** in modified files
3. **Detects test frameworks** and suggests running tests
4. **Sends desktop notifications** (Linux/macOS)
5. **Logs completion** for audit

### Example Output

```
============================================================
✅ Task Complete - Final Summary
============================================================

📝 5 uncommitted file(s)
   Tip: Use /git:commit when ready

⚠️  Found 3 TODO/FIXME comment(s) in modified files:
   • [TODO] src/api.ts: Add error handling for edge cases
   • [FIXME] src/auth.ts: Temporary workaround, needs proper fix
   • [TODO] tests/api.test.ts: Add tests for new endpoint

💡 Test framework detected
   Run /quality:test to verify changes

============================================================
```

### Desktop Notifications

**Linux (notify-send)**:
```
┌────────────────────────────┐
│ Claude Code                │
│ Task completed!            │
└────────────────────────────┘
```

**macOS (osascript)**:
```
Claude Code
Task completed!
```

### TODO/FIXME Detection

Scans for comment patterns:
```python
# Matches:
# TODO: Fix this later
// FIXME: Temporary hack
/* XXX: This is wrong */
# HACK: Quick fix needed
```

### Test Framework Detection

Automatically detects:
- **Node.js**: package.json with test script
- **Python**: pytest.ini or setup.py
- **Rust**: Cargo.toml
- **Go**: go.mod

### Completion Logging

Logged to `.claude/logs/completion.log`:

```json
{
  "timestamp": "2025-11-11T10:40:22",
  "uncommitted_files": [
    "M src/api.ts",
    "A tests/api.test.ts",
    "M README.md"
  ],
  "todos_found": 3
}
```

### Key Functions

**check_uncommitted_code()**: Gets git status
**scan_for_todos()**: Finds TODO/FIXME comments
**check_tests()**: Detects test frameworks
**send_notification(message)**: Desktop notifications

### Customization

Add custom validations:
```python
# Check for specific patterns
def check_documentation_updated():
    """Ensure docs are updated"""
    result = run_command('git diff --name-only HEAD')
    files = result['stdout'].split('\n')

    # Check if code changed but docs didn't
    code_changed = any(f.endswith(('.py', '.js', '.ts')) for f in files)
    docs_changed = any('docs/' in f or 'README' in f for f in files)

    if code_changed and not docs_changed:
        return "⚠️ Code changed but documentation not updated"

    return None
```

---

## Creating Custom Hooks

### Step 1: Create Hook Script

```bash
# Create new hook
touch .claude/hooks/my-custom-hook.py
chmod +x .claude/hooks/my-custom-hook.py
```

### Step 2: Write Hook Logic

```python
#!/usr/bin/env python3
"""
My Custom Hook - Description
Executes at [trigger point]
"""

import sys
import json

def main():
    """Main hook logic"""
    try:
        # Read input from stdin
        hook_input = json.loads(sys.stdin.read())

        # Your custom logic here
        # ...

        # Output message to user
        print("✅ Custom hook executed successfully")

        # Exit with success
        sys.exit(0)

    except Exception as e:
        # Log error but don't block
        print(f"⚠️ Custom hook error: {str(e)}", file=sys.stderr)
        sys.exit(0)

if __name__ == "__main__":
    main()
```

### Step 3: Register Hook

Edit `.claude/settings.json`:
```json
{
  "hooks": {
    "pre-tool-use": ".claude/hooks/my-custom-hook.py"
  }
}
```

### Hook Template Examples

#### Notification Hook

```python
#!/usr/bin/env python3
import sys
import json
import requests

def send_slack_notification(message):
    """Send message to Slack"""
    webhook_url = os.environ.get('SLACK_WEBHOOK_URL')
    if webhook_url:
        requests.post(webhook_url, json={'text': message})

def main():
    hook_input = json.loads(sys.stdin.read())
    send_slack_notification("Claude Code task started!")
    sys.exit(0)

if __name__ == "__main__":
    main()
```

#### Validation Hook

```python
#!/usr/bin/env python3
import sys
import json
from pathlib import Path

def validate_api_schema():
    """Ensure API schema is valid"""
    schema_file = Path('api/schema.json')
    if schema_file.exists():
        with open(schema_file) as f:
            schema = json.load(f)
            # Validate schema
            if 'version' not in schema:
                return "❌ API schema missing version field"
    return None

def main():
    error = validate_api_schema()
    if error:
        print(json.dumps({'decision': 'block', 'reason': error}))
        sys.exit(2)  # Block
    sys.exit(0)

if __name__ == "__main__":
    main()
```

---

## Troubleshooting

### Hook Not Executing

**Check configuration**:
```bash
cat .claude/settings.json | python3 -m json.tool
```

**Verify hook path**:
```bash
ls -la .claude/hooks/session-start.py
```

**Check permissions**:
```bash
# Make executable
chmod +x .claude/hooks/*.py
```

**Test hook manually**:
```bash
# Session start hook
python3 .claude/hooks/session-start.py

# Hooks with input
echo '{"toolName":"Bash","parameters":{}}' | python3 .claude/hooks/pre-tool-use.py
```

### Hook Failing

**Enable debug mode**:
```bash
export CLAUDE_DEBUG=1
claude
```

**Check Python errors**:
```bash
python3 .claude/hooks/session-start.py
# Look for syntax errors, missing imports
```

**View logs**:
```bash
tail -f .claude/logs/security.log
tail -f .claude/logs/quality.log
```

### Hook Blocking Unexpectedly

**Check exit codes**:
```bash
python3 .claude/hooks/pre-tool-use.py
echo $?  # Should be 0 for success, 2 for block
```

**Review security patterns**:
```python
# In pre-tool-use.py
DANGEROUS_PATTERNS = [...]  # Check if your command matches
SENSITIVE_FILES = [...]     # Check if your file matches
```

**Temporary disable**:
```json
{
  "hooks": {
    "pre-tool-use": ""  // Disable temporarily
  }
}
```

---

## Best Practices

### Do's ✅

1. **Keep hooks fast** - Timeout after 5-10 seconds
2. **Handle errors gracefully** - Use try/except blocks
3. **Log important events** - Write to `.claude/logs/`
4. **Exit with correct codes** - 0 = success, 2 = block
5. **Make hooks executable** - `chmod +x`
6. **Use absolute paths** - For file operations
7. **Validate input** - Check for None/empty values
8. **Provide helpful messages** - Explain why blocked
9. **Test hooks manually** - Before using in Claude
10. **Document custom hooks** - Add comments

### Don'ts ❌

1. **Don't block unnecessarily** - Only for security/critical issues
2. **Don't hang indefinitely** - Always use timeouts
3. **Don't ignore errors** - Log them for debugging
4. **Don't use print() for data** - Use json.dumps() for structured output
5. **Don't hardcode paths** - Use environment variables
6. **Don't modify files directly** - Let tools do modifications
7. **Don't make external calls** - Keep hooks self-contained when possible
8. **Don't commit secrets** - Use environment variables
9. **Don't overcomplicate** - Keep hooks simple and focused
10. **Don't skip testing** - Test edge cases

### Security Considerations

1. **Validate all inputs** from hook_input
2. **Sanitize commands** before execution
3. **Use whitelists** not blacklists when possible
4. **Log security events** for audit trail
5. **Fail safely** - Default to blocking on errors
6. **Review patterns regularly** - Update dangerous patterns
7. **Protect credentials** - Never log API keys
8. **Limit permissions** - Run with minimal privileges
9. **Timeout operations** - Prevent hanging
10. **Test security** - Try to bypass your own hooks

### Performance Tips

1. **Cache results** - Don't recompute expensive operations
2. **Limit file scans** - Only check modified files
3. **Use timeouts** - Prevent slow operations
4. **Parallelize** - Run independent checks concurrently
5. **Skip when possible** - Early exit if nothing to do
6. **Limit output** - Truncate long messages
7. **Use efficient tools** - grep instead of Python parsing
8. **Avoid heavy imports** - Import only what you need
9. **Profile hooks** - Measure execution time
10. **Optimize hot paths** - Focus on frequently run code

---

## Resources

- **Claude Code Hooks Documentation**: https://docs.claude.com/claude-code/hooks
- **Python subprocess**: https://docs.python.org/3/library/subprocess.html
- **JSON in Python**: https://docs.python.org/3/library/json.html
- **Exit Codes**: https://tldp.org/LDP/abs/html/exitcodes.html

---

**Happy Hooking!** ⚡

For more information, see:
- [Setup Guide](SETUP.md)
- [Commands Reference](COMMANDS.md)
- [MCP Servers](MCP_SERVERS.md)
