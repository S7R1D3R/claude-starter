# RAG Integration Guide

## Integrating Archon with Claude-Starter

This guide shows you how to add **Retrieval-Augmented Generation (RAG)** capabilities to your Claude Code workflow using [Archon](https://github.com/coleam00/Archon).

## What is RAG?

**Retrieval-Augmented Generation** enhances AI responses by:
- **Retrieving** relevant context from a knowledge base
- **Augmenting** prompts with that context
- **Generating** more accurate, informed responses

Think of it as giving Claude instant access to your entire project documentation, API references, and code examples.

## Why Use Archon?

Archon provides:
- ✅ **Vector-based semantic search** - Find relevant docs by meaning, not just keywords
- ✅ **MCP Server integration** - Native Claude Code support
- ✅ **Multi-format support** - PDFs, websites, markdown, code examples
- ✅ **Intelligent chunking** - Optimized context retrieval
- ✅ **Result reranking** - Most relevant information first

## Integration Approaches

### Approach 1: MCP Server (Recommended)
**Best for**: Direct Claude Code integration, real-time knowledge access

### Approach 2: Enhanced Hooks
**Best for**: Automatic context injection during development

### Approach 3: Slash Commands
**Best for**: On-demand knowledge retrieval

### Approach 4: Skills
**Best for**: Complex RAG workflows

---

## Approach 1: MCP Server Integration

### Prerequisites

1. **Install Archon**
   ```bash
   git clone -b stable https://github.com/coleam00/Archon.git
   cd Archon
   docker-compose up -d
   ```

2. **Setup Supabase** (Free tier works)
   - Go to https://supabase.com
   - Create a new project
   - Save your connection credentials

3. **Configure Archon**
   ```bash
   # Copy environment template
   cp .env.example .env

   # Edit with your credentials
   nano .env
   ```

   Add:
   ```env
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_key
   OPENAI_API_KEY=your_openai_key  # Or use Ollama
   ```

4. **Verify Archon is Running**
   ```bash
   # Check services
   docker-compose ps

   # Should show:
   # - archon-frontend (port 3737)
   # - archon-server (port 8181)
   # - archon-mcp (port 8051)
   # - archon-agents (port 8052)
   ```

### Configure Claude Code

Edit `~/.claude.json`:

```json
{
  "mcpServers": {
    "archon": {
      "type": "http",
      "url": "http://localhost:8051",
      "description": "RAG-powered knowledge base for project context"
    }
  }
}
```

### Populate Knowledge Base

Open Archon UI at `http://localhost:3737` and:

1. **Create a Project**
   - Name: Your project name
   - Description: Brief overview

2. **Add Documentation Sources**

   **From Websites:**
   ```
   Add Source → Website
   URL: https://docs.yourframework.com
   ✓ Auto-detect sitemaps
   ```

   **From Local Files:**
   ```
   Add Source → Upload
   - API documentation PDFs
   - Architecture diagrams
   - Code examples
   ```

   **From GitHub:**
   ```
   Add Source → Repository
   URL: https://github.com/yourorg/docs
   ```

3. **Index the Content**
   - Click "Process" on each source
   - Wait for embedding generation
   - Verify in "Knowledge" tab

### Using RAG in Claude Code

Now Claude can automatically retrieve context:

**Example Session:**
```
You: How do I authenticate users in this framework?

Claude: [Automatically queries Archon MCP]
Based on your project documentation, authentication is handled using...
[Includes specific code examples from your docs]
```

Claude will automatically:
- Detect when knowledge lookup would help
- Query Archon's vector database
- Include relevant context in responses

### Advanced MCP Configuration

**Custom Search Parameters:**
```json
{
  "archon": {
    "type": "http",
    "url": "http://localhost:8051",
    "config": {
      "maxResults": 5,
      "minRelevance": 0.7,
      "includeCodeExamples": true
    }
  }
}
```

---

## Approach 2: RAG-Enhanced Hooks

Automatically inject relevant context into prompts and validations.

### Enhanced User Prompt Hook

Create `.claude/hooks/rag-prompt-enhance.py`:

```python
#!/usr/bin/env python3
"""
RAG-Enhanced Prompt Hook
Automatically adds relevant context from Archon knowledge base
"""

import sys
import json
import requests
from typing import Dict, List

ARCHON_API = "http://localhost:8181/api"
ARCHON_MCP = "http://localhost:8051"

def search_knowledge(query: str, max_results: int = 3) -> List[Dict]:
    """Query Archon's knowledge base"""
    try:
        response = requests.post(
            f"{ARCHON_API}/knowledge/search",
            json={
                "query": query,
                "limit": max_results,
                "min_relevance": 0.6
            },
            timeout=5
        )

        if response.status_code == 200:
            return response.json().get("results", [])
        return []
    except Exception as e:
        # Fail gracefully if Archon unavailable
        print(f"RAG search failed: {e}", file=sys.stderr)
        return []

def enhance_prompt(original_prompt: str) -> str:
    """Add relevant context to user prompt"""

    # Search for relevant knowledge
    results = search_knowledge(original_prompt)

    if not results:
        return original_prompt

    # Build context enhancement
    context_lines = [
        "\n[Relevant Context from Project Knowledge Base]",
        ""
    ]

    for i, result in enumerate(results, 1):
        context_lines.append(f"{i}. {result['title']} (Relevance: {result['score']:.0%})")
        context_lines.append(f"   {result['excerpt']}")

        if 'code_example' in result:
            context_lines.append(f"   Code: {result['code_example']}")

        context_lines.append("")

    context_lines.append("[End Context]")

    # Append context to prompt
    enhanced = original_prompt + "\n" + "\n".join(context_lines)
    return enhanced

def main():
    # Read hook input
    input_data = json.loads(sys.stdin.read())
    prompt = input_data.get("prompt", "")

    # Enhance with RAG
    enhanced_prompt = enhance_prompt(prompt)

    # Return enhanced prompt
    result = {
        "prompt": enhanced_prompt,
        "message": "✨ Added context from knowledge base"
    }

    print(json.dumps(result))
    sys.exit(0)

if __name__ == '__main__':
    main()
```

**Enable the Hook:**

Edit `.claude/settings.json`:
```json
{
  "hooks": {
    "userPromptSubmit": {
      "command": ".claude/hooks/rag-prompt-enhance.py",
      "enabled": true
    }
  }
}
```

### What This Does

Before each prompt is sent to Claude:
1. **Extract intent** from your message
2. **Query Archon** for relevant docs
3. **Append context** automatically
4. **Claude sees** both your question + relevant docs

**Example:**
```
You type: "How do I handle errors?"

Claude receives:
"How do I handle errors?

[Relevant Context from Project Knowledge Base]

1. Error Handling Best Practices (Relevance: 87%)
   Use try-catch blocks with specific error types.
   Always log errors with context.

   Code:
   try {
     await operation();
   } catch (error) {
     logger.error('Operation failed', { error });
     throw new AppError('Operation failed', error);
   }

[End Context]"
```

---

## Approach 3: Slash Commands for Knowledge

Create on-demand RAG queries.

### /knowledge:search Command

Create `.claude/commands/knowledge/search.md`:

```markdown
---
description: Search project knowledge base for relevant documentation
---

# Search Knowledge Base

You are helping the user search the project's RAG-powered knowledge base.

## Instructions

1. **Understand the Query**: Determine what information the user needs
2. **Query Archon**: Use the Archon MCP server to search for relevant content
3. **Present Results**: Show the most relevant documentation with excerpts
4. **Offer Actions**: Suggest follow-up queries or related topics

## Query Strategy

- Use semantic search (meaning-based, not just keywords)
- Include code examples when available
- Show relevance scores
- Limit to top 5 most relevant results

## Response Format

For each result, show:
- Title and source
- Relevance score
- Key excerpt
- Code example (if available)
- Link to full document (if available)

## Example Output

```
📚 Knowledge Base Results for "authentication"

1. User Authentication Flow (Relevance: 92%)
   Source: docs/authentication.md

   "The authentication system uses JWT tokens with refresh token rotation..."

   Code Example:
   ```typescript
   const token = await auth.login(email, password);
   ```

   [View Full Document]

2. OAuth2 Integration Guide (Relevance: 85%)
   Source: docs/oauth2.md
   ...
```

## Follow-up Suggestions

After showing results, suggest:
- Related topics to explore
- More specific queries
- Implementation help
```

### /knowledge:add Command

Create `.claude/commands/knowledge/add.md`:

```markdown
---
description: Add new documentation to the knowledge base
---

# Add to Knowledge Base

Help the user add new documentation sources to Archon.

## Instructions

1. **Determine Source Type**: Website, file, or code repository
2. **Validate Source**: Check accessibility and format
3. **Use Archon API**: Call the appropriate endpoint to add source
4. **Process Content**: Trigger indexing and embedding generation
5. **Confirm Success**: Verify content is searchable

## Supported Source Types

**Websites:**
- Full site crawling with sitemap detection
- Single page capture
- Automatic code example extraction

**Files:**
- PDF documents
- Markdown files
- Word documents
- Plain text

**Repositories:**
- GitHub repositories
- README and documentation folders
- Code examples

## Example

User: "Add the React documentation to our knowledge base"

Response:
```
Adding React documentation to knowledge base...

✓ Detected source: Website (https://react.dev)
✓ Found sitemap with 247 pages
✓ Starting crawl and indexing...
✓ Processing: 50/247 pages
...
✓ Complete! Indexed 247 pages with 1,842 code examples

The React documentation is now searchable in your knowledge base.

Try: /knowledge:search "how to use hooks"
```
```

### /knowledge:refresh Command

Create `.claude/commands/knowledge/refresh.md`:

```markdown
---
description: Update and refresh knowledge base content
---

# Refresh Knowledge Base

Update outdated documentation and re-index content.

## Instructions

1. **Check for Updates**: Query Archon for stale sources
2. **Re-fetch Content**: Download latest versions
3. **Re-index**: Generate fresh embeddings
4. **Report Changes**: Show what was updated

## Use Cases

- Documentation websites that update frequently
- GitHub repositories with active development
- Internal docs that change regularly

## Example

```
Refreshing knowledge base...

Checking 12 sources for updates...

✓ React Docs: No changes
✓ TypeScript Docs: 3 pages updated
✓ Internal API Docs: 15 pages updated
⚠ FastAPI Docs: Site unreachable (will retry)

Re-indexing 18 updated pages...
✓ Complete!

Updated content is now searchable.
```
```

---

## Approach 4: RAG Skills

Create sophisticated RAG workflows.

### Architecture Context Skill

Create `~/.claude/skills/architecture-context/skill.json`:

```json
{
  "name": "architecture-context",
  "description": "Load comprehensive architectural context using RAG for system design tasks",
  "version": "1.0.0",
  "triggers": [
    "architecture",
    "system design",
    "scalability",
    "database design"
  ]
}
```

Create `~/.claude/skills/architecture-context/instructions.md`:

```markdown
# Architecture Context Skill

When the user asks about system architecture, design patterns, or scalability:

1. **Query Knowledge Base** for:
   - System architecture documents
   - Database schemas
   - API specifications
   - Deployment configurations
   - Performance requirements

2. **Analyze Current State**:
   - Review existing architecture
   - Identify patterns in use
   - Find related code

3. **Provide Contextualized Recommendations**:
   - Based on documented patterns
   - Consistent with current architecture
   - Include specific examples from knowledge base

4. **Reference Documentation**:
   - Link to relevant arch docs
   - Show similar implementations
   - Cite design decisions

## Example Workflow

User: "How should I design the user service to scale?"

1. Query Archon for:
   - "microservices architecture"
   - "user service design"
   - "scalability patterns"
   - "database sharding"

2. Review results and extract:
   - Current architecture patterns
   - Scaling strategies in docs
   - Team's past decisions

3. Provide recommendation:
   "Based on your architecture docs, the team uses:
   - Event-driven microservices
   - PostgreSQL with read replicas
   - Redis for caching

   For the user service, I recommend:
   [Detailed design based on docs]"
```

---

## Complete Integration Example

### Full Setup Workflow

**1. Install Archon:**
```bash
git clone -b stable https://github.com/coleam00/Archon.git
cd Archon
docker-compose up -d
```

**2. Configure MCP:**
```bash
# Edit ~/.claude.json
cat >> ~/.claude.json << 'EOF'
{
  "mcpServers": {
    "archon": {
      "type": "http",
      "url": "http://localhost:8051"
    }
  }
}
EOF
```

**3. Add Knowledge Sources:**

Open http://localhost:3737 and add:
- Your project's README and docs
- Framework documentation
- API references
- Code examples

**4. Install RAG Hooks:**
```bash
cd /path/to/claude-starter
cp examples/rag-hooks/* .claude/hooks/
chmod +x .claude/hooks/rag-*.py
```

**5. Enable in Settings:**
```json
{
  "hooks": {
    "userPromptSubmit": {
      "command": ".claude/hooks/rag-prompt-enhance.py",
      "enabled": true
    }
  }
}
```

**6. Test It:**
```bash
claude-code

# In Claude Code:
> How do I implement authentication in this project?

# Claude will automatically query Archon and provide
# context-aware answers based on your docs!
```

---

## Best Practices

### Knowledge Base Organization

**Project Structure:**
```
Archon Knowledge Base
├── Project: YourApp
│   ├── Architecture
│   │   ├── System Design
│   │   ├── Database Schema
│   │   └── API Specs
│   ├── Development
│   │   ├── Setup Guide
│   │   ├── Coding Standards
│   │   └── Testing Guide
│   ├── External Docs
│   │   ├── Framework Docs
│   │   ├── Library References
│   │   └── Best Practices
│   └── Code Examples
│       ├── Authentication
│       ├── Database Access
│       └── API Endpoints
```

### Content Quality

**Good Documentation for RAG:**
- ✅ Clear, structured content
- ✅ Code examples with context
- ✅ Specific implementation details
- ✅ Architecture diagrams (with text descriptions)
- ✅ Decision rationale (why, not just what)

**Avoid:**
- ❌ Vague or ambiguous descriptions
- ❌ Outdated information
- ❌ Code without explanation
- ❌ Implementation details without context

### Update Frequency

**How Often to Refresh:**
- **Daily**: Active documentation sites
- **Weekly**: Framework docs, libraries
- **Monthly**: Stable references, specifications
- **On-demand**: Internal docs after major changes

### Query Optimization

**Effective Queries:**
```
✅ "How do I handle user authentication with JWT?"
✅ "What's the database schema for the user table?"
✅ "Show me examples of API error handling"

❌ "authentication" (too broad)
❌ "code" (not specific)
❌ "help" (no context)
```

---

## Troubleshooting

### Archon MCP Not Connecting

**Check Service:**
```bash
curl http://localhost:8051/health
# Should return: {"status": "ok"}
```

**Check Logs:**
```bash
docker-compose logs archon-mcp
```

**Verify Configuration:**
```bash
cat ~/.claude.json | jq '.mcpServers.archon'
```

### Poor Search Results

**Improve Relevance:**
1. Add more specific documentation
2. Include code examples
3. Use consistent terminology
4. Refresh stale content

**Check Embeddings:**
```bash
# In Archon UI
Navigate to: Knowledge → View Embeddings
Verify: Documents are properly indexed
```

### Hook Failures

**Test RAG Hook Manually:**
```bash
echo '{"type": "userPromptSubmit", "prompt": "test query"}' | \
  python3 .claude/hooks/rag-prompt-enhance.py
```

**Check Archon API:**
```bash
curl -X POST http://localhost:8181/api/knowledge/search \
  -H "Content-Type: application/json" \
  -d '{"query": "authentication", "limit": 3}'
```

---

## Performance Optimization

### Vector Search Tuning

**Adjust Relevance Threshold:**
```python
# In rag-prompt-enhance.py
{
  "query": query,
  "limit": 3,
  "min_relevance": 0.7  # Higher = more relevant but fewer results
}
```

### Caching

**Add Result Caching:**
```python
import hashlib
import json
from functools import lru_cache

@lru_cache(maxsize=100)
def search_knowledge_cached(query_hash: str, query: str) -> str:
    """Cached knowledge search"""
    results = search_knowledge(query)
    return json.dumps(results)

# Usage
query_hash = hashlib.md5(query.encode()).hexdigest()
results = json.loads(search_knowledge_cached(query_hash, query))
```

### Batch Processing

**Optimize Multiple Queries:**
```python
def search_knowledge_batch(queries: List[str]) -> Dict[str, List[Dict]]:
    """Search multiple queries in parallel"""
    response = requests.post(
        f"{ARCHON_API}/knowledge/batch_search",
        json={"queries": queries},
        timeout=10
    )
    return response.json()
```

---

## Advanced Use Cases

### 1. Context-Aware Code Review

Hook that adds relevant style guides during reviews:

```python
# .claude/hooks/rag-code-review.py
def enhance_code_review(file_path: str, changes: str) -> str:
    # Query for coding standards
    standards = search_knowledge(f"coding standards {language}")

    # Query for similar code patterns
    patterns = search_knowledge(f"code examples {component_type}")

    # Return context
    return format_review_context(standards, patterns)
```

### 2. Onboarding Assistant

Skill for new developer onboarding:

```markdown
# Onboarding Skill

When helping new developers, automatically provide:
1. Setup guides from knowledge base
2. Architecture overview
3. Code standards and conventions
4. Common patterns and examples
5. Team-specific practices

Query knowledge base for:
- "getting started"
- "development setup"
- "architecture overview"
- "coding conventions"
```

### 3. API Explorer

Command that explores API documentation:

```bash
/api:explore <endpoint>

# Searches knowledge base for:
# - API endpoint documentation
# - Request/response schemas
# - Example usage
# - Authentication requirements
```

---

## Integration Checklist

- [ ] Install and configure Archon
- [ ] Set up Supabase database
- [ ] Add Archon MCP to `~/.claude.json`
- [ ] Populate knowledge base with docs
- [ ] Install RAG-enhanced hooks (optional)
- [ ] Add knowledge slash commands (optional)
- [ ] Create RAG skills (optional)
- [ ] Test knowledge retrieval
- [ ] Verify search relevance
- [ ] Set up refresh schedule
- [ ] Train team on RAG features

---

## Resources

- **Archon Repository**: https://github.com/coleam00/Archon
- **MCP Documentation**: https://modelcontextprotocol.io
- **Vector Search Guide**: See Archon docs
- **Supabase Setup**: https://supabase.com/docs

---

## Next Steps

1. **Start Simple**: Begin with MCP integration only
2. **Add Content**: Populate knowledge base with key docs
3. **Test Queries**: Verify search quality
4. **Enhance Gradually**: Add hooks and commands as needed
5. **Monitor Usage**: Track which queries work best
6. **Iterate**: Improve content based on results

**Questions?** Check the troubleshooting section or open an issue!
