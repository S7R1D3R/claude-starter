# Docker MCP Toolkit Integration Guide

## Overview

**Docker MCP Toolkit** is a powerful management interface integrated into Docker Desktop that lets you set up, manage, and run containerized MCP servers with Claude Code. It provides:

- 🚀 **200+ pre-built MCP servers** in a curated catalog
- 🔒 **Secure credential management** through Docker secrets
- ⚡ **One-click deployment** from Docker Desktop UI
- 🔄 **Automatic routing** through Docker MCP Gateway
- 🎯 **Project-scoped or global** MCP server configurations

## Why Use Docker MCP Toolkit?

### Traditional MCP Setup Challenges
- Manual server installation and configuration
- Complex `~/.claude.json` editing
- API key management in config files
- Dependency conflicts between servers
- Version compatibility issues

### Docker MCP Toolkit Benefits
- ✅ **Visual catalog** of available servers
- ✅ **One-click installation** with guided setup
- ✅ **Secure secrets** stored in Docker Desktop
- ✅ **Containerized isolation** prevents conflicts
- ✅ **Automatic updates** for server containers
- ✅ **Project-level configs** via `.mcp.json`
- ✅ **Unified gateway** for all MCP traffic

## Prerequisites

### Required Software

1. **Docker Desktop 4.40+** (4.48+ recommended)
   - Windows: v4.42 or newer
   - macOS: v4.40 or newer
   - Linux: v4.40 or newer

2. **Claude Code CLI** (latest version)
   ```bash
   curl -fsSL https://claude.ai/install.sh | sh
   ```

### Verify Installation

```bash
# Check Docker Desktop version
docker --version

# Check Claude Code CLI
claude --version

# Verify Docker is running
docker ps
```

## Setup Instructions

### Step 1: Enable MCP Toolkit in Docker Desktop

1. Open **Docker Desktop**
2. Go to **Settings** → **Beta features**
3. Enable **"Enable Docker MCP Toolkit"**
4. Click **Apply & Restart**

![Docker MCP Toolkit Setting](https://docs.docker.com/assets/images/mcp-toolkit-enable.png)

### Step 2: Access MCP Toolkit UI

1. In Docker Desktop, click the **MCP Toolkit** icon in the sidebar
2. You'll see two tabs:
   - **Catalog**: Browse and add MCP servers
   - **Clients**: Connect AI clients (Claude Desktop, Claude Code)

### Step 3: Add MCP Servers from Catalog

#### Popular Servers for Development

**Filesystem MCP**
```
Purpose: Secure file system access
Setup: Select directories to grant access
Auth: None required
```

**GitHub MCP**
```
Purpose: Repository management, PRs, issues
Setup: OAuth authentication
Auth: GitHub token (auto-managed)
```

**Docker Hub MCP**
```
Purpose: Search and manage Docker images
Setup: Optional Docker Hub login
Auth: Docker credentials
```

**PostgreSQL MCP**
```
Purpose: Database queries and schema inspection
Setup: Connection string configuration
Auth: Database credentials
```

**Jira MCP**
```
Purpose: Issue tracking and project management
Setup: Jira workspace URL and API token
Auth: Atlassian credentials
```

**Brave Search MCP**
```
Purpose: Web search capabilities
Setup: Brave API key
Auth: API key required
```

#### Installation Process

1. Go to **Catalog** tab in MCP Toolkit
2. Search for the desired server (e.g., "GitHub Official")
3. Click the **+ icon** to add
4. Complete the configuration wizard:
   - For OAuth servers: Authorize via browser
   - For API key servers: Enter credentials
   - For filesystem servers: Select allowed directories
5. Server container will download and start automatically

### Step 4: Connect Claude Code

#### Option A: Global Configuration (All Projects)

1. In MCP Toolkit, go to **Clients** tab
2. Find **"Claude Code (CLI)"**
3. Click **Connect**
4. This creates/updates `~/.claude.json` with:
   ```json
   {
     "mcpServers": {
       "MCP_DOCKER": {
         "command": "docker",
         "args": ["mcp", "gateway", "run"]
       }
     }
   }
   ```

#### Option B: Project-Scoped Configuration (This Project Only)

1. In MCP Toolkit, click **"Configure for Project"**
2. Select your project directory: `/home/user/claude-starter`
3. This creates `.mcp.json` in your project root
4. Add to `.gitignore`:
   ```bash
   echo ".mcp.json" >> .gitignore
   ```

### Step 5: Verify Connection

```bash
# Navigate to project directory
cd /home/user/claude-starter

# List available MCP servers
claude mcp list

# Expected output:
# ✓ MCP_DOCKER (connected)
#   - filesystem
#   - github
#   - docker-hub
#   - [other enabled servers]
```

## Configuration Examples

### Project-Level `.mcp.json`

When using project-scoped configuration, Docker creates `.mcp.json`:

```json
{
  "mcpServers": {
    "MCP_DOCKER": {
      "command": "docker",
      "args": ["mcp", "gateway", "run"]
    }
  }
}
```

**Important**: This file should be in `.gitignore` as it may contain project-specific settings.

### Global `~/.claude.json`

For system-wide configuration:

```json
{
  "mcpServers": {
    "MCP_DOCKER": {
      "command": "docker",
      "args": ["mcp", "gateway", "run"]
    }
  }
}
```

### Hybrid Approach (Recommended)

Use **Docker MCP Toolkit for Claude Code** + **Manual configs for specialized servers**:

```json
{
  "mcpServers": {
    "MCP_DOCKER": {
      "command": "docker",
      "args": ["mcp", "gateway", "run"]
    },
    "sequential-thinking": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "archon": {
      "type": "http",
      "url": "http://localhost:8051",
      "description": "RAG knowledge base"
    }
  }
}
```

## Managing MCP Servers

### Adding New Servers

```bash
# Via Docker Desktop UI
1. Open MCP Toolkit → Catalog
2. Search for server
3. Click + to add
4. Configure credentials

# Claude Code automatically detects new servers
claude mcp list
```

### Updating Servers

```bash
# Docker MCP Toolkit auto-updates server containers
# To manually update:
docker pull mcp/[server-name]:latest
```

### Removing Servers

```bash
# Via Docker Desktop UI
1. Open MCP Toolkit → Catalog
2. Find installed server
3. Click "Remove"

# Or via CLI
docker stop mcp-[server-name]
docker rm mcp-[server-name]
```

### Viewing Server Logs

```bash
# List MCP server containers
docker ps --filter "name=mcp-"

# View logs for a specific server
docker logs mcp-github

# Follow logs in real-time
docker logs -f mcp-github
```

## Security Best Practices

### Credential Management

✅ **DO**:
- Use Docker Desktop's built-in secrets management
- Store API keys through MCP Toolkit UI
- Use OAuth when available
- Grant minimal required permissions

❌ **DON'T**:
- Store credentials in `.mcp.json` or code
- Commit `.mcp.json` to version control
- Use root/admin tokens
- Share Docker MCP Gateway configs publicly

### Filesystem Access Control

When configuring Filesystem MCP:

```
Allowed Directories:
✅ /home/user/claude-starter
✅ /home/user/projects
❌ /home/user
❌ /etc
❌ /root
```

**Principle of Least Privilege**: Only grant access to directories Claude Code actively needs.

### Network Security

Docker MCP Gateway routes all traffic through `localhost`:
- MCP servers run in isolated containers
- No external network access by default
- Secrets never exposed in environment variables
- Encrypted communication between Claude and gateway

## Recommended Server Configurations

### For This Boilerplate Project

Based on the `claude-starter` project structure, recommended servers:

#### 1. **Filesystem MCP** (Essential)
```
Purpose: File operations, code reading
Configuration:
  - Allow: /home/user/claude-starter
  - Read/Write: Yes
```

#### 2. **GitHub MCP** (Essential)
```
Purpose: PR management, issue tracking
Configuration:
  - OAuth: Enable
  - Scopes: repo, read:org
```

#### 3. **Docker Hub MCP** (Recommended)
```
Purpose: Container image management
Configuration:
  - Login: Optional
  - Use case: Managing Docker-based MCP servers
```

#### 4. **Brave Search MCP** (Optional)
```
Purpose: Web research for documentation
Configuration:
  - API Key: Required
  - Use case: Finding library docs, Stack Overflow
```

#### 5. **PostgreSQL MCP** (If using databases)
```
Purpose: Database queries
Configuration:
  - Connection String: postgresql://localhost:5432/dbname
```

### Quick Setup for Claude Starter

```bash
# 1. Enable these servers in Docker MCP Toolkit:
#    - Filesystem MCP → Allow /home/user/claude-starter
#    - GitHub MCP → OAuth authenticate
#    - Docker Hub MCP → Optional login

# 2. Verify setup
cd /home/user/claude-starter
claude mcp list

# 3. Test functionality
# Ask Claude to:
# - List project files (Filesystem MCP)
# - Check GitHub repo status (GitHub MCP)
# - Search Docker images (Docker Hub MCP)
```

## Troubleshooting

### Issue: MCP_DOCKER Not Showing in `claude mcp list`

**Solution**:
1. Verify Docker Desktop is running: `docker ps`
2. Check Docker MCP Gateway is active: `docker ps --filter "name=mcp-gateway"`
3. Restart Docker Desktop
4. Restart Claude Code session

### Issue: "Docker Desktop is not running" Error

**Solution**:
```bash
# WSL2 users (Windows)
# Ensure Docker Desktop WSL integration is enabled
# Settings → Resources → WSL Integration → Enable

# macOS/Linux users
# Start Docker Desktop application
open -a Docker  # macOS
systemctl start docker  # Linux
```

### Issue: Authentication Failures

**Solution**:
1. Re-authenticate in MCP Toolkit UI
2. For GitHub: Revoke and re-grant OAuth access
3. For API keys: Verify key validity and permissions
4. Check Docker logs: `docker logs mcp-[server-name]`

### Issue: Server Container Won't Start

**Solution**:
```bash
# Check container status
docker ps -a --filter "name=mcp-"

# View container logs
docker logs mcp-[server-name]

# Remove and re-add server
docker rm -f mcp-[server-name]
# Then re-add via MCP Toolkit UI
```

### Issue: Slow Performance

**Solution**:
- Check Docker resource allocation: Settings → Resources
- Increase memory/CPU if needed (recommend 4GB+ RAM)
- Limit number of active MCP servers
- Use project-scoped config to only load needed servers

### Issue: .mcp.json Conflicts with ~/.claude.json

**Solution**:
- Project-level `.mcp.json` takes precedence
- Use **one or the other**, not both simultaneously
- For multi-project setup: Use global `~/.claude.json`
- For single project: Use project `.mcp.json`

## Performance Optimization

### Resource Management

```bash
# Monitor Docker resource usage
docker stats --filter "name=mcp-"

# Recommended allocations for Docker Desktop:
# - Memory: 4-8 GB
# - CPUs: 2-4 cores
# - Disk: 20+ GB
```

### Selective Server Loading

Instead of enabling all 200+ servers, focus on:
- **Essential**: Filesystem, GitHub
- **Project-specific**: Database, API servers relevant to your stack
- **As-needed**: Search, browser automation only when required

### Caching

Docker MCP Toolkit caches:
- Server container images (faster subsequent launches)
- Authentication tokens (OAuth refresh)
- Configuration state

## Advanced Usage

### Custom MCP Server in Docker

Create a `Dockerfile` for your custom MCP server:

```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 8080
CMD ["npm", "start"]
```

Register in Docker MCP Toolkit:
```bash
docker build -t my-custom-mcp .
# Add to MCP Toolkit via custom server option
```

### Environment-Specific Configs

```bash
# Development
.mcp.dev.json

# Production
.mcp.prod.json

# Load based on environment
ln -sf .mcp.$ENV.json .mcp.json
```

### MCP Server Health Checks

```bash
# Create monitoring script
cat > check-mcp-health.sh <<'EOF'
#!/bin/bash
for server in $(docker ps --filter "name=mcp-" --format "{{.Names}}"); do
  echo "Checking $server..."
  docker exec $server healthcheck || echo "❌ $server unhealthy"
done
EOF

chmod +x check-mcp-health.sh
./check-mcp-health.sh
```

## Integration with This Boilerplate

### Update .gitignore

```bash
echo "
# Docker MCP Toolkit
.mcp.json
.mcp.*.json
" >> .gitignore
```

### Add Slash Command: /mcp:status

Create `.claude/commands/mcp/status.md`:

```markdown
Check the status of all Docker MCP Toolkit servers:

1. Run `docker ps --filter "name=mcp-"`
2. Run `claude mcp list`
3. Report which servers are active
4. Check for any errors in logs
```

### Add to Session Start Hook

Update `.claude/hooks/session-start/hook.sh`:

```bash
# Check Docker MCP Toolkit status
if command -v docker &> /dev/null; then
  echo "🐳 Docker MCP Toolkit Status:"
  docker ps --filter "name=mcp-" --format "  ✓ {{.Names}}" 2>/dev/null || echo "  ℹ️  No MCP servers running"
fi
```

## Resources

### Documentation
- [Docker MCP Toolkit Official Docs](https://docs.docker.com/ai/mcp-catalog-and-toolkit/)
- [MCP Specification](https://modelcontextprotocol.io)
- [Docker MCP Gateway GitHub](https://github.com/docker/mcp-gateway)

### Server Catalog
- Browse all 200+ servers in Docker Desktop MCP Toolkit
- [Official MCP Servers](https://github.com/modelcontextprotocol/servers)

### Community
- [Docker Community Slack](https://dockercommunity.slack.com) - #mcp-toolkit channel
- [MCP GitHub Discussions](https://github.com/modelcontextprotocol/servers/discussions)

## Quick Reference

### Common Commands

```bash
# List MCP servers
claude mcp list

# Check Docker MCP containers
docker ps --filter "name=mcp-"

# View server logs
docker logs mcp-github

# Restart MCP Gateway
docker restart mcp-gateway

# Health check all servers
docker ps --filter "name=mcp-" --format "{{.Names}}: {{.Status}}"
```

### Configuration Locations

```
Global:     ~/.claude.json
Project:    .mcp.json (in project root)
Secrets:    Managed by Docker Desktop
Logs:       docker logs mcp-[server-name]
```

## Next Steps

1. **Install Docker Desktop 4.40+** if not already installed
2. **Enable MCP Toolkit** in Docker Desktop settings
3. **Add essential servers** (Filesystem, GitHub)
4. **Connect Claude Code** via Clients tab
5. **Verify** with `claude mcp list`
6. **Start using** Claude Code with enhanced MCP capabilities!

---

**Pro Tip**: Start with Filesystem and GitHub MCPs, then add others as needed. The toolkit makes it easy to enable/disable servers on the fly!
