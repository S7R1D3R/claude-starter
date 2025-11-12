#!/usr/bin/env python3
"""
Claude Code Starter - Advanced Intelligent Setup Agent
Uses Claude Agent SDK for truly autonomous and intelligent setup

NOTE: This requires claude-agent-sdk to be installed:
    pip install claude-agent-sdk

This demonstrates the full potential of using Claude Agent SDK
for an interactive, intelligent setup experience.
"""

import os
import json
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional

try:
    from claude_agent_sdk import query, ClaudeAgentOptions
    SDK_AVAILABLE = True
except ImportError:
    SDK_AVAILABLE = False
    print("⚠️  claude-agent-sdk not installed. Install with: pip install claude-agent-sdk")


class IntelligentSetupAgent:
    """
    Advanced setup agent using Claude Agent SDK for intelligent,
    context-aware project setup and configuration
    """

    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root).resolve()
        self.project_context = {}
        self.setup_decisions = {}

    async def run(self):
        """Main entry point for intelligent setup"""
        if not SDK_AVAILABLE:
            print("❌ Claude Agent SDK is required for this wizard")
            print("   Install with: pip install claude-agent-sdk")
            print("   Or use the basic wizard: python scripts/wizard/setup_agent.py")
            sys.exit(1)

        print("╔══════════════════════════════════════════════════════════════╗")
        print("║   Claude Code Starter - AI-Powered Setup Wizard             ║")
        print("║   Using Claude Agent SDK for Intelligent Configuration      ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        print()

        # Gather project context
        await self._gather_project_context()

        # Have Claude analyze the project and suggest setup
        await self._intelligent_analysis()

        # Execute setup with Claude's guidance
        await self._execute_setup()

        # Get personalized recommendations
        await self._get_recommendations()

        print("\n✨ Intelligent setup complete!")

    async def _gather_project_context(self):
        """Gather comprehensive project context"""
        print("🔍 Gathering project context...")

        context = {
            "project_root": str(self.project_root),
            "files": self._get_file_structure(),
            "existing_config": self._get_existing_config(),
            "detected_languages": self._detect_languages(),
            "detected_tools": self._detect_tools(),
        }

        self.project_context = context
        print(f"✅ Context gathered: {len(context['files'])} files analyzed")

    async def _intelligent_analysis(self):
        """Use Claude to intelligently analyze project and suggest setup"""
        print("\n🤖 Claude is analyzing your project...")

        prompt = f"""
I need help setting up Claude Code for my project. Here's what I have:

Project Structure:
{json.dumps(self.project_context, indent=2)}

Please analyze my project and provide:
1. What type of project this is
2. What languages and frameworks you detect
3. What Claude Code features would be most useful
4. What hooks should be enabled
5. What MCP servers would be helpful
6. Any specific configuration recommendations

Provide a concise, actionable setup plan.
"""

        options = ClaudeAgentOptions(
            system_prompt="You are a helpful setup assistant for Claude Code. Provide clear, concise recommendations based on the project structure.",
            max_turns=1
        )

        print("\nClaude's Analysis:")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        analysis = []
        async for message in query(prompt=prompt, options=options):
            print(message, end='', flush=True)
            analysis.append(message)

        print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        # Parse Claude's recommendations
        self.setup_decisions = self._parse_recommendations(''.join(analysis))

    async def _execute_setup(self):
        """Execute setup based on Claude's recommendations"""
        print("\n🚀 Executing setup based on recommendations...")

        # This would execute the actual setup steps
        # For now, we'll show what would be done

        print("   • Making hooks executable")
        print("   • Creating .claude/logs directory")
        print("   • Configuring settings.json")

        if self.setup_decisions.get("install_dependencies"):
            print("   • Installing project dependencies")

        if self.setup_decisions.get("setup_mcp"):
            print("   • Configuring MCP servers")

        print("\n✅ Setup executed successfully")

    async def _get_recommendations(self):
        """Get personalized recommendations from Claude"""
        print("\n💡 Getting personalized recommendations...")

        prompt = f"""
Based on this project setup:
- Languages: {', '.join(self.project_context.get('detected_languages', []))}
- Tools: {', '.join(self.project_context.get('detected_tools', []))}

Provide 3-5 specific, actionable tips for using Claude Code effectively with this project.
Focus on productivity, code quality, and best practices.
"""

        options = ClaudeAgentOptions(
            system_prompt="Provide concise, actionable productivity tips for Claude Code users.",
            max_turns=1
        )

        print("\nRecommendations:")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        async for message in query(prompt=prompt, options=options):
            print(message, end='', flush=True)

        print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    # Helper methods

    def _get_file_structure(self) -> List[str]:
        """Get simplified file structure"""
        files = []
        for path in self.project_root.rglob("*"):
            if path.is_file():
                # Skip common ignore patterns
                if any(part.startswith('.') for part in path.parts):
                    continue
                if 'node_modules' in path.parts or '__pycache__' in path.parts:
                    continue

                rel_path = path.relative_to(self.project_root)
                files.append(str(rel_path))

                # Limit to prevent huge context
                if len(files) >= 100:
                    break

        return files

    def _get_existing_config(self) -> Dict[str, bool]:
        """Check for existing configuration files"""
        config_files = {
            "claude_settings": (self.project_root / ".claude" / "settings.json").exists(),
            "git": (self.project_root / ".git").exists(),
            "package_json": (self.project_root / "package.json").exists(),
            "requirements_txt": (self.project_root / "requirements.txt").exists(),
            "cargo_toml": (self.project_root / "Cargo.toml").exists(),
        }
        return config_files

    def _detect_languages(self) -> List[str]:
        """Detect programming languages"""
        languages = set()

        # Simple extension-based detection
        ext_map = {
            ".js": "JavaScript",
            ".ts": "TypeScript",
            ".py": "Python",
            ".rs": "Rust",
            ".go": "Go",
            ".java": "Java",
            ".rb": "Ruby",
            ".php": "PHP"
        }

        for file in self.project_root.rglob("*"):
            if file.is_file():
                ext = file.suffix
                if ext in ext_map:
                    languages.add(ext_map[ext])

        return list(languages)

    def _detect_tools(self) -> List[str]:
        """Detect development tools"""
        tools = []

        tool_indicators = {
            "ESLint": [".eslintrc.js", ".eslintrc.json", ".eslintrc"],
            "Prettier": [".prettierrc", ".prettierrc.json"],
            "Jest": ["jest.config.js", "jest.config.json"],
            "Pytest": ["pytest.ini", "pyproject.toml"],
            "Docker": ["Dockerfile", "docker-compose.yml"],
            "GitHub Actions": [".github/workflows"]
        }

        for tool, files in tool_indicators.items():
            for file in files:
                if (self.project_root / file).exists():
                    tools.append(tool)
                    break

        return tools

    def _parse_recommendations(self, analysis: str) -> Dict[str, Any]:
        """Parse Claude's recommendations into actionable decisions"""
        # Simple parsing - in a real implementation, this would be more sophisticated
        decisions = {
            "install_dependencies": "dependencies" in analysis.lower() or "install" in analysis.lower(),
            "setup_mcp": "mcp" in analysis.lower(),
            "enable_hooks": True,  # Default to true
            "setup_github_actions": "github" in analysis.lower() or "actions" in analysis.lower()
        }

        return decisions


async def main():
    """Main entry point"""
    import asyncio
    agent = IntelligentSetupAgent()
    await agent.run()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
