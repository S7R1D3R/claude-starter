#!/usr/bin/env python3
"""
PreToolUse Hook - Security Validation
Executes before Claude uses tools like Bash, Write, or Edit.
Blocks dangerous operations and validates file paths.
"""

import sys
import json
import re
from pathlib import Path
from datetime import datetime

# Dangerous command patterns
DANGEROUS_PATTERNS = [
    (r'rm\s+-rf\s+/', 'Attempting to recursively delete from root directory'),
    (r'rm\s+-rf\s+~', 'Attempting to delete home directory'),
    (r'rm\s+-rf\s+\*', 'Attempting to delete all files recursively'),
    (r'sudo\s+rm', 'Using sudo with rm command'),
    (r'chmod\s+777', 'Setting overly permissive file permissions'),
    (r'chmod\s+-R\s+777', 'Recursively setting dangerous permissions'),
    (r'dd\s+if=.*of=/dev/', 'Attempting to write to device file'),
    (r'mkfs', 'Attempting to format filesystem'),
    (r':(){ :|:& };:', 'Fork bomb detected'),
    (r'curl.*\|\s*bash', 'Piping remote script directly to bash'),
    (r'wget.*\|\s*sh', 'Piping remote script directly to shell'),
]

# Sensitive file patterns
SENSITIVE_FILES = [
    r'\.env$',
    r'\.env\..*',
    r'.*\.pem$',
    r'.*\.key$',
    r'.*credentials.*',
    r'.*secrets.*',
    r'id_rsa',
    r'id_dsa',
    r'.*\.p12$',
    r'.*\.pfx$',
    r'config\.json',
]

# Sensitive directories
SENSITIVE_DIRS = [
    '/etc',
    '/bin',
    '/sbin',
    '/usr/bin',
    '/usr/sbin',
    '/var',
    '/boot',
    '/sys',
    '/proc',
]

def log_security_event(event_type, details):
    """Log security events for audit trail"""
    log_dir = Path('.claude/logs')
    log_dir.mkdir(parents=True, exist_ok=True)

    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'event_type': event_type,
        'details': details
    }

    log_file = log_dir / 'security.log'
    with open(log_file, 'a') as f:
        f.write(json.dumps(log_entry) + '\n')

def check_bash_command(command):
    """Validate bash commands for dangerous patterns"""
    for pattern, reason in DANGEROUS_PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            return {
                'decision': 'block',
                'reason': f'🛡️  SECURITY BLOCK: {reason}\n'
                         f'Command: {command}\n\n'
                         f'This operation has been blocked for safety.\n'
                         f'If you need to perform this action, please do it manually.'
            }
    return None

def check_file_operation(tool_name, parameters):
    """Validate file write/edit operations"""
    file_path = parameters.get('file_path', '')

    if not file_path:
        return None

    path = Path(file_path)

    # Check for sensitive files
    for pattern in SENSITIVE_FILES:
        if re.search(pattern, str(path), re.IGNORECASE):
            return {
                'decision': 'block',
                'reason': f'🛡️  SECURITY BLOCK: Attempting to modify sensitive file\n'
                         f'File: {file_path}\n\n'
                         f'Sensitive files like credentials, keys, and .env files\n'
                         f'should be modified manually to prevent accidental exposure.\n'
                         f'Pattern matched: {pattern}'
            }

    # Check for sensitive directories
    try:
        abs_path = path.resolve()
        for sensitive_dir in SENSITIVE_DIRS:
            if str(abs_path).startswith(sensitive_dir):
                return {
                    'decision': 'block',
                    'reason': f'🛡️  SECURITY BLOCK: Attempting to modify system directory\n'
                             f'Path: {abs_path}\n'
                             f'Protected directory: {sensitive_dir}\n\n'
                             f'System directories should not be modified by AI.\n'
                             f'Please perform this operation manually if necessary.'
                }
    except Exception:
        pass

    return None

def main():
    """Main pre-tool-use hook"""
    try:
        # Read hook input
        hook_input = json.loads(sys.stdin.read())

        tool_name = hook_input.get('toolName', '')
        parameters = hook_input.get('parameters', {})

        # Validate based on tool type
        if tool_name == 'Bash':
            command = parameters.get('command', '')
            validation = check_bash_command(command)

            if validation:
                log_security_event('bash_blocked', {
                    'command': command,
                    'reason': validation['reason']
                })
                print(json.dumps(validation))
                sys.exit(2)  # Block with error

        elif tool_name in ['Write', 'Edit']:
            validation = check_file_operation(tool_name, parameters)

            if validation:
                log_security_event('file_blocked', {
                    'tool': tool_name,
                    'file': parameters.get('file_path', ''),
                    'reason': validation['reason']
                })
                print(json.dumps(validation))
                sys.exit(2)  # Block with error

        # All checks passed
        sys.exit(0)

    except json.JSONDecodeError:
        # Invalid input, allow to continue
        sys.exit(0)
    except Exception as e:
        # Log error but don't block
        print(f"⚠️  Security hook error: {str(e)}", file=sys.stderr)
        sys.exit(0)

if __name__ == "__main__":
    main()
