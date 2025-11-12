#!/usr/bin/env python3
"""
Claude Code Starter - Intelligent Setup Wizard CLI
Entry point for the autonomous setup agent

Usage:
    python scripts/setup-agent.py           # Run basic wizard
    python scripts/setup-agent.py --ai      # Run AI-powered wizard (requires SDK)
    python scripts/setup-agent.py --help    # Show help
"""

import sys
import os
import argparse
from pathlib import Path

# Add wizard module to path
sys.path.insert(0, str(Path(__file__).parent))


def check_sdk_available():
    """Check if Claude Agent SDK is available"""
    try:
        import claude_agent_sdk
        return True
    except ImportError:
        return False


def print_help():
    """Print help message"""
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║   Claude Code Starter - Setup Wizard                        ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()
    print("Usage:")
    print("  python scripts/setup-agent.py           Run basic wizard")
    print("  python scripts/setup-agent.py --ai      Run AI-powered wizard")
    print("  python scripts/setup-agent.py --help    Show this help")
    print()
    print("Wizard Options:")
    print()
    print("  1. Basic Wizard (Default)")
    print("     • Fast, offline setup")
    print("     • Auto-detects project type")
    print("     • Configures Claude Code features")
    print("     • No external dependencies")
    print()
    print("  2. AI-Powered Wizard (--ai)")
    print("     • Intelligent project analysis")
    print("     • Natural language configuration")
    print("     • Personalized recommendations")
    print("     • Requires: claude-agent-sdk")
    print()
    print("Installation:")
    print("  pip install claude-agent-sdk    # For AI-powered wizard")
    print()


def run_basic_wizard():
    """Run the basic setup wizard"""
    try:
        from wizard.setup_agent import main
        import asyncio
        asyncio.run(main())
    except Exception as e:
        print(f"❌ Error running basic wizard: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def run_ai_wizard():
    """Run the AI-powered setup wizard"""
    if not check_sdk_available():
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("❌ Claude Agent SDK not installed")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print()
        print("The AI-powered wizard requires the Claude Agent SDK.")
        print()
        print("Install with:")
        print("  pip install claude-agent-sdk")
        print()
        print("Or use the basic wizard instead:")
        print("  python scripts/setup-agent.py")
        print()
        sys.exit(1)

    try:
        from wizard.intelligent_setup_agent import main
        import asyncio
        asyncio.run(main())
    except Exception as e:
        print(f"❌ Error running AI wizard: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Claude Code Starter Setup Wizard",
        add_help=False
    )
    parser.add_argument(
        "--ai",
        action="store_true",
        help="Use AI-powered wizard (requires claude-agent-sdk)"
    )
    parser.add_argument(
        "--help",
        action="store_true",
        help="Show help message"
    )

    args = parser.parse_args()

    if args.help:
        print_help()
        sys.exit(0)

    if args.ai:
        run_ai_wizard()
    else:
        run_basic_wizard()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
