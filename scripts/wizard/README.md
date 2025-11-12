# Setup Wizard

Automated setup wizards for Claude Code Starter boilerplate.

## Quick Reference

### Run Wizards

```bash
# Basic wizard (recommended)
python scripts/setup-agent.py

# AI-powered wizard (requires Claude Agent SDK)
python scripts/setup-agent.py --ai

# Shell wizard (fastest, minimal features)
./scripts/setup-wizard.sh

# Help
python scripts/setup-agent.py --help
```

## Wizard Files

- `setup-agent.py` - Main entry point CLI
- `setup_agent.py` - Basic wizard implementation
- `intelligent_setup_agent.py` - AI-powered wizard with Claude Agent SDK
- `requirements.txt` - Optional dependencies

## Features

### Basic Wizard

- Auto-detects languages, frameworks, and tools
- Interactive configuration
- Installs dependencies
- Validates setup
- Provides recommendations

### AI-Powered Wizard

Everything in Basic Wizard, plus:
- Intelligent project analysis using Claude
- Natural language configuration
- Context-aware recommendations
- Personalized productivity tips

## Requirements

### Basic Wizard
- Python 3.10+
- No additional dependencies

### AI-Powered Wizard
- Python 3.10+
- `claude-agent-sdk` (`pip install claude-agent-sdk`)
- `ANTHROPIC_API_KEY` environment variable

## Documentation

See [docs/SETUP_WIZARD.md](../../docs/SETUP_WIZARD.md) for complete documentation.

## Development

### Testing Detection Logic

```python
from wizard.setup_agent import SetupWizardAgent
import asyncio

async def test():
    agent = SetupWizardAgent()
    print('Languages:', agent._detect_languages())
    print('Package Managers:', agent._detect_package_managers())

asyncio.run(test())
```

### Extending the Wizard

1. Edit detection methods in `setup_agent.py`
2. Add custom configuration in `_configure_*` methods
3. Add installation steps in `phase_installation`
4. Update recommendations in `phase_personalization`

### Adding New Languages

```python
def _detect_languages(self) -> List[str]:
    languages = []

    language_indicators = {
        "YourLanguage": ["config.yml", "*.ext"],
        # Add your language detection
    }

    # Detection logic...
    return languages
```

## Architecture

```
setup-agent.py (CLI entry point)
    ├── Basic Wizard
    │   └── wizard/setup_agent.py
    │       ├── Phase 1: Discovery
    │       ├── Phase 2: Configuration
    │       ├── Phase 3: Installation
    │       ├── Phase 4: Validation
    │       └── Phase 5: Recommendations
    │
    └── AI Wizard
        └── wizard/intelligent_setup_agent.py
            ├── Gather Context
            ├── Claude Analysis
            ├── Execute Setup
            └── Personalized Recommendations
```

## Troubleshooting

**ImportError: No module named 'wizard'**
- Run from project root: `python scripts/setup-agent.py`

**Python version too old**
- Requires Python 3.10+
- Check: `python3 --version`

**Claude Agent SDK not found**
- Install: `pip install claude-agent-sdk`
- Or use basic wizard without `--ai` flag

**Permission denied**
- Make executable: `chmod +x scripts/setup-agent.py`

## License

MIT License - See [LICENSE](../../LICENSE)
