#!/usr/bin/env python3
"""
Notification Hook - Desktop Notifications
Executes when Claude Code sends notifications.
Provides visual/audio feedback for important events.
"""

import sys
import json
import subprocess

def run_command(cmd, timeout=5):
    """Execute command safely"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return result.returncode == 0
    except Exception:
        return False

def send_notification(title, message, urgency='normal'):
    """Send desktop notification using available system"""

    # Escape special characters
    title = title.replace('"', '\\"').replace("'", "\\'")
    message = message.replace('"', '\\"').replace("'", "\\'")

    # Try notify-send (Linux)
    if run_command('which notify-send 2>/dev/null'):
        cmd = f'notify-send -u {urgency} "{title}" "{message}"'
        if run_command(cmd):
            return True

    # Try osascript (macOS)
    if run_command('which osascript 2>/dev/null'):
        cmd = f'osascript -e \'display notification "{message}" with title "{title}"\''
        if run_command(cmd):
            return True

    # Try terminal-notifier (macOS alternative)
    if run_command('which terminal-notifier 2>/dev/null'):
        cmd = f'terminal-notifier -title "{title}" -message "{message}"'
        if run_command(cmd):
            return True

    return False

def play_sound():
    """Play notification sound if available"""
    # Try different sound players
    sound_commands = [
        'paplay /usr/share/sounds/freedesktop/stereo/complete.oga 2>/dev/null',  # Linux
        'afplay /System/Library/Sounds/Glass.aiff 2>/dev/null',  # macOS
        'powershell -c (New-Object Media.SoundPlayer "/Windows/Media/notify.wav").PlaySync() 2>/dev/null',  # Windows
    ]

    for cmd in sound_commands:
        if run_command(cmd, timeout=2):
            return True

    return False

def main():
    """Main notification hook"""
    try:
        # Read hook input
        hook_input = json.loads(sys.stdin.read())

        notification_type = hook_input.get('notificationType', 'info')
        message = hook_input.get('message', 'Claude Code notification')

        # Determine urgency and title
        if notification_type == 'permission':
            title = '🔐 Claude Code - Permission Required'
            urgency = 'critical'
        elif notification_type == 'error':
            title = '❌ Claude Code - Error'
            urgency = 'critical'
        elif notification_type == 'warning':
            title = '⚠️  Claude Code - Warning'
            urgency = 'normal'
        else:
            title = '💡 Claude Code - Info'
            urgency = 'low'

        # Send notification
        success = send_notification(title, message[:200], urgency)

        # Play sound for important notifications
        if notification_type in ['permission', 'error'] and success:
            play_sound()

        # Log notification
        from pathlib import Path
        from datetime import datetime

        log_dir = Path('.claude/logs')
        log_dir.mkdir(parents=True, exist_ok=True)

        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'type': notification_type,
            'message': message,
            'sent': success
        }

        with open(log_dir / 'notifications.log', 'a') as f:
            f.write(json.dumps(log_entry) + '\n')

        sys.exit(0)

    except json.JSONDecodeError:
        sys.exit(0)
    except Exception as e:
        print(f"⚠️  Notification hook error: {str(e)}", file=sys.stderr)
        sys.exit(0)

if __name__ == "__main__":
    main()
