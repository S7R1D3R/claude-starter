# RAG Integration Examples

This directory contains example implementations for integrating **Retrieval-Augmented Generation (RAG)** with the claude-starter boilerplate using [Archon](https://github.com/coleam00/Archon).

## What's Included

### Hooks (`hooks/`)
- **`rag-prompt-enhance.py`** - Automatically enhances user prompts with relevant context from the knowledge base

### Slash Commands (`commands/`)
- **`knowledge-search.md`** - Search the RAG knowledge base
- **`knowledge-add.md`** - Add documentation to the knowledge base

### Skills (`skills/`)
- **`SKILL.md`** - RAG context loading skill for complex tasks

## Quick Setup

### 1. Install Archon

```bash
# Clone Archon
git clone -b stable https://github.com/coleam00/Archon.git
cd Archon

# Configure environment
cp .env.example .env
nano .env  # Add Supabase credentials

# Start services
docker-compose up -d

# Verify services are running
docker-compose ps
# Should show: archon-frontend, archon-server, archon-mcp, archon-agents
```

### 2. Configure MCP

Edit `~/.claude.json`:

```json
{
  "mcpServers": {
    "archon": {
      "type": "http",
      "url": "http://localhost:8051",
      "description": "RAG knowledge base for project context"
    }
  }
}
```

### 3. Populate Knowledge Base

```bash
# Open Archon UI
open http://localhost:3737

# Or use API
curl -X POST http://localhost:8181/api/sources/website \
  -H "Content-Type: application/json" \
  -d '{
    "project_id": "your-project-id",
    "url": "https://docs.yourframework.com",
    "crawl_sitemap": true
  }'
```

### 4. Install Examples (Optional)

Choose which features you want:

#### Option A: RAG-Enhanced Hooks

```bash
# Copy RAG prompt enhancement hook
cp examples/rag-integration/hooks/rag-prompt-enhance.py .claude/hooks/
chmod +x .claude/hooks/rag-prompt-enhance.py

# Enable in .claude/settings.json
cat >> .claude/settings.json << 'EOF'
{
  "hooks": {
    "userPromptSubmit": {
      "command": ".claude/hooks/rag-prompt-enhance.py",
      "enabled": true
    }
  }
}
EOF
```

Now every prompt you send will be automatically enhanced with relevant docs!

#### Option B: Knowledge Commands

```bash
# Copy slash commands
mkdir -p .claude/commands/knowledge
cp examples/rag-integration/commands/knowledge-search.md .claude/commands/knowledge/search.md
cp examples/rag-integration/commands/knowledge-add.md .claude/commands/knowledge/add.md
```

Now you can use:
- `/knowledge:search <query>` - Search documentation
- `/knowledge:add <source>` - Add new docs

#### Option C: RAG Skills

```bash
# Copy to user skills directory
mkdir -p ~/.claude/skills/rag-context
cp examples/rag-integration/skills/SKILL.md ~/.claude/skills/rag-context/instructions.md

# Create skill.json
cat > ~/.claude/skills/rag-context/skill.json << 'EOF'
{
  "name": "rag-context",
  "description": "Load comprehensive project context using RAG for complex tasks",
  "version": "1.0.0"
}
EOF
```

The skill will automatically activate for complex coding tasks!

## Usage Examples

### Example 1: Automatic Context Enhancement

With the RAG hook enabled:

```
You: How do I implement user authentication?

[RAG Hook automatically searches knowledge base]
[Finds 3 relevant documentation pages]
[Appends context to your prompt]

Claude receives:
"How do I implement user authentication?

═══════════════════════════════════════
📚 RELEVANT CONTEXT FROM PROJECT KNOWLEDGE BASE
═══════════════════════════════════════

1. Authentication Patterns (Relevance: 94%)
   Source: docs/auth/patterns.md

   "The project uses JWT-based authentication with refresh
   tokens. Passwords are hashed using bcrypt..."

   Example Code:
   ```typescript
   const token = await auth.login(email, password);
   ```

... [more context] ...
"

Claude now provides an answer based on YOUR specific docs!
```

### Example 2: Manual Knowledge Search

```
You: /knowledge:search "database transactions"

Claude:
📚 Knowledge Base Search Results

Query: "database transactions"
Found: 3 relevant documents

─────────────────────────────────────────────────────

1. Database Transaction Patterns (Relevance: 94%)
   Source: docs/database/transactions.md

   "Our application uses the Unit of Work pattern..."

   [Code examples included]

─────────────────────────────────────────────────────

💡 Key Takeaways:
- Use Unit of Work pattern for multi-step transactions
- Always implement rollback logic
- Configure connection pools appropriately

Would you like help implementing this pattern?
```

### Example 3: Adding Documentation

```
You: /knowledge:add https://react.dev

Claude:
Adding React documentation to knowledge base...

🔍 Analyzing source: https://react.dev
✓ Valid website detected
✓ Sitemap found: 247 pages
✓ Starting crawl...

[Progress updates...]

✅ Complete! Indexed 247 pages with 1,842 code examples.
The React documentation is now searchable.
```

## Configuration

### RAG Hook Settings

Edit `hooks/rag-prompt-enhance.py`:

```python
# Configuration
ARCHON_API_BASE = "http://localhost:8181/api"
MAX_RESULTS = 3              # Number of docs to retrieve
MIN_RELEVANCE = 0.65         # Relevance threshold (0-1)
ENABLE_CODE_EXAMPLES = True  # Include code snippets
VERBOSE_LOGGING = False      # Debug output
```

### Archon Settings

Edit Archon's `.env`:

```env
# Vector search settings
EMBEDDING_MODEL=text-embedding-ada-002
SEARCH_TOP_K=10
MIN_RELEVANCE_SCORE=0.6

# Indexing settings
CHUNK_SIZE=512
CHUNK_OVERLAP=50
```

## Troubleshooting

### Archon Not Responding

```bash
# Check if services are running
docker-compose ps

# View logs
docker-compose logs archon-mcp

# Restart services
docker-compose restart
```

### Poor Search Results

1. **Increase relevance threshold**
   ```python
   MIN_RELEVANCE = 0.75  # Higher = more relevant but fewer results
   ```

2. **Add more documentation**
   - More docs = better coverage
   - Include code examples
   - Keep docs updated

3. **Check indexing**
   ```bash
   # Verify in Archon UI
   open http://localhost:3737
   # Navigate to Knowledge → Check embedding status
   ```

### Hook Not Working

```bash
# Test manually
echo '{"type": "userPromptSubmit", "prompt": "test"}' | \
  python3 .claude/hooks/rag-prompt-enhance.py

# Check permissions
chmod +x .claude/hooks/rag-prompt-enhance.py

# View logs
tail -f .claude/logs/hooks.log
```

## Performance Tips

### Optimize Query Speed

1. **Use caching**
   ```python
   from functools import lru_cache

   @lru_cache(maxsize=100)
   def search_knowledge_cached(query: str):
       # Cached searches
   ```

2. **Adjust result limits**
   ```python
   MAX_RESULTS = 2  # Fewer results = faster
   ```

3. **Increase relevance threshold**
   ```python
   MIN_RELEVANCE = 0.8  # Skip low-relevance results
   ```

### Optimize Indexing

1. **Batch processing**
   - Add multiple sources at once
   - Use parallel processing

2. **Selective indexing**
   - Only index documentation, skip marketing pages
   - Use include/exclude patterns

3. **Periodic updates**
   - Refresh docs weekly/monthly
   - Don't re-index unchanged content

## Advanced Usage

### Custom Query Strategies

Modify the hook to use different search strategies:

```python
def search_by_intent(prompt: str) -> List[Dict]:
    """Use different search strategies based on intent"""

    if "example" in prompt.lower():
        # Prioritize code examples
        return search_knowledge(prompt, category="examples")

    elif "how to" in prompt.lower():
        # Prioritize tutorials
        return search_knowledge(prompt, category="tutorials")

    else:
        # General documentation
        return search_knowledge(prompt)
```

### Multi-Source RAG

Query multiple knowledge sources:

```python
def search_all_sources(query: str) -> List[Dict]:
    """Search across multiple RAG sources"""
    results = []

    # Project docs (Archon)
    results.extend(search_archon(query))

    # Framework docs (Context7)
    results.extend(search_context7(query))

    # Team wiki
    results.extend(search_wiki(query))

    # Rank and merge
    return rank_results(results)
```

## Best Practices

1. **Keep docs updated** - Stale docs = poor results
2. **Include examples** - Code examples are most valuable
3. **Organize well** - Use clear categories and tags
4. **Test queries** - Verify important topics are findable
5. **Monitor usage** - Track which queries work best

## Resources

- **Full RAG Integration Guide**: [../../docs/RAG_INTEGRATION.md](../../docs/RAG_INTEGRATION.md)
- **Archon Repository**: https://github.com/coleam00/Archon
- **MCP Configuration**: [../../docs/MCP_SERVERS.md](../../docs/MCP_SERVERS.md)
- **Hooks Documentation**: [../../docs/HOOKS.md](../../docs/HOOKS.md)

## Need Help?

- Open an issue on GitHub
- Check Archon discussions
- See [docs/RAG_INTEGRATION.md](../../docs/RAG_INTEGRATION.md) for detailed setup

---

**Happy RAG-enhanced coding!** 🚀📚
