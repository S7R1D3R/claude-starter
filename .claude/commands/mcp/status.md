Check the status of all MCP servers (both Docker MCP Toolkit and manual configurations).

## Instructions

Provide a comprehensive MCP status report:

### 1. Check Claude Code MCP Configuration

Run `claude mcp list` and analyze the output:
- List all configured MCP servers
- Show connection status for each
- Identify MCP_DOCKER if using Docker MCP Toolkit
- Note any disconnected or failed servers

### 2. Check Docker MCP Toolkit Servers

If MCP_DOCKER is present:
```bash
# List all MCP server containers
docker ps --filter "name=mcp-" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

# Count active servers
docker ps --filter "name=mcp-" --quiet | wc -l
```

### 3. Check MCP Gateway Status

If using Docker MCP Toolkit:
```bash
# Check MCP Gateway health
docker ps --filter "name=mcp-gateway" --format "{{.Status}}"

# View recent gateway logs (last 20 lines)
docker logs --tail 20 mcp-gateway 2>/dev/null || echo "MCP Gateway not running"
```

### 4. Verify Configuration Files

Check for MCP configuration files:
```bash
# Project-level config
ls -lh .mcp.json 2>/dev/null || echo "No project-level .mcp.json"

# Global config
ls -lh ~/.claude.json 2>/dev/null || echo "No global ~/.claude.json"
```

### 5. Check Individual Server Health

For each active Docker MCP server, check logs:
```bash
# List server names and check for errors
for server in $(docker ps --filter "name=mcp-" --format "{{.Names}}"); do
  echo "=== $server ==="
  docker logs --tail 5 $server 2>&1 | grep -i "error\|warning\|ready" || echo "No issues detected"
done
```

### 6. Performance Check

If Docker is being used:
```bash
# Show resource usage for MCP containers
docker stats --no-stream --filter "name=mcp-" --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"
```

### 7. Summarize Status

Provide a clear summary:
- **Total MCP servers configured**: X
- **Active/Connected**: Y
- **Docker MCP Toolkit servers**: Z
- **Manual MCP servers**: W
- **Issues detected**: List any problems

### 8. Provide Recommendations

Based on status:

**If all healthy**:
- ✅ All MCP servers operating normally
- No action required

**If issues detected**:
- 🔴 List specific problems
- Provide troubleshooting steps
- Suggest relevant documentation

**If no MCP configured**:
- ℹ️  No MCP servers configured
- Suggest running `/mcp:setup-docker` for easy setup
- Or refer to `docs/MCP_SERVERS.md` for manual setup

## Output Format

Present results in a clear, formatted table:

```
MCP Server Status Report
========================

Claude Code MCP Configuration:
  MCP_DOCKER: ✓ Connected
  sequential-thinking: ✓ Connected
  archon: ✗ Disconnected

Docker MCP Toolkit Servers:
  mcp-filesystem: ✓ Running (32MB RAM, 0.5% CPU)
  mcp-github: ✓ Running (48MB RAM, 1.2% CPU)
  mcp-docker-hub: ✓ Running (28MB RAM, 0.3% CPU)

MCP Gateway:
  Status: ✓ Healthy
  Uptime: 2 hours

Configuration:
  Project config: .mcp.json (384 bytes)
  Global config: ~/.claude.json (2.1 KB)

Summary:
  Total: 5 servers
  Active: 4
  Issues: 1 (archon disconnected)

Recommendation:
  Check Archon RAG service: docker-compose ps
```

## Troubleshooting Commands

If issues are found, provide relevant commands:

```bash
# Restart all MCP servers
docker restart $(docker ps --filter "name=mcp-" --quiet)

# Restart MCP Gateway
docker restart mcp-gateway

# View full logs for a specific server
docker logs -f mcp-[server-name]

# Remove and re-add a problematic server
docker rm -f mcp-[server-name]
# Then re-add via Docker Desktop MCP Toolkit UI
```

## Resources

- Docker MCP Toolkit setup: `docs/DOCKER_MCP_TOOLKIT.md`
- Manual MCP configuration: `docs/MCP_SERVERS.md`
- Troubleshooting guide: `docs/DOCKER_MCP_TOOLKIT.md#troubleshooting`
