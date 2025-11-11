#!/usr/bin/env python3
"""
UserPromptSubmit Hook - Enhance User Prompts
Executes before user prompts are sent to Claude.
Can modify prompts to add context, enforce standards, or block invalid requests.
"""

import sys
import json
import subprocess
import os
from pathlib import Path

def run_command(cmd):
    """Execute shell command safely"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=3
        )
        return result.stdout.strip() if result.returncode == 0 else None
    except Exception:
        return None

def get_recent_errors():
    """Check for recent error logs"""
    log_files = [
        'error.log',
        'npm-debug.log',
        'yarn-error.log',
        '.pytest_cache/v/cache/lastfailed'
    ]

    errors = []
    for log_file in log_files:
        if Path(log_file).exists():
            try:
                # Get last few lines
                content = run_command(f"tail -n 5 {log_file} 2>/dev/null")
                if content:
                    errors.append(f"Recent errors from {log_file}:\n{content}")
            except Exception:
                pass

    return "\n\n".join(errors) if errors else None

def enhance_prompt(prompt):
    """Enhance user prompt with context"""
    enhancements = []

    # Check if prompt is vague
    vague_indicators = ['fix', 'improve', 'make better', 'optimize', 'enhance']
    if any(word in prompt.lower() for word in vague_indicators) and len(prompt.split()) < 10:
        enhancements.append(
            "⚠️  Vague request detected. Consider being more specific:\n"
            "  • What specific functionality needs fixing?\n"
            "  • What are the expected vs actual behaviors?\n"
            "  • Are there error messages or symptoms?\n"
        )

    # Add error context if available
    errors = get_recent_errors()
    if errors and any(word in prompt.lower() for word in ['error', 'fail', 'bug', 'broken']):
        enhancements.append(f"📋 Recent Error Context:\n{errors}\n")

    # Remind about testing for implementation requests
    impl_keywords = ['add', 'create', 'implement', 'build', 'write']
    if any(word in prompt.lower() for word in impl_keywords):
        enhancements.append(
            "💡 Reminder: Run /quality:test after implementation\n"
        )

    # Check git status for commit-related prompts
    if any(word in prompt.lower() for word in ['commit', 'push', 'pr', 'pull request']):
        status = run_command("git status --short 2>/dev/null")
        if status:
            uncommitted = len(status.split('\n'))
            enhancements.append(
                f"🌿 Git Status: {uncommitted} uncommitted file(s)\n"
                f"   Tip: Use /git:commit for conventional commits\n"
            )

    return "\n".join(enhancements) if enhancements else None

def validate_prompt(prompt):
    """Validate prompt for dangerous patterns"""
    dangerous_patterns = [
        ('delete everything', 'Requesting deletion of all files'),
        ('remove all', 'Requesting bulk deletion'),
        ('drop database', 'Requesting database deletion'),
        ('format disk', 'Requesting disk formatting'),
    ]

    for pattern, reason in dangerous_patterns:
        if pattern in prompt.lower():
            return {
                "decision": "block",
                "reason": f"⛔ Dangerous request detected: {reason}\n"
                         f"Please be more specific and cautious."
            }

    return None

def main():
    """Main user prompt submit hook"""
    try:
        # Read hook input from stdin
        hook_input = json.loads(sys.stdin.read())
        prompt = hook_input.get('userPrompt', '')

        if not prompt:
            # No prompt to process
            sys.exit(0)

        # Validate for dangerous patterns
        validation = validate_prompt(prompt)
        if validation:
            # Block dangerous prompts
            output = {
                "decision": "block",
                "reason": validation["reason"]
            }
            print(json.dumps(output))
            sys.exit(2)  # Exit code 2 blocks the prompt

        # Enhance prompt with context
        enhancement = enhance_prompt(prompt)
        if enhancement:
            # Print enhancement to add context
            # This will be visible in transcript mode
            print(enhancement)

        # Allow prompt to continue
        sys.exit(0)

    except json.JSONDecodeError:
        # Invalid JSON input, skip hook
        sys.exit(0)
    except Exception as e:
        # Log error but don't block
        print(f"⚠️  Hook error: {str(e)}", file=sys.stderr)
        sys.exit(0)

if __name__ == "__main__":
    main()
