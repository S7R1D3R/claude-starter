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
    """Detect primary programming language (optimized with caching)"""
    # Check cache first (valid for 1 hour)
    cache_file = Path('.claude/.cache/language-detect.json')
    cache_file.parent.mkdir(parents=True, exist_ok=True)

    try:
        if cache_file.exists():
            import time
            cache_age = time.time() - cache_file.stat().st_mtime
            if cache_age < 3600:  # 1 hour
                with open(cache_file, 'r') as f:
                    return json.load(f)['language']
    except Exception:
        pass

    # Fast config-based detection first
    config_hints = {
        'package.json': 'JavaScript',
        'tsconfig.json': 'TypeScript',
        'Cargo.toml': 'Rust',
        'go.mod': 'Go',
        'pom.xml': 'Java',
        'build.gradle': 'Java',
        'requirements.txt': 'Python',
        'pyproject.toml': 'Python',
        'Gemfile': 'Ruby',
        'composer.json': 'PHP',
    }

    for config, lang in config_hints.items():
        if Path(config).exists():
            # Cache result
            try:
                with open(cache_file, 'w') as f:
                    json.dump({'language': lang}, f)
            except Exception:
                pass
            return lang

    # Fallback: optimized file counting (single find command with exclusions)
    try:
        # Exclude common directories
        exclude_dirs = [
            'node_modules', '.git', 'venv', '.venv', 'env', '.env',
            'target', 'build', 'dist', '__pycache__', '.cache',
            'vendor', '.idea', '.vscode', 'coverage'
        ]

        exclude_pattern = ' '.join([f"-path '*/{d}' -prune -o" for d in exclude_dirs])

        # Single find command for common extensions
        find_cmd = f"find . {exclude_pattern} -type f \\( -name '*.py' -o -name '*.js' -o -name '*.ts' -o -name '*.rs' -o -name '*.go' -o -name '*.java' \\) -print"
        result = run_command(find_cmd)

        if result:
            # Count by extension
            counts = {}
            ext_map = {
                '.py': 'Python', '.js': 'JavaScript', '.ts': 'TypeScript',
                '.rs': 'Rust', '.go': 'Go', '.java': 'Java'
            }

            for line in result.split('\n'):
                for ext, lang in ext_map.items():
                    if line.endswith(ext):
                        counts[lang] = counts.get(lang, 0) + 1
                        break

            if counts:
                detected = max(counts.items(), key=lambda x: x[1])[0]
                # Cache result
                try:
                    with open(cache_file, 'w') as f:
                        json.dump({'language': detected, 'counts': counts}, f)
                except Exception:
                    pass
                return detected
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
