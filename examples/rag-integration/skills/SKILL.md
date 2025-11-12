# RAG Context Loading Skill

**Skill Name:** rag-context
**Description:** Automatically load relevant project context from RAG knowledge base for complex tasks
**Version:** 1.0.0

## Purpose

This skill automatically queries the Archon RAG knowledge base to provide comprehensive project context when working on complex coding tasks. It ensures Claude has access to:

- Project architecture and design patterns
- Code standards and conventions
- API specifications and interfaces
- Best practices and common patterns
- Relevant code examples

## When to Invoke

Automatically invoke this skill when the user:

1. **Starts a complex implementation task**
   - "Implement user authentication system"
   - "Create a new API endpoint for payments"
   - "Refactor the data access layer"

2. **Asks about architecture or design**
   - "How should I structure this feature?"
   - "What's the best way to handle caching here?"
   - "Should I use REST or GraphQL?"

3. **Needs pattern/example guidance**
   - "Show me how we handle errors"
   - "What's our standard for API responses?"
   - "How do we test database operations?"

4. **Works on unfamiliar parts of codebase**
   - "I need to modify the payment processing module"
   - "How does the authentication flow work?"
   - "Where should I add this new service?"

## Skill Workflow

### 1. Understand the Task

Extract key elements:
- **Domain**: Which part of the system (auth, payments, data, etc.)
- **Operation**: What action (create, update, refactor, debug)
- **Scope**: Complexity and components involved

### 2. Query Knowledge Base

Search for relevant documentation in these categories:

**Architecture Context:**
```
Query: "system architecture {domain}"
Query: "design patterns {domain}"
Query: "component relationships {domain}"
```

**Implementation Patterns:**
```
Query: "code standards {language}"
Query: "common patterns {operation} {domain}"
Query: "best practices {technology}"
```

**API & Interfaces:**
```
Query: "API specification {endpoint}"
Query: "interface definitions {component}"
Query: "data models {entity}"
```

**Code Examples:**
```
Query: "example implementation {feature}"
Query: "{domain} code examples"
Query: "test examples {component}"
```

### 3. Synthesize Context

Organize retrieved information into categories:

```markdown
## 📚 Project Context Loaded

### Architecture Overview
{High-level architecture relevant to task}

### Design Patterns in Use
{Patterns the team follows for this type of task}

### Code Standards
{Relevant coding conventions and style guides}

### Similar Implementations
{Code examples from the project}

### API Specifications
{Relevant API endpoints and interfaces}

### Best Practices
{Team-specific best practices}
```

### 4. Apply Context to Task

Use the loaded context to:
- Follow established patterns
- Maintain consistency with existing code
- Apply team conventions
- Reference similar implementations
- Avoid known anti-patterns

### 5. Provide Implementation

Generate solution that:
- ✅ Matches project architecture
- ✅ Follows team conventions
- ✅ Uses established patterns
- ✅ Includes proper error handling
- ✅ Maintains consistency with examples
- ✅ Includes relevant tests

## Example Invocation

### User Request
```
"I need to add a new API endpoint for creating user profiles"
```

### Skill Execution

**Step 1: Understand Task**
- Domain: API, User Management
- Operation: Create new endpoint
- Scope: REST API, Database, Validation

**Step 2: Query Knowledge Base**
```
Querying knowledge base...

1. "API architecture patterns" → 3 results
2. "REST endpoint examples" → 5 results
3. "user management code" → 4 results
4. "validation best practices" → 2 results
5. "API testing patterns" → 3 results
```

**Step 3: Synthesize Context**
```markdown
## 📚 Project Context Loaded

### Architecture Overview
Your API uses:
- Express.js with TypeScript
- Controller → Service → Repository pattern
- Joi for request validation
- Jest for testing

### Design Patterns in Use
For new API endpoints, the team follows:
1. Controller handles HTTP concerns (req/res)
2. Service contains business logic
3. Repository manages data access
4. Middleware for auth, validation, error handling

### Code Standards
- Use async/await (not callbacks)
- Validate all inputs with Joi schemas
- Return consistent error format
- Include OpenAPI docs
- Write integration tests

### Similar Implementation Example
From `UserController.createUser()`:
```typescript
async createUser(req: Request, res: Response) {
  const validated = userSchema.validate(req.body);
  const user = await userService.create(validated);
  res.status(201).json({ data: user });
}
```

### API Response Format
Standard success response:
```json
{
  "data": { ...result },
  "meta": { timestamp, version }
}
```

Error response:
```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable message",
    "details": { ...validation errors }
  }
}
```

### Testing Expectations
- Integration tests for happy path
- Validation error tests
- Authentication/authorization tests
- Use test fixtures for data
```

**Step 4: Provide Implementation**

Now I'll implement the endpoint following your project's patterns...

```typescript
// src/controllers/ProfileController.ts
import { Request, Response } from 'express';
import { profileService } from '../services/ProfileService';
import { createProfileSchema } from '../validation/profileSchemas';

export class ProfileController {
  /**
   * Create a new user profile
   * POST /api/profiles
   */
  async createProfile(req: Request, res: Response) {
    // Validate input (following project pattern)
    const validated = createProfileSchema.validate(req.body);
    if (validated.error) {
      return res.status(400).json({
        error: {
          code: 'VALIDATION_ERROR',
          message: 'Invalid profile data',
          details: validated.error.details
        }
      });
    }

    try {
      // Create profile through service layer
      const profile = await profileService.create(
        req.user.id,
        validated.value
      );

      // Return standard success format
      return res.status(201).json({
        data: profile,
        meta: {
          timestamp: new Date().toISOString(),
          version: 'v1'
        }
      });
    } catch (error) {
      // Standard error handling
      if (error instanceof ConflictError) {
        return res.status(409).json({
          error: {
            code: 'PROFILE_EXISTS',
            message: 'User already has a profile'
          }
        });
      }
      throw error; // Let error middleware handle others
    }
  }
}
```

Following your project's patterns, I've also created:
- ✅ Service layer implementation
- ✅ Repository with database access
- ✅ Joi validation schema
- ✅ Integration tests
- ✅ OpenAPI documentation

Would you like me to show those files as well?

## Configuration

### Prerequisites

1. **Archon Running**
   ```bash
   docker-compose ps | grep archon
   ```

2. **Knowledge Base Populated**
   - Architecture documentation
   - Code examples
   - API specifications
   - Style guides

3. **MCP Configured**
   ```json
   // ~/.claude.json
   {
     "mcpServers": {
       "archon": {
         "type": "http",
         "url": "http://localhost:8051"
       }
     }
   }
   ```

### Skill Settings

Customize behavior in skill configuration:

```json
{
  "maxContextQueries": 5,
  "minRelevanceScore": 0.7,
  "includeCodeExamples": true,
  "prioritizeRecent": true,
  "contextCategories": [
    "architecture",
    "patterns",
    "examples",
    "standards",
    "apis"
  ]
}
```

## Benefits

Using this skill provides:

✅ **Consistency**: Code matches project patterns
✅ **Quality**: Follows established best practices
✅ **Speed**: No need to manually search docs
✅ **Context**: Understands full project architecture
✅ **Learning**: New team members see patterns in action

## Limitations

Be aware of:

⚠️ **Requires populated knowledge base**: No docs = no context
⚠️ **Query time overhead**: ~2-5 seconds for context loading
⚠️ **Archon must be running**: Falls back to no context if unavailable
⚠️ **Relevance depends on quality**: Better docs = better context

## Troubleshooting

### No Context Loaded

**Issue**: Skill reports "No relevant context found"

**Solutions**:
1. Check Archon is running: `curl http://localhost:8051/health`
2. Verify knowledge base has content
3. Try broader search terms
4. Add more documentation to Archon

### Poor Quality Results

**Issue**: Retrieved context isn't relevant

**Solutions**:
1. Increase `minRelevanceScore` threshold
2. Improve documentation in knowledge base
3. Add more specific documentation
4. Use more precise query terms

### Slow Performance

**Issue**: Context loading takes too long

**Solutions**:
1. Reduce `maxContextQueries` setting
2. Optimize Archon database indexes
3. Use faster embedding model
4. Cache common queries

## Tips for Best Results

1. **Keep docs updated**: Fresh documentation = better context
2. **Include examples**: Code examples are most valuable
3. **Document decisions**: Explain why, not just what
4. **Organize well**: Use clear categories and tags
5. **Test queries**: Verify important topics are findable

## Related Resources

- [RAG Integration Guide](../docs/RAG_INTEGRATION.md)
- [Archon Documentation](https://github.com/coleam00/Archon)
- [Knowledge Base Setup](../docs/RAG_INTEGRATION.md#knowledge-base-setup)
- [Slash Commands](/knowledge:search, /knowledge:add)

---

**Version**: 1.0.0
**Last Updated**: 2025-11-12
**Author**: Claude Code Community
**License**: MIT
