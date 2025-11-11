#!/usr/bin/env python3
"""
SessionStart Hook - Initialize Development Environment
Executes when a new Claude Code session starts.
Provides project context, git status, and environment information.
"""

import subprocess
import sys
import json
from pathlib import Path
from datetime import datetime

def run_command(cmd):
    """Execute shell command and return output"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout.strip() if result.returncode == 0 else None
    except Exception:
        return None

def detect_language():
    """Detect primary programming language"""
    extensions = {
        '.py': 'Python',
        '.js': 'JavaScript',
        '.ts': 'TypeScript',
        '.rs': 'Rust',
        '.go': 'Go',
        '.java': 'Java',
        '.rb': 'Ruby',
        '.php': 'PHP',
        '.cpp': 'C++',
        '.c': 'C',
        '.cs': 'C#',
        '.swift': 'Swift',
        '.kt': 'Kotlin'
    }

    try:
        # Count files by extension
        counts = {}
        for ext, lang in extensions.items():
            result = run_command(f"find . -type f -name '*{ext}' | wc -l")
            if result:
                count = int(result)
                if count > 0:
                    counts[lang] = count

        if counts:
            return max(counts.items(), key=lambda x: x[1])[0]
    except Exception:
        pass

    return "Unknown"

def detect_package_manager():
    """Detect package manager"""
    managers = {
        'package.json': 'npm/yarn',
        'requirements.txt': 'pip',
        'Cargo.toml': 'cargo',
        'go.mod': 'go modules',
        'pom.xml': 'maven',
        'build.gradle': 'gradle',
        'Gemfile': 'bundler',
        'composer.json': 'composer'
    }

    for file, manager in managers.items():
        if Path(file).exists():
            return manager

    return "Unknown"

def get_git_info():
    """Get git repository information"""
    info = {}

    # Current branch
    branch = run_command("git rev-parse --abbrev-ref HEAD 2>/dev/null")
    info['branch'] = branch if branch else "Not a git repository"

    # Uncommitted changes
    status = run_command("git status --short 2>/dev/null")
    info['uncommitted'] = len(status.split('\n')) if status else 0

    # Recent commits (last 3)
    commits = run_command("git log -3 --oneline 2>/dev/null")
    info['recent_commits'] = commits.split('\n') if commits else []

    # Unpushed commits
    unpushed = run_command("git log @{u}.. --oneline 2>/dev/null")
    info['unpushed'] = len(unpushed.split('\n')) if unpushed else 0

    return info

def main():
    """Main session start hook"""
    output = {
        "timestamp": datetime.now().isoformat(),
        "project": Path.cwd().name,
        "language": detect_language(),
        "package_manager": detect_package_manager(),
        "git": get_git_info()
    }

    # Build informative message
    msg = f"""
╔══════════════════════════════════════════════════════════════╗
║         Claude Code Session Started                          ║
╚══════════════════════════════════════════════════════════════╝

📁 Project: {output['project']}
🔧 Language: {output['language']}
📦 Package Manager: {output['package_manager']}

🌿 Git Status:
   Branch: {output['git']['branch']}
   Uncommitted files: {output['git']['uncommitted']}
   Unpushed commits: {output['git']['unpushed']}

📝 Recent Commits:
"""

    for commit in output['git']['recent_commits'][:3]:
        msg += f"   • {commit}\n"

    msg += """
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
"""

    print(msg)

    # Exit with success
    sys.exit(0)

if __name__ == "__main__":
    main()
