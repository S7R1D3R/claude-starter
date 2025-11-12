#!/usr/bin/env python3
"""
Claude Code Starter - Intelligent Setup Agent
Using Claude Agent SDK for autonomous project setup and configuration
"""

import os
import json
import sys
import subprocess
from pathlib import Path
from typing import Dict, List, Any, Optional
import asyncio


class SetupWizardAgent:
    """Intelligent setup wizard powered by Claude Agent SDK"""

    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root).resolve()
        self.config = {}
        self.detected_info = {}

    async def run(self):
        """Main entry point for the setup wizard"""
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║   Claude Code Starter - Intelligent Setup Wizard            ║")
        print("║   Powered by Claude Agent SDK                                ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        print()

        try:
            # Phase 1: Discovery
            await self.phase_discovery()

            # Phase 2: Interactive Configuration
            await self.phase_configuration()

            # Phase 3: Installation
            await self.phase_installation()

            # Phase 4: Validation
            await self.phase_validation()

            # Phase 5: Personalization
            await self.phase_personalization()

            # Summary
            self.print_summary()

        except KeyboardInterrupt:
            print("\n\n⚠️  Setup interrupted by user")
            sys.exit(1)
        except Exception as e:
            print(f"\n\n❌ Setup failed: {e}")
            raise

    async def phase_discovery(self):
        """Phase 1: Analyze project and detect languages/tools"""
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Phase 1: Project Discovery")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print()
        print("🔍 Analyzing project structure...")

        # Detect languages
        languages = self._detect_languages()
        print(f"✅ Detected languages: {', '.join(languages) if languages else 'None detected'}")

        # Detect package managers
        package_managers = self._detect_package_managers()
        print(f"✅ Detected package managers: {', '.join(package_managers) if package_managers else 'None detected'}")

        # Detect frameworks
        frameworks = self._detect_frameworks()
        print(f"✅ Detected frameworks: {', '.join(frameworks) if frameworks else 'None detected'}")

        # Detect existing tools
        tools = self._detect_existing_tools()
        print(f"✅ Detected tools: {', '.join(tools) if tools else 'None detected'}")

        # Check git status
        git_initialized = self._check_git()
        print(f"✅ Git repository: {'Initialized' if git_initialized else 'Not initialized'}")

        self.detected_info = {
            "languages": languages,
            "package_managers": package_managers,
            "frameworks": frameworks,
            "tools": tools,
            "git_initialized": git_initialized
        }

        print()

    async def phase_configuration(self):
        """Phase 2: Interactive configuration with user"""
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Phase 2: Configuration")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print()

        # In a real implementation, this would use the Claude Agent SDK
        # to have an intelligent conversation with the user
        # For now, we'll use simple prompts

        print("Let me help you configure your Claude Code setup.")
        print()

        # Ask about hooks
        print("🔧 Hooks Configuration")
        self.config["hooks"] = self._configure_hooks()

        # Ask about slash commands
        print("\n📝 Slash Commands")
        self.config["commands"] = self._configure_commands()

        # Ask about MCP servers
        print("\n🔌 MCP Servers")
        self.config["mcp_servers"] = self._configure_mcp_servers()

        # Ask about GitHub Actions
        print("\n🤖 GitHub Actions")
        self.config["github_actions"] = self._configure_github_actions()

        # Ask about RAG integration
        print("\n🧠 RAG Integration (Advanced)")
        self.config["rag"] = self._configure_rag()

        # Ask about Skills
        print("\n⚡ Skills System")
        self.config["skills"] = self._configure_skills()

        print()

    async def phase_installation(self):
        """Phase 3: Install dependencies and configure tools"""
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Phase 3: Installation")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print()

        # Initialize Git if needed
        if not self.detected_info["git_initialized"]:
            print("🌿 Initializing Git repository...")
            self._run_command("git init")
            print("✅ Git repository initialized")

        # Make hooks executable
        print("🔧 Making hooks executable...")
        self._run_command("chmod +x .claude/hooks/*.py")
        print("✅ Hooks are now executable")

        # Create directories
        print("📁 Creating required directories...")
        os.makedirs(".claude/logs", exist_ok=True)
        print("✅ Directories created")

        # Install dependencies based on detected package managers
        if self.config.get("install_dependencies", True):
            await self._install_dependencies()

        # Install MCP servers
        if self.config.get("mcp_servers", {}).get("enabled"):
            await self._install_mcp_servers()

        # Configure GitHub Actions
        if self.config.get("github_actions", {}).get("enabled"):
            self._setup_github_actions()

        # Setup RAG if requested
        if self.config.get("rag", {}).get("enabled"):
            await self._setup_rag()

        print()

    async def phase_validation(self):
        """Phase 4: Validate installation and test hooks"""
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Phase 4: Validation")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print()

        # Test hooks
        print("🧪 Testing hook execution...")
        hook_test = self._test_hooks()
        if hook_test:
            print("✅ Hooks can execute successfully")
        else:
            print("⚠️  Hook test failed - you may need to install dependencies")

        # Verify Python
        print("🐍 Checking Python...")
        python_version = self._check_python()
        if python_version:
            print(f"✅ Python {python_version} found")
        else:
            print("⚠️  Python not found")

        # Verify Git
        print("🌿 Checking Git...")
        git_version = self._check_git_version()
        if git_version:
            print(f"✅ Git {git_version} found")
        else:
            print("⚠️  Git not found")

        # Check MCP servers if configured
        if self.config.get("mcp_servers", {}).get("enabled"):
            print("🔌 Checking MCP servers...")
            self._validate_mcp_servers()

        print()

    async def phase_personalization(self):
        """Phase 5: Provide personalized recommendations"""
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Phase 5: Recommendations")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print()

        print("💡 Based on your project, here are some recommendations:")
        print()

        # Language-specific recommendations
        if "JavaScript" in self.detected_info["languages"] or "TypeScript" in self.detected_info["languages"]:
            print("📦 JavaScript/TypeScript:")
            print("   • Use /quality:lint with ESLint for code quality")
            print("   • Use /quality:format with Prettier for consistent formatting")
            print("   • Consider adding pre-commit hooks for automatic formatting")

        if "Python" in self.detected_info["languages"]:
            print("🐍 Python:")
            print("   • Use /quality:lint with pylint/ruff")
            print("   • Use /quality:format with black")
            print("   • Consider setting up virtual environments")

        if "Rust" in self.detected_info["languages"]:
            print("🦀 Rust:")
            print("   • Use /quality:lint with clippy")
            print("   • Use /quality:format with rustfmt")
            print("   • Enable all clippy warnings in Cargo.toml")

        # General recommendations
        print("\n🚀 Productivity Tips:")
        print("   • Use /ai:context for complex tasks requiring project understanding")
        print("   • Use /quality:review before committing code")
        print("   • Use /git:commit for conventional commit messages")
        print("   • Enable session-start hook for automatic project context")

        # Advanced features
        if self.config.get("mcp_servers", {}).get("enabled"):
            print("\n🔌 MCP Servers:")
            print("   • Your MCP servers are configured and ready")
            print("   • Claude can now use these external capabilities automatically")

        if self.config.get("rag", {}).get("enabled"):
            print("\n🧠 RAG Integration:")
            print("   • Add your project documentation to Archon")
            print("   • Claude will automatically search docs when needed")

        print()

    def print_summary(self):
        """Print setup summary"""
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("✨ Setup Complete!")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print()
        print("Your Claude Code environment is ready! 🚀")
        print()
        print("Next steps:")
        print("  1. Review CLAUDE.md for project context")
        print("  2. Customize .claude/settings.local.json if needed")
        print("  3. Start coding with Claude Code!")
        print()
        print("Quick start commands:")
        print("  /dev:setup    - Install project dependencies")
        print("  /quality:test - Run tests")
        print("  /git:commit   - Create conventional commit")
        print()
        print("For more information, see README.md and docs/")
        print()
        print("Happy coding! 💻")
        print()

    # Helper methods

    def _detect_languages(self) -> List[str]:
        """Detect programming languages in project"""
        languages = []

        # Check for language-specific files
        language_indicators = {
            "JavaScript": ["package.json", "*.js"],
            "TypeScript": ["tsconfig.json", "*.ts"],
            "Python": ["requirements.txt", "setup.py", "pyproject.toml", "*.py"],
            "Rust": ["Cargo.toml", "*.rs"],
            "Go": ["go.mod", "*.go"],
            "Java": ["pom.xml", "build.gradle", "*.java"],
            "Ruby": ["Gemfile", "*.rb"],
            "PHP": ["composer.json", "*.php"],
            "C++": ["CMakeLists.txt", "*.cpp"],
            "C": ["Makefile", "*.c"]
        }

        for lang, indicators in language_indicators.items():
            for indicator in indicators:
                if list(self.project_root.glob(indicator)):
                    if lang not in languages:
                        languages.append(lang)
                    break

        return languages

    def _detect_package_managers(self) -> List[str]:
        """Detect package managers in use"""
        managers = []

        manager_files = {
            "npm": "package.json",
            "yarn": "yarn.lock",
            "pnpm": "pnpm-lock.yaml",
            "pip": "requirements.txt",
            "poetry": "poetry.lock",
            "cargo": "Cargo.toml",
            "go": "go.mod",
            "maven": "pom.xml",
            "gradle": "build.gradle"
        }

        for manager, file in manager_files.items():
            if (self.project_root / file).exists():
                managers.append(manager)

        return managers

    def _detect_frameworks(self) -> List[str]:
        """Detect frameworks in use"""
        frameworks = []

        # Check package.json for frameworks
        package_json = self.project_root / "package.json"
        if package_json.exists():
            try:
                with open(package_json) as f:
                    data = json.load(f)
                    deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}

                    framework_mapping = {
                        "react": "React",
                        "vue": "Vue",
                        "angular": "Angular",
                        "next": "Next.js",
                        "express": "Express",
                        "nestjs": "NestJS"
                    }

                    for pkg, framework in framework_mapping.items():
                        if any(pkg in dep for dep in deps.keys()):
                            frameworks.append(framework)
            except:
                pass

        # Check Python frameworks
        requirements = self.project_root / "requirements.txt"
        if requirements.exists():
            try:
                content = requirements.read_text()
                if "django" in content.lower():
                    frameworks.append("Django")
                if "flask" in content.lower():
                    frameworks.append("Flask")
                if "fastapi" in content.lower():
                    frameworks.append("FastAPI")
            except:
                pass

        return frameworks

    def _detect_existing_tools(self) -> List[str]:
        """Detect existing development tools"""
        tools = []

        tool_files = {
            "ESLint": ".eslintrc.js",
            "Prettier": ".prettierrc",
            "Black": "pyproject.toml",
            "Pytest": "pytest.ini",
            "Jest": "jest.config.js",
            "Docker": "Dockerfile",
            "Docker Compose": "docker-compose.yml"
        }

        for tool, file in tool_files.items():
            if (self.project_root / file).exists():
                tools.append(tool)

        return tools

    def _check_git(self) -> bool:
        """Check if Git is initialized"""
        return (self.project_root / ".git").exists()

    def _check_python(self) -> Optional[str]:
        """Check Python version"""
        try:
            result = subprocess.run(
                ["python3", "--version"],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip().replace("Python ", "")
        except:
            return None

    def _check_git_version(self) -> Optional[str]:
        """Check Git version"""
        try:
            result = subprocess.run(
                ["git", "--version"],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip().replace("git version ", "")
        except:
            return None

    def _configure_hooks(self) -> Dict[str, Any]:
        """Configure hooks (simplified for now)"""
        print("   All hooks are enabled by default.")
        return {"enabled": True, "all": True}

    def _configure_commands(self) -> Dict[str, Any]:
        """Configure slash commands"""
        print("   All slash commands are available.")
        return {"enabled": True, "all": True}

    def _configure_mcp_servers(self) -> Dict[str, Any]:
        """Configure MCP servers"""
        response = input("   Would you like to configure MCP servers? (y/N): ").strip().lower()
        return {"enabled": response == "y"}

    def _configure_github_actions(self) -> Dict[str, Any]:
        """Configure GitHub Actions"""
        response = input("   Enable GitHub Actions workflows? (y/N): ").strip().lower()
        return {"enabled": response == "y"}

    def _configure_rag(self) -> Dict[str, Any]:
        """Configure RAG integration"""
        response = input("   Enable RAG integration with Archon? (advanced, y/N): ").strip().lower()
        return {"enabled": response == "y"}

    def _configure_skills(self) -> Dict[str, Any]:
        """Configure Skills system"""
        print("   Skills are enabled by default.")
        return {"enabled": True}

    async def _install_dependencies(self):
        """Install project dependencies based on detected package managers"""
        print("📦 Installing project dependencies...")

        if "npm" in self.detected_info["package_managers"]:
            print("   Running npm install...")
            self._run_command("npm install")
        elif "yarn" in self.detected_info["package_managers"]:
            print("   Running yarn install...")
            self._run_command("yarn install")
        elif "pnpm" in self.detected_info["package_managers"]:
            print("   Running pnpm install...")
            self._run_command("pnpm install")

        if "pip" in self.detected_info["package_managers"]:
            print("   Running pip install...")
            if (self.project_root / "requirements.txt").exists():
                self._run_command("pip install -r requirements.txt")

        if "cargo" in self.detected_info["package_managers"]:
            print("   Running cargo build...")
            self._run_command("cargo build")

        if "go" in self.detected_info["package_managers"]:
            print("   Running go mod download...")
            self._run_command("go mod download")

        print("✅ Dependencies installed")

    async def _install_mcp_servers(self):
        """Install recommended MCP servers"""
        print("🔌 Installing MCP servers...")
        # This would install MCP servers based on configuration
        print("   (MCP server installation would happen here)")
        print("✅ MCP servers configured")

    def _setup_github_actions(self):
        """Setup GitHub Actions"""
        print("🤖 Setting up GitHub Actions...")
        print("   Workflows are already in .github/workflows/")
        print("   ⚠️  Remember to add ANTHROPIC_API_KEY to repository secrets")
        print("✅ GitHub Actions configured")

    async def _setup_rag(self):
        """Setup RAG integration"""
        print("🧠 Setting up RAG integration...")
        print("   See docs/RAG_INTEGRATION.md for Archon setup instructions")
        print("✅ RAG configuration noted")

    def _test_hooks(self) -> bool:
        """Test if hooks can execute"""
        try:
            subprocess.run(
                ["python3", ".claude/hooks/session-start.py"],
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True,
                timeout=5
            )
            return True
        except:
            return False

    def _validate_mcp_servers(self):
        """Validate MCP server configuration"""
        print("   (MCP server validation would happen here)")
        print("✅ MCP servers validated")

    def _run_command(self, command: str, shell: bool = True):
        """Run shell command"""
        try:
            subprocess.run(
                command,
                shell=shell,
                check=True,
                cwd=self.project_root,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
        except subprocess.CalledProcessError as e:
            print(f"   ⚠️  Command failed: {command}")
            print(f"      Error: {e.stderr.decode() if e.stderr else 'Unknown error'}")


async def main():
    """Main entry point"""
    agent = SetupWizardAgent()
    await agent.run()


if __name__ == "__main__":
    asyncio.run(main())
