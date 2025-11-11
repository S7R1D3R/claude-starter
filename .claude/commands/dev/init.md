---
description: Initialize a new project with auto-detected language and framework
---

# Initialize New Project

You are helping initialize a new project. Follow these steps:

## 1. Detect Project Type

Analyze the current directory to determine:
- Primary programming language (check file extensions)
- Build tool/package manager (package.json, requirements.txt, Cargo.toml, etc.)
- Framework (React, Django, Rails, etc.)
- Testing framework

## 2. Create Standard Structure

Based on the detected type, create a standard project structure:
- Source directory (src/, lib/, app/, etc.)
- Test directory (tests/, test/, spec/, etc.)
- Documentation directory (docs/)
- Configuration files

## 3. Initialize Tools

Set up appropriate tools:
- Version control (git init if not exists)
- Package manager initialization
- Linter/formatter configuration
- CI/CD templates

## 4. Generate Essential Files

Create:
- README.md with project overview
- .gitignore for the specific language
- License file (MIT by default)
- Configuration files for tools

## 5. Provide Next Steps

After initialization, tell the user:
- How to install dependencies (/dev:setup)
- How to run tests (/quality:test)
- How to start development server (/dev:serve)
- Any additional setup needed

**IMPORTANT**: Be language-agnostic. Adapt all recommendations to the detected project type.
