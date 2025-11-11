#!/usr/bin/env python3
"""
Stop Hook - Final Validation
Executes when Claude Code completes all responses.
Performs final checks, validation, and sends completion notifications.
"""

import sys
import json
import subprocess
import re
from pathlib import Path
from datetime import datetime

def run_command(cmd, timeout=30):
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
            'stderr': result.stderr
        }
    except Exception as e:
        return {'success': False, 'error': str(e)}

def check_tests():
    """Check if tests are passing"""
    test_commands = [
        ('package.json', 'npm test -- --passWithNoTests 2>&1'),
        ('pytest.ini', 'pytest --collect-only -q 2>&1'),
        ('setup.py', 'python -m pytest --collect-only -q 2>&1'),
        ('Cargo.toml', 'cargo test --no-run 2>&1'),
        ('go.mod', 'go test -run NONE ./... 2>&1'),
    ]

    for marker_file, test_cmd in test_commands:
        if Path(marker_file).exists():
            # Check if tests exist
            result = run_command(test_cmd)
            return {
                'framework_detected': True,
                'command': test_cmd,
                'result': result
            }

    return {'framework_detected': False}

def check_uncommitted_code():
    """Check for uncommitted changes"""
    result = run_command('git status --short 2>/dev/null', timeout=5)
    if result.get('success'):
        lines = result['stdout'].strip().split('\n')
        return {
            'has_changes': len(lines) > 0 and lines[0] != '',
            'files': lines
        }
    return None

def scan_for_todos():
    """Scan for TODO/FIXME comments in recent changes"""
    # Get files changed in working directory
    result = run_command(
        "git diff --name-only HEAD 2>/dev/null || find . -name '*.py' -o -name '*.js' -o -name '*.ts' -o -name '*.go' -o -name '*.rs' | head -20",
        timeout=10
    )

    if not result.get('success'):
        return None

    files = result['stdout'].strip().split('\n')
    todos = []

    for file_path in files[:10]:  # Limit to 10 files
        if not file_path or not Path(file_path).exists():
            continue

        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                # Find TODO/FIXME comments
                matches = re.finditer(
                    r'(//|#|/\*|\*)\s*(TODO|FIXME|HACK|XXX):?\s*(.+)',
                    content,
                    re.IGNORECASE
                )
                for match in matches:
                    todos.append({
                        'file': file_path,
                        'type': match.group(2).upper(),
                        'comment': match.group(3).strip()[:100]
                    })
        except Exception:
            pass

    return todos if todos else None

def send_notification(message):
    """Send desktop notification if available"""
    # Try notify-send (Linux)
    if run_command('which notify-send 2>/dev/null', timeout=2).get('success'):
        run_command(f"notify-send 'Claude Code' '{message}'", timeout=5)
        return True

    # Try osascript (macOS)
    if run_command('which osascript 2>/dev/null', timeout=2).get('success'):
        escaped = message.replace("'", "\\'")
        run_command(f"osascript -e 'display notification \"{escaped}\" with title \"Claude Code\"'", timeout=5)
        return True

    return False

def main():
    """Main stop hook"""
    try:
        # Read hook input
        hook_input = json.loads(sys.stdin.read())

        messages = []
        warnings = []
        should_block = False

        # Check for uncommitted changes
        git_status = check_uncommitted_code()
        if git_status and git_status['has_changes']:
            file_count = len(git_status['files'])
            messages.append(
                f"📝 {file_count} uncommitted file(s)\n"
                f"   Tip: Use /git:commit when ready"
            )

        # Scan for TODOs
        todos = scan_for_todos()
        if todos:
            messages.append(
                f"⚠️  Found {len(todos)} TODO/FIXME comment(s) in modified files:"
            )
            for todo in todos[:3]:  # Show first 3
                messages.append(
                    f"   • [{todo['type']}] {todo['file']}: {todo['comment']}"
                )
            if len(todos) > 3:
                messages.append(f"   ... and {len(todos) - 3} more")

        # Check tests (optional, non-blocking)
        test_status = check_tests()
        if test_status.get('framework_detected'):
            messages.append(
                "💡 Test framework detected\n"
                "   Run /quality:test to verify changes"
            )

        # Build final output
        if messages or warnings:
            output = "\n" + "="*60 + "\n"
            output += "✅ Task Complete - Final Summary\n"
            output += "="*60 + "\n\n"
            output += "\n\n".join(messages + warnings)
            output += "\n" + "="*60 + "\n"
            print(output)

            # Send desktop notification
            send_notification("Claude Code task completed!")

        # Log completion
        log_dir = Path('.claude/logs')
        log_dir.mkdir(parents=True, exist_ok=True)

        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'uncommitted_files': git_status.get('files', []) if git_status else [],
            'todos_found': len(todos) if todos else 0,
        }

        with open(log_dir / 'completion.log', 'a') as f:
            f.write(json.dumps(log_entry) + '\n')

        # Block if critical issues (none by default)
        if should_block:
            sys.exit(2)

        sys.exit(0)

    except json.JSONDecodeError:
        sys.exit(0)
    except Exception as e:
        print(f"⚠️  Stop hook error: {str(e)}", file=sys.stderr)
        sys.exit(0)

if __name__ == "__main__":
    main()
