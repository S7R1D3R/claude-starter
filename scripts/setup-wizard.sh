#!/bin/bash
#
# Claude Code Starter - Setup Wizard
# Automates installation and configuration
#

set -e

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║     Claude Code Starter - Setup Wizard                      ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Check Python
echo "🔍 Checking dependencies..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required for hooks but not found."
    echo "   Please install Python 3.8+ and run this script again."
    exit 1
fi
echo "✅ Python 3 found: $(python3 --version)"

# Check Git
if ! command -v git &> /dev/null; then
    echo "❌ Git is required but not found."
    echo "   Please install Git and run this script again."
    exit 1
fi
echo "✅ Git found: $(git --version)"

# Make hooks executable
echo ""
echo "🔧 Making hooks executable..."
chmod +x .claude/hooks/*.py
echo "✅ Hooks are now executable"

# Initialize git if needed
echo ""
if [ ! -d ".git" ]; then
    echo "🌿 Initializing Git repository..."
    git init
    echo "✅ Git repository initialized"
else
    echo "✅ Git repository already exists"
fi

# Create local settings from example
echo ""
if [ ! -f ".claude/settings.local.json" ]; then
    echo "📝 Creating local settings file..."
    cp .claude/settings.local.json.example .claude/settings.local.json 2>/dev/null || true
    echo "✅ Local settings created (edit .claude/settings.local.json to customize)"
fi

# Create logs directory
echo ""
echo "📁 Creating logs directory..."
mkdir -p .claude/logs
echo "✅ Logs directory created"

# Test hooks
echo ""
echo "🧪 Testing hook execution..."
if python3 .claude/hooks/session-start.py < /dev/null > /dev/null 2>&1; then
    echo "✅ Hooks can execute successfully"
else
    echo "⚠️  Hook test failed - you may need to install dependencies"
fi

# MCP Server Setup (optional)
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "MCP Server Configuration"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "MCP servers enhance Claude Code with external tool access."
echo "Configuration should be added to: ~/.claude.json"
echo ""
echo "Recommended MCP servers:"
echo "  • GitHub MCP - PR and issue management"
echo "  • Sequential Thinking - Complex problem solving"
echo "  • Filesystem - Enhanced file operations"
echo ""
echo "See docs/MCP_SERVERS.md for setup instructions"
echo ""

# GitHub Actions Setup (optional)
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "GitHub Actions Configuration"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "To enable AI-powered PR reviews and automation:"
echo "  1. Add ANTHROPIC_API_KEY to repository secrets"
echo "  2. Ensure GitHub Actions is enabled"
echo "  3. Push .github/workflows to your repository"
echo ""

# Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✨ Setup Complete!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Next steps:"
echo "  1. Review CLAUDE.md for project context"
echo "  2. Customize .claude/settings.local.json if needed"
echo "  3. Open Claude Code and start coding!"
echo ""
echo "Quick start commands:"
echo "  /dev:init     - Initialize project"
echo "  /dev:setup    - Install dependencies"
echo "  /quality:test - Run tests"
echo ""
echo "For more information, see README.md and docs/"
echo ""
echo "Happy coding! 🚀"
