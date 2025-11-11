---
description: Load comprehensive project context for complex AI tasks
---

# Load Project Context

Load extensive project context to help Claude Code understand the full scope of the codebase for complex tasks.

## Context Loading Strategy

### 1. Project Structure
```bash
tree -L 3 -I 'node_modules|.git|dist|build'
```

Map out:
- Directory organization
- Key entry points
- Module boundaries
- Configuration locations

### 2. Technology Stack

Read and analyze:
- **package.json** / **requirements.txt** / **Cargo.toml**
  - Dependencies
  - Scripts
  - Version constraints
- **tsconfig.json** / **pyproject.toml**
  - Language configuration
  - Build settings
- **docker-compose.yml** / **Dockerfile**
  - Infrastructure

### 3. Architecture Understanding

Identify patterns:
- **MVC** / **MVVM** / **Layered** architecture
- **Frontend** framework (React, Vue, Angular)
- **Backend** framework (Express, Django, Rails)
- **Database** (PostgreSQL, MongoDB, etc.)
- **API** style (REST, GraphQL, gRPC)

### 4. Key Files Analysis

Read critical files:
```
docs/
├── architecture/
├── CLAUDE.md
└── README.md

src/
├── index.*
├── main.*
├── app.*
└── config/
```

### 5. Recent Changes

```bash
git log --since="2 weeks ago" --oneline --stat
git diff HEAD~20..HEAD --stat
```

Understand:
- What's being worked on
- Recent features
- Problem areas

### 6. Dependencies Graph

Map out:
- How modules depend on each other
- External service integrations
- API contracts

### 7. Code Conventions

Extract from:
- **.eslintrc** / **pylintrc**
- **CLAUDE.md** standards
- Existing code patterns

## Context Assembly

Build comprehensive context document:

```markdown
# Project Context

## Overview
[1-2 paragraph project description]

## Architecture
- Pattern: [MVC/Microservices/etc]
- Frontend: [Framework + version]
- Backend: [Framework + version]
- Database: [Type + version]
- Infrastructure: [Docker/K8s/etc]

## Directory Structure
\`\`\`
[Tree output]
\`\`\`

## Key Components
1. **Authentication** (src/auth/)
   - OAuth2 flow
   - JWT tokens
   - Session management

2. **API Layer** (src/api/)
   - REST endpoints
   - Validation middleware
   - Error handling

[etc...]

## Data Flow
[User Request] → [API Gateway] → [Business Logic] → [Database]
                           ↓
                      [Cache Layer]

## External Dependencies
- Stripe for payments
- SendGrid for emails
- AWS S3 for storage

## Current Focus
Based on recent commits:
- Implementing payment processing
- Refactoring authentication
- Adding test coverage

## Conventions
- Use TypeScript strict mode
- Async/await over promises
- Functional components with hooks
- Test all public APIs
```

## Use Task Tool for Deep Analysis

For thorough exploration:
```
Use the Task tool with subagent_type=Explore to:
- Map out complete codebase structure
- Understand component relationships
- Identify patterns and conventions
- Locate all configuration files
```

## When to Use This Command

Use `/ai:context` before:
- Large refactoring tasks
- Architectural changes
- Cross-cutting feature implementation
- Performance optimization
- Security audits
- Code migration

## Output

Present context in structured format:
1. **Summary** - Quick overview
2. **Architecture** - System design
3. **Components** - Key modules
4. **Dependencies** - External services
5. **Conventions** - Code standards
6. **Current State** - Recent work

Then confirm: "Context loaded. What would you like to work on?"

## Arguments

- `/ai:context` - Load full project context
- `/ai:context frontend` - Focus on frontend
- `/ai:context --deep` - Use Explore subagent for thorough analysis

**IMPORTANT**: This command uses significant tokens. Use only when necessary for complex tasks requiring deep understanding.
