Set up Docker MCP Toolkit for this project with guided assistance.

## Instructions

Follow these steps to configure Docker MCP Toolkit:

### 1. Verify Prerequisites

Check if Docker Desktop is installed and meets version requirements:
- Run `docker --version` to check Docker version
- Minimum required: Docker Desktop 4.40+ (4.48+ recommended)
- If not installed or outdated, provide installation instructions

### 2. Check Docker MCP Toolkit Status

Determine current state:
- Run `docker ps --filter "name=mcp-"` to see active MCP servers
- Run `claude mcp list` to check Claude Code MCP configuration
- Report findings to user

### 3. Guide Docker Desktop Configuration

Provide step-by-step instructions:
1. Open Docker Desktop application
2. Navigate to Settings → Beta Features
3. Enable "Enable Docker MCP Toolkit"
4. Click Apply & Restart
5. Wait for Docker Desktop to restart

### 4. Recommend Essential Servers

Based on this project's structure, suggest:

**Essential (High Priority)**:
- **Filesystem MCP**: File access for /home/user/claude-starter
- **GitHub MCP**: Repository management, PRs, issues

**Recommended (Medium Priority)**:
- **Docker Hub MCP**: Container image management
- **Brave Search MCP**: Web research capabilities

**Optional (Low Priority)**:
- **PostgreSQL MCP**: If project uses databases
- **Jira MCP**: If team uses Jira for tracking

### 5. Installation Instructions

For each recommended server:
1. Open Docker Desktop → MCP Toolkit → Catalog
2. Search for server name (e.g., "Filesystem Official")
3. Click the **+** icon to add
4. Complete configuration wizard:
   - Filesystem: Select `/home/user/claude-starter` directory
   - GitHub: Complete OAuth authentication
   - Docker Hub: Optional login
   - Brave Search: Enter API key if available

### 6. Connect Claude Code

Guide connection setup:
1. In MCP Toolkit, go to Clients tab
2. Find "Claude Code (CLI)"
3. Choose configuration type:
   - **Project-scoped**: For this project only (creates `.mcp.json`)
   - **Global**: For all projects (updates `~/.claude.json`)
4. Recommend project-scoped for this setup
5. Click "Connect"

### 7. Verify Installation

Run verification commands:
```bash
# Navigate to project directory
cd /home/user/claude-starter

# List available MCP servers
claude mcp list

# Check Docker MCP containers
docker ps --filter "name=mcp-"
```

Expected output:
- `claude mcp list` shows MCP_DOCKER (connected)
- `docker ps` shows running mcp-* containers

### 8. Update .gitignore

If project-scoped configuration was chosen:
```bash
# Add .mcp.json to .gitignore if not already present
grep -q "\.mcp\.json" .gitignore || echo ".mcp.json" >> .gitignore
```

### 9. Provide Next Steps

Inform user:
- Docker MCP Toolkit is now configured
- Servers can be managed via Docker Desktop UI
- New servers can be added anytime from the Catalog
- Reference documentation: `docs/DOCKER_MCP_TOOLKIT.md`

### 10. Offer Test Commands

Suggest trying MCP functionality:
```
Ask me to:
- "List the project files" (tests Filesystem MCP)
- "Check the latest commits" (tests GitHub MCP if configured)
- "Search Docker Hub for node images" (tests Docker Hub MCP if configured)
```

## Troubleshooting

If issues occur:

**Docker Desktop not installed**:
- Provide download link: https://www.docker.com/products/docker-desktop/
- Recommend latest stable version

**MCP Toolkit not available**:
- Verify Docker Desktop version ≥ 4.40
- Check Beta Features are enabled in Settings
- Try restarting Docker Desktop

**MCP_DOCKER not connecting**:
- Ensure Docker Desktop is running
- Restart Claude Code session
- Check `docker ps` for mcp-gateway container

**Authentication failures**:
- Re-authenticate in MCP Toolkit UI
- For GitHub: Revoke and re-grant OAuth access
- Check Docker logs: `docker logs mcp-[server-name]`

## Resources

- Full setup guide: `docs/DOCKER_MCP_TOOLKIT.md`
- Manual MCP setup: `docs/MCP_SERVERS.md`
- Docker MCP Toolkit docs: https://docs.docker.com/ai/mcp-catalog-and-toolkit/

---

**Note**: Be encouraging and supportive throughout the process. Docker MCP Toolkit makes MCP setup much easier than manual configuration!
