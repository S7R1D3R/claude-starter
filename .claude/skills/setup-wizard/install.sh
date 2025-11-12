#!/bin/bash

# Setup Wizard Skill Installation Script
# Installs the setup-wizard skill to ~/.claude/skills/

set -e  # Exit on error

SKILL_NAME="setup-wizard"
SKILL_SOURCE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_SKILLS_DIR="${HOME}/.claude/skills"
SKILL_DEST="${CLAUDE_SKILLS_DIR}/${SKILL_NAME}"

echo "🧙 Setup Wizard Skill Installer"
echo "================================"
echo ""

# Create skills directory if it doesn't exist
if [ ! -d "${CLAUDE_SKILLS_DIR}" ]; then
    echo "📁 Creating Claude skills directory..."
    mkdir -p "${CLAUDE_SKILLS_DIR}"
fi

# Check if skill already exists
if [ -L "${SKILL_DEST}" ] || [ -d "${SKILL_DEST}" ]; then
    echo "⚠️  Setup Wizard skill already exists at ${SKILL_DEST}"
    echo ""
    read -p "Do you want to update it? (y/n) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "❌ Installation cancelled"
        exit 0
    fi

    echo "🗑️  Removing existing installation..."
    rm -rf "${SKILL_DEST}"
fi

# Ask user about installation method
echo ""
echo "Installation options:"
echo "1. Symlink (recommended - auto-updates when project updates)"
echo "2. Copy (standalone - manual updates required)"
echo ""
read -p "Choose installation method (1 or 2): " -n 1 -r
echo ""

if [[ $REPLY == "1" ]]; then
    echo "🔗 Creating symlink..."
    ln -s "${SKILL_SOURCE}" "${SKILL_DEST}"
    echo "✅ Symlink created: ${SKILL_DEST} -> ${SKILL_SOURCE}"
    echo ""
    echo "ℹ️  The skill will auto-update when you update the claude-starter project."
elif [[ $REPLY == "2" ]]; then
    echo "📋 Copying skill files..."
    cp -r "${SKILL_SOURCE}" "${SKILL_DEST}"
    echo "✅ Skill copied to: ${SKILL_DEST}"
    echo ""
    echo "ℹ️  To update, run this script again or manually copy files."
else
    echo "❌ Invalid choice. Installation cancelled."
    exit 1
fi

# Verify installation
echo ""
echo "🔍 Verifying installation..."
if [ -f "${SKILL_DEST}/skill.json" ] && [ -f "${SKILL_DEST}/instructions.md" ]; then
    echo "✅ Skill files verified"
else
    echo "❌ Installation verification failed"
    exit 1
fi

# Display success message
echo ""
echo "🎉 Setup Wizard Skill installed successfully!"
echo ""
echo "Usage:"
echo "------"
echo "The skill will automatically activate when you say things like:"
echo "  - 'Set up this project'"
echo "  - 'Configure Claude Code'"
echo "  - 'Help me get started'"
echo ""
echo "Or use the slash command:"
echo "  /setup:wizard"
echo ""
echo "Learn more:"
echo "  cat ${SKILL_DEST}/README.md"
echo ""
echo "Happy coding! 🚀"
