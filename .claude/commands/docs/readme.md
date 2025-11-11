---
description: Update README.md based on recent changes and project state
---

# Update README

Intelligently update the README.md file based on project changes and current state.

## README Structure Analysis

Standard sections to maintain:
1. **Project Title & Description**
2. **Badges** (build status, coverage, version)
3. **Features**
4. **Installation**
5. **Usage/Quick Start**
6. **API Documentation**
7. **Configuration**
8. **Development**
9. **Testing**
10. **Contributing**
11. **License**

## Update Process

### 1. Analyze Recent Changes
```bash
git log --since="1 week ago" --oneline
git diff HEAD~10 --stat
```

Identify:
- New features added
- Dependencies changed
- API changes
- Configuration changes
- New scripts added

### 2. Check Current Project State

Scan for:
- **Dependencies**: Read package.json, requirements.txt, etc.
- **Scripts**: Available npm/yarn scripts
- **Configuration**: Environment variables needed
- **Entry points**: Main files, commands
- **Features**: Analyze code structure

### 3. Update Relevant Sections

#### Installation Section
- Update if dependencies changed
- Add new environment requirements
- Update setup steps

#### Usage Section
- Add examples for new features
- Update CLI commands
- Add code snippets

#### API Documentation
- Update if public APIs changed
- Add new endpoints/methods
- Update examples

#### Configuration
- Add new environment variables
- Update configuration options
- Show example .env file

### 4. Add Missing Sections

If README is incomplete, add:
- **Features** list with checkmarks
- **Screenshots** placeholder (if applicable)
- **Architecture** overview
- **Deployment** guide
- **Troubleshooting** section

### 5. Improve Content Quality

Enhance:
- Make installation steps clearer
- Add more usage examples
- Improve formatting
- Add emojis for visual appeal (optional)
- Fix typos and grammar

## Template for Missing README

If no README exists, generate from this template:

```markdown
# Project Name

Brief description of what this project does.

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

\`\`\`bash
# Commands to install
\`\`\`

## Usage

\`\`\`bash
# Commands to run
\`\`\`

## Configuration

Environment variables and configuration options.

## Development

How to set up development environment.

## Testing

\`\`\`bash
# Command to run tests
\`\`\`

## Contributing

Guidelines for contributing.

## License

MIT License
```

## Quality Checks

After updating:
- [ ] All code examples are valid
- [ ] Links are not broken
- [ ] Badges are current
- [ ] Installation steps work
- [ ] Examples match current API

## Changelog Integration

If CHANGELOG.md exists, sync recent changes:
- Extract latest version changes
- Summarize in README
- Link to full CHANGELOG

## Arguments

- `/docs:readme` - Smart update based on changes
- `/docs:readme --full` - Complete rewrite
- `/docs:readme --check` - Check README quality without updating

**IMPORTANT**: Preserve existing content. Only update what's necessary based on actual code changes.
