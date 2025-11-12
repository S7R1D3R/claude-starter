#!/usr/bin/env python3
"""
PostToolUse Hook - Automated Quality Checks
Executes after Write/Edit tools complete successfully.
Auto-formats code, runs linters, and executes relevant tests.
"""

import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime

# Cache for tool availability (persists during hook execution)
_TOOL_CACHE = {}

# Language-specific tools configuration
FORMATTERS = {
    '.py': ['black', 'autopep8', 'yapf'],
    '.js': ['prettier'],
    '.ts': ['prettier'],
    '.jsx': ['prettier'],
    '.tsx': ['prettier'],
    '.rs': ['rustfmt'],
    '.go': ['gofmt', 'goimports'],
    '.java': ['google-java-format'],
    '.rb': ['rubocop -a'],
    '.php': ['php-cs-fixer'],
    '.c': ['clang-format'],
    '.cpp': ['clang-format'],
    '.h': ['clang-format'],
    '.swift': ['swiftformat'],
}

LINTERS = {
    '.py': ['pylint', 'flake8', 'mypy'],
    '.js': ['eslint'],
    '.ts': ['eslint'],
    '.jsx': ['eslint'],
    '.tsx': ['eslint'],
    '.rs': ['clippy'],
    '.go': ['golint', 'go vet'],
    '.java': ['checkstyle'],
    '.rb': ['rubocop'],
    '.php': ['phpcs'],
}

def run_command(cmd, timeout=10):
    """Execute command and return result"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return {
            'success': result.returncode == 0,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'returncode': result.returncode
        }
    except subprocess.TimeoutExpired:
        return {'success': False, 'error': 'Command timed out'}
    except Exception as e:
        return {'success': False, 'error': str(e)}

def check_tool_available(tool_cmd):
    """Check if a tool is installed (with caching)"""
    tool_name = tool_cmd.split()[0]

    # Check cache first
    if tool_name in _TOOL_CACHE:
        return _TOOL_CACHE[tool_name]

    # Check tool availability
    result = run_command(f"which {tool_name} 2>/dev/null", timeout=2)
    is_available = result.get('success', False)

    # Cache result
    _TOOL_CACHE[tool_name] = is_available

    return is_available

def format_file(file_path):
    """Auto-format file based on extension"""
    path = Path(file_path)
    ext = path.suffix

    if ext not in FORMATTERS:
        return None

    # Try formatters in order of preference
    for formatter_cmd in FORMATTERS[ext]:
        if not check_tool_available(formatter_cmd):
            continue

        # Build format command
        if formatter_cmd == 'black':
            cmd = f"black {file_path} 2>&1"
        elif formatter_cmd == 'prettier':
            cmd = f"prettier --write {file_path} 2>&1"
        elif formatter_cmd == 'rustfmt':
            cmd = f"rustfmt {file_path} 2>&1"
        elif formatter_cmd == 'gofmt':
            cmd = f"gofmt -w {file_path} 2>&1"
        elif formatter_cmd == 'goimports':
            cmd = f"goimports -w {file_path} 2>&1"
        else:
            cmd = f"{formatter_cmd} {file_path} 2>&1"

        result = run_command(cmd)
        if result['success']:
            return {
                'tool': formatter_cmd,
                'success': True,
                'message': f'✓ Formatted with {formatter_cmd}'
            }

    return None

def lint_file(file_path):
    """Run linter on file"""
    path = Path(file_path)
    ext = path.suffix

    if ext not in LINTERS:
        return None

    issues = []

    # Try linters
    for linter_cmd in LINTERS[ext]:
        if not check_tool_available(linter_cmd):
            continue

        # Build lint command
        if linter_cmd == 'pylint':
            cmd = f"pylint {file_path} 2>&1"
        elif linter_cmd == 'eslint':
            cmd = f"eslint {file_path} 2>&1"
        elif linter_cmd == 'clippy':
            cmd = f"cargo clippy -- {file_path} 2>&1"
        elif linter_cmd == 'go vet':
            cmd = f"go vet {file_path} 2>&1"
        else:
            cmd = f"{linter_cmd} {file_path} 2>&1"

        result = run_command(cmd, timeout=15)

        if not result['success'] and result.get('stdout'):
            # Found linting issues
            issues.append({
                'tool': linter_cmd,
                'output': result['stdout'][:500]  # Limit output
            })
            break  # Only report from first linter

    return issues if issues else None

def log_quality_check(file_path, actions):
    """Log quality check actions"""
    log_dir = Path('.claude/logs')
    log_dir.mkdir(parents=True, exist_ok=True)

    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'file': file_path,
        'actions': actions
    }

    log_file = log_dir / 'quality.log'
    with open(log_file, 'a') as f:
        f.write(json.dumps(log_entry) + '\n')

def main():
    """Main post-tool-use hook"""
    try:
        # Read hook input
        hook_input = json.loads(sys.stdin.read())

        tool_name = hook_input.get('toolName', '')
        parameters = hook_input.get('parameters', {})

        # Only process Write/Edit tools
        if tool_name not in ['Write', 'Edit']:
            sys.exit(0)

        file_path = parameters.get('file_path', '')
        if not file_path or not Path(file_path).exists():
            sys.exit(0)

        actions = []
        messages = []

        # Auto-format
        format_result = format_file(file_path)
        if format_result:
            actions.append(format_result)
            messages.append(format_result['message'])

        # Lint check
        lint_result = lint_file(file_path)
        if lint_result:
            actions.append({'linting': lint_result})
            for issue in lint_result:
                messages.append(
                    f"⚠️  Linting issues found ({issue['tool']}):\n"
                    f"{issue['output']}"
                )

        # Log actions
        if actions:
            log_quality_check(file_path, actions)

        # Output messages
        if messages:
            output_msg = '\n\n'.join(messages)
            print(f"\n{'='*60}")
            print("📋 Automated Quality Checks")
            print('='*60)
            print(output_msg)
            print('='*60)

        # Always exit with success (non-blocking)
        sys.exit(0)

    except json.JSONDecodeError:
        sys.exit(0)
    except Exception as e:
        print(f"⚠️  Quality hook error: {str(e)}", file=sys.stderr)
        sys.exit(0)

if __name__ == "__main__":
    main()
