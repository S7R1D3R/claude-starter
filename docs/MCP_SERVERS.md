# MCP Servers Configuration Guide

Model Context Protocol (MCP) servers extend Claude Code with external tool access, databases, APIs, and services.

## 🚀 NEW: Docker MCP Toolkit (Recommended!)

**The easiest way to set up MCP servers is with Docker MCP Toolkit!**

Docker MCP Toolkit provides:
- 📦 **200+ pre-built MCP servers** in a curated catalog
- 🖱️ **One-click deployment** from Docker Desktop UI
- 🔒 **Secure credential management** built-in
- ⚡ **Containerized isolation** prevents conflicts
- 🎯 **Visual management** instead of JSON editing

**Prerequisites**: Docker Desktop 4.40+ with MCP Toolkit enabled

**Quick Start**:
1. Enable MCP Toolkit in Docker Desktop → Settings → Beta Features
2. Open MCP Toolkit in Docker Desktop sidebar
3. Browse Catalog and add servers (Filesystem, GitHub, etc.)
4. Connect Claude Code from the Clients tab
5. Done! No manual JSON editing needed.

**Full Guide**: See [DOCKER_MCP_TOOLKIT.md](DOCKER_MCP_TOOLKIT.md) for complete setup instructions.

---

## Manual MCP Setup (Alternative)

If you prefer manual configuration or need custom servers, use the traditional approach below:

## Quick Setup

### 1. Configuration Location

MCP servers are configured in your user-level Claude configuration:
```bash
~/.claude.json
```

**Important**: Do NOT commit this file. It contains API keys and should remain private.

### 2. Basic Structure

```json
{
  "mcpServers": {
    "server-name": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@package/name"],
      "env": {
        "API_KEY": "your-secret-key"
      }
    }
  }
}
```

## Recommended MCP Servers

### Essential Servers

#### 1. GitHub MCP
**Purpose**: PR management, issues, repository access

```json
{
  "mcpServers": {
    "github": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

**Get Token**: https://github.com/settings/tokens (needs `repo` scope)

#### 2. Sequential Thinking MCP
**Purpose**: Break down complex problems systematically

```json
{
  "sequential-thinking": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
  }
}
```

**No API key required**

#### 3. Filesystem MCP
**Purpose**: Enhanced file operations

```json
{
  "filesystem": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
  }
}
```

**Security Note**: Specify allowed directories explicitly

#### 4. Archon RAG MCP (Recommended!)
**Purpose**: RAG-powered knowledge base for project documentation

```json
{
  "archon": {
    "type": "http",
    "url": "http://localhost:8051",
    "description": "RAG knowledge base for project context"
  }
}
```

**Setup Required**:
1. Install Archon: `git clone -b stable https://github.com/coleam00/Archon.git`
2. Configure Supabase credentials
3. Start services: `docker-compose up -d`
4. Populate knowledge base with project docs

**Benefits**:
- 🔍 Semantic search across all project documentation
- 📚 Automatic context injection for better responses
- 💡 Code examples from docs instantly available
- 🎯 Vector-based relevance matching

**Full Setup Guide**: See [docs/RAG_INTEGRATION.md](RAG_INTEGRATION.md)

### Development Servers

#### Context7 MCP
**Purpose**: Access library documentation

```json
{
  "context7": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "@context7/server"],
    "env": {
      "CONTEXT7_API_KEY": "your_context7_key"
    }
  }
}
```

**Get API Key**: https://context7.com/api

#### PostgreSQL MCP
**Purpose**: Database queries and schema inspection

```json
{
  "postgres": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-postgres"],
    "env": {
      "DATABASE_URL": "postgresql://user:pass@localhost:5432/dbname"
    }
  }
}
```

#### Puppeteer MCP
**Purpose**: Browser automation and web scraping

```json
{
  "puppeteer": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-puppeteer"]
  }
}
```

## Complete Example Configuration

```json
{
  "mcpServers": {
    "github": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_xxxxxxxxxxxx"
      }
    },
    "sequential-thinking": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "filesystem": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/username/projects"]
    },
    "context7": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@context7/server"],
      "env": {
        "CONTEXT7_API_KEY": "your_key_here"
      }
    }
  }
}
```

## Setup Instructions

### Step 1: Create Configuration File

```bash
# Create or edit the configuration file
nano ~/.claude.json
```

### Step 2: Add MCP Servers

Copy the JSON configuration from the examples above.

### Step 3: Add API Keys

Replace placeholder values:
- `ghp_xxxxxxxxxxxx` → Your GitHub token
- `your_key_here` → Your API keys

### Step 4: Restart Claude Code

Close and reopen Claude Code to load the new configuration.

### Step 5: Verify

The MCP servers should now be available in Claude Code.

## Security Best Practices

### API Key Management

✅ **DO**:
- Store API keys in `~/.claude.json`
- Use environment variables for CI/CD
- Rotate keys regularly
- Use minimal required permissions

❌ **DON'T**:
- Commit `~/.claude.json` to git
- Share API keys in code or docs
- Use root/admin tokens
- Grant unnecessary scopes

### Access Control

For Filesystem MCP:
```json
{
  "filesystem": {
    "type": "stdio",
    "command": "npx",
    "args": [
      "-y",
      "@modelcontextprotocol/server-filesystem",
      "/allowed/path/one",
      "/allowed/path/two"
    ]
  }
}
```

## Troubleshooting

### MCP Server Not Loading

1. **Check configuration syntax**
   ```bash
   cat ~/.claude.json | python3 -m json.tool
   ```

2. **Verify npx is installed**
   ```bash
   npx --version
   ```

3. **Test server manually**
   ```bash
   npx -y @modelcontextprotocol/server-github
   ```

### Connection Errors

- Verify API keys are correct
- Check network connectivity
- Review allowed directories (Filesystem MCP)
- Check Claude Code logs

### Permission Issues

- Ensure API tokens have required scopes
- Check file system permissions
- Verify database connection strings

## Advanced Configuration

### HTTP MCP Servers

For servers running as HTTP services:

```json
{
  "custom-api": {
    "type": "http",
    "url": "http://localhost:3000/mcp",
    "headers": {
      "Authorization": "Bearer your_token"
    }
  }
}
```

### Environment Variables

Use environment variables for sensitive data:

```json
{
  "github": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-github"],
    "env": {
      "GITHUB_TOKEN": "${GITHUB_TOKEN}"
    }
  }
}
```

Then set in your shell:
```bash
export GITHUB_TOKEN=ghp_your_token
```

## Available MCP Servers

Explore more servers:
- **Official**: https://github.com/modelcontextprotocol/servers
- **Community**: https://github.com/topics/mcp-server
- **Documentation**: https://modelcontextprotocol.io

## Creating Custom MCP Servers

Want to create your own MCP server? See:
- [MCP Specification](https://modelcontextprotocol.io/docs)
- [Server Examples](https://github.com/modelcontextprotocol/servers)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)

## Resources

- [MCP Documentation](https://modelcontextprotocol.io)
- [Claude Code MCP Guide](https://docs.claude.com/claude-code/mcp)
- [GitHub Discussions](https://github.com/modelcontextprotocol/servers/discussions)

---

**Need help?** Open an issue or check the troubleshooting section above.
