---
description: Generate or update CHANGELOG based on commits
---

# Generate Changelog

Create or update CHANGELOG.md from commit history following Keep a Changelog format.

## Changelog Format

Follow [Keep a Changelog](https://keepachangelog.com/) specification:

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- New feature X

### Changed
- Improved feature Y

### Fixed
- Bug fix Z

## [1.0.0] - 2025-01-15

### Added
- Initial release
```

## Generation Process

### 1. Determine Version

Check for:
- package.json version
- git tags
- Previous CHANGELOG entries

### 2. Parse Commit History

Since last version/tag:
```bash
git log v1.0.0..HEAD --oneline
```

Or since last changelog update.

### 3. Categorize Commits

By conventional commit type:
- **feat:** → Added
- **fix:** → Fixed
- **docs:** → Documentation
- **refactor:** → Changed
- **perf:** → Changed (performance)
- **test:** → Testing
- **chore:** → Maintenance
- **BREAKING CHANGE:** → Breaking Changes

### 4. Group by Category

```markdown
### Added
- OAuth2 authentication
- User profile management
- Export to PDF feature

### Changed
- Improved database query performance
- Updated UI design

### Fixed
- Session timeout bug
- Memory leak in API client

### Security
- Fixed SQL injection vulnerability
```

### 5. Add Version Header

Format:
```markdown
## [1.1.0] - 2025-01-20

### Added
...
```

## Smart Commit Parsing

Extract meaningful information:
```
feat(auth): add OAuth2 support
  → Added: OAuth2 authentication support

fix(api): resolve timeout issue (#123)
  → Fixed: API timeout issue (#123)

refactor: improve code structure
  → Changed: Improved code structure
```

## Unreleased Section

Maintain `## [Unreleased]` section for:
- Commits since last release
- Work in progress
- Planned features

## Version Bump Suggestions

Based on changes:
- **Major (2.0.0)**: Breaking changes present
- **Minor (1.1.0)**: New features added
- **Patch (1.0.1)**: Only bug fixes

## Link Generation

Add comparison links at bottom:
```markdown
[Unreleased]: https://github.com/user/repo/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/user/repo/releases/tag/v1.0.0
```

## Integration with Releases

If preparing release:
1. Move Unreleased to new version
2. Add version number and date
3. Create new empty Unreleased section
4. Suggest creating git tag

## Output Example

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📝 CHANGELOG UPDATED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Analyzed 23 commits since v1.0.0

Changes categorized:
  • Added: 5 features
  • Changed: 3 improvements
  • Fixed: 7 bugs
  • Security: 1 fix

Suggested version: 1.1.0 (minor)

Next steps:
  1. Review CHANGELOG.md
  2. Update package.json version
  3. Create git tag: git tag v1.1.0
  4. Create release on GitHub

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Arguments

- `/docs:changelog` - Update with unreleased changes
- `/docs:changelog 1.1.0` - Create new version entry
- `/docs:changelog --since v1.0.0` - From specific version
- `/docs:changelog --draft` - Preview without saving

**IMPORTANT**: Group related changes together. Be concise but descriptive.
