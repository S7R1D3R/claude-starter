---
description: Search project knowledge base for relevant documentation using RAG
---

# Knowledge Base Search

You are helping the user search the project's RAG-powered knowledge base (Archon).

## Prerequisites

Verify that Archon is running:
- Archon UI: http://localhost:3737
- Archon MCP: http://localhost:8051
- Knowledge base has been populated with documentation

If Archon is not running, inform the user and provide setup instructions from `docs/RAG_INTEGRATION.md`.

## Instructions

1. **Understand the Query**
   - Extract the main topic or question
   - Identify the type of information needed (concept, code example, API reference, etc.)
   - Consider context from the current conversation

2. **Query Archon**
   - Use semantic search (meaning-based, not just keywords)
   - Request relevant code examples when appropriate
   - Set appropriate relevance threshold (0.6-0.8)
   - Limit to top 5 most relevant results

3. **Present Results**
   - Show results ordered by relevance
   - Include document title and source
   - Display key excerpts (300-500 chars)
   - Show code examples when available
   - Include relevance scores to indicate confidence

4. **Provide Context**
   - Explain how results relate to the query
   - Highlight key takeaways
   - Connect results to current project context

5. **Suggest Next Steps**
   - Related topics to explore
   - More specific queries
   - Implementation guidance
   - Links to full documentation

## Response Format

Use this structure for presenting results:

```
📚 Knowledge Base Search Results

Query: "{user's query}"
Found: {N} relevant documents

─────────────────────────────────────────────────────

1. {Document Title} (Relevance: {XX}%)
   Source: {source path or URL}

   {Key excerpt from document...}

   {Code example if available:}
   ```{language}
   {code}
   ```

   📖 [View full document]

─────────────────────────────────────────────────────

2. {Next document...}

─────────────────────────────────────────────────────

💡 Key Takeaways:
- {Important point 1}
- {Important point 2}
- {Important point 3}

🔍 Related Topics:
- {Related topic 1}
- {Related topic 2}

Next Steps:
{Suggested actions based on results}
```

## Example Interaction

**User Query:**
```
/knowledge:search how to handle database transactions
```

**Your Response:**
```
📚 Knowledge Base Search Results

Query: "how to handle database transactions"
Found: 3 relevant documents

─────────────────────────────────────────────────────

1. Database Transaction Patterns (Relevance: 94%)
   Source: docs/database/transactions.md

   "Our application uses the Unit of Work pattern for database transactions.
   All operations within a request are wrapped in a transaction that commits
   on success or rolls back on error."

   Example Code:
   ```typescript
   async function createUser(data: UserData) {
     return await db.transaction(async (trx) => {
       const user = await trx.insert('users', data);
       await trx.insert('audit_log', { action: 'user_created', userId: user.id });
       return user;
     });
   }
   ```

   📖 [View full document: docs/database/transactions.md]

─────────────────────────────────────────────────────

2. Error Handling in Database Operations (Relevance: 87%)
   Source: docs/patterns/error-handling.md

   "Always wrap database operations in try-catch blocks and implement proper
   rollback logic. Use specific error types to distinguish between different
   failure modes..."

   Example Code:
   ```typescript
   try {
     await db.transaction(/* ... */);
   } catch (error) {
     if (error instanceof UniqueConstraintError) {
       throw new ConflictError('User already exists');
     }
     throw new DatabaseError('Transaction failed', error);
   }
   ```

─────────────────────────────────────────────────────

3. Connection Pooling Best Practices (Relevance: 72%)
   Source: docs/database/connections.md

   "Configure connection pools with appropriate timeouts for transaction
   scenarios. Default pool size is 20 connections with 30s idle timeout..."

─────────────────────────────────────────────────────

💡 Key Takeaways:
- Use the Unit of Work pattern for multi-step transactions
- Always implement proper error handling and rollback logic
- Wrap transactions in try-catch blocks with specific error types
- Configure connection pools appropriately for transaction workloads

🔍 Related Topics:
- Database connection pooling
- Error handling patterns
- Unit of Work pattern implementation
- Database migration strategies

Would you like me to:
1. Show you how to implement this pattern in your current code?
2. Explain the Unit of Work pattern in more detail?
3. Search for more information about error handling?
```

## Search Strategies

### For Conceptual Questions
- Query: Broad conceptual terms
- Focus: Documentation and architecture guides
- Example: "microservices architecture patterns"

### For Implementation Help
- Query: Specific technical terms
- Focus: Code examples and tutorials
- Example: "implement JWT authentication middleware"

### For API Reference
- Query: Specific function/class names
- Focus: API documentation and type definitions
- Example: "UserService.authenticate method"

### For Troubleshooting
- Query: Error symptoms or patterns
- Focus: Error handling docs and common issues
- Example: "database connection timeout errors"

## Error Handling

If Archon is unavailable or returns no results:

```
⚠️ Knowledge Base Unavailable

The RAG knowledge base (Archon) is not responding.

Possible causes:
- Archon services are not running
- MCP connection is not configured
- Network connectivity issues

To fix:
1. Check if Archon is running:
   docker-compose ps

2. Verify Archon MCP configuration in ~/.claude.json:
   {
     "mcpServers": {
       "archon": {
         "type": "http",
         "url": "http://localhost:8051"
       }
     }
   }

3. See setup guide: docs/RAG_INTEGRATION.md

Would you like me to help you set up Archon?
```

If no relevant results found:

```
🔍 No Relevant Results Found

I searched the knowledge base but didn't find documentation matching:
"{query}"

This might mean:
- The topic isn't documented yet
- Try a different search term or phrase
- The documentation needs to be added to Archon

Suggestions:
1. Try a broader search term
2. Search for related concepts
3. Add this documentation to the knowledge base with /knowledge:add

Would you like to try a different search?
```

## Quality Checks

Before presenting results, verify:
- ✅ Results are actually relevant to the query
- ✅ Code examples are complete and syntactically valid
- ✅ Sources are accurate and accessible
- ✅ Relevance scores make sense (>60%)
- ✅ Excerpts provide meaningful context

## Implementation Notes

The knowledge base search uses:
- **Vector embeddings** for semantic similarity
- **Hybrid search** combining semantic + keyword matching
- **Result reranking** to prioritize most relevant content
- **Contextual chunking** for optimal excerpt extraction

This provides much better results than simple keyword search!

## Tips for Users

Share these tips when appropriate:
- **Be specific**: "How to implement JWT auth" > "authentication"
- **Use natural language**: Ask questions as you would to a person
- **Include context**: Mention your specific use case or framework
- **Iterate**: Refine searches based on initial results
- **Add documentation**: The more docs in the knowledge base, the better results

---

**Remember**: The goal is to help users discover relevant information quickly and implement it correctly!
