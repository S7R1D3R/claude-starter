---
description: Add new documentation sources to the RAG knowledge base
---

# Add to Knowledge Base

Help the user add documentation sources to Archon's knowledge base.

## Prerequisites

- Archon is running (http://localhost:3737)
- User has access to documentation sources
- Knowledge base project exists in Archon

## Source Types Supported

### 1. Websites
- Full site crawling with sitemap detection
- Single page capture
- Automatic code example extraction
- JavaScript rendering support

### 2. Files
- PDF documents
- Markdown files (.md)
- Word documents (.docx)
- Plain text files (.txt)
- Code files with documentation

### 3. Repositories
- GitHub repositories (public or with token)
- GitLab repositories
- README and docs folders
- Code examples and comments

## Instructions

1. **Identify Source Type**
   - Ask user what they want to add
   - Validate source accessibility
   - Determine best approach

2. **Prepare Source**
   - Check URL is accessible (for websites)
   - Verify file format is supported
   - Ensure repository permissions

3. **Add to Archon**
   - Use Archon UI or API
   - Configure processing options
   - Start indexing

4. **Monitor Processing**
   - Track progress
   - Report any errors
   - Verify completion

5. **Validate Addition**
   - Test search with relevant query
   - Verify content is indexed
   - Check embedding quality

## Adding Websites

### Process

```bash
# Option 1: Use Archon UI
Open: http://localhost:3737
→ Select Project
→ Click "Add Source"
→ Choose "Website"
→ Enter URL
→ Configure options
→ Click "Process"

# Option 2: Use API
curl -X POST http://localhost:8181/api/sources/website \
  -H "Content-Type: application/json" \
  -d '{
    "project_id": "your-project-id",
    "url": "https://docs.example.com",
    "crawl_sitemap": true,
    "max_pages": 500,
    "extract_code": true
  }'
```

### Example Interaction

**User:** "Add the React documentation to our knowledge base"

**Response:**
```
Adding React documentation to knowledge base...

🔍 Analyzing source: https://react.dev

✓ Valid website detected
✓ Sitemap found: https://react.dev/sitemap.xml
✓ Estimated pages: 247
✓ Code examples: Yes

Starting crawl and indexing...

Progress:
[████████░░] 80% - Processing 197/247 pages
```

Wait for completion, then:

```
✅ Complete!

Summary:
- Pages indexed: 247
- Code examples extracted: 1,842
- Average processing time: 0.8s/page
- Total size: 12.4 MB

The React documentation is now searchable!

Test it: /knowledge:search "how to use hooks"
```

### Website Configuration Options

```json
{
  "crawl_sitemap": true,     // Follow sitemap.xml
  "max_pages": 500,           // Limit pages
  "extract_code": true,       // Extract code blocks
  "follow_links": true,       // Follow internal links
  "render_javascript": false, // Enable for SPAs
  "exclude_patterns": [       // Skip URLs matching
    "/blog/",
    "/changelog/"
  ]
}
```

## Adding Files

### Process

```bash
# Option 1: Use Archon UI
Open: http://localhost:3737
→ Select Project
→ Click "Add Source"
→ Choose "Upload File"
→ Select file(s)
→ Click "Process"

# Option 2: Use API
curl -X POST http://localhost:8181/api/sources/file \
  -F "project_id=your-project-id" \
  -F "file=@/path/to/document.pdf"
```

### Example Interaction

**User:** "Add our API specification PDF to the knowledge base"

**Response:**
```
Adding API specification document...

📄 File: api-spec-v2.pdf
📏 Size: 3.2 MB
📃 Type: PDF

Processing...
✓ PDF parsed: 45 pages
✓ Text extracted: 18,500 words
✓ Code examples found: 23
✓ Diagrams identified: 8

Creating embeddings...
[████████████] 100% - 45/45 pages

✅ Complete!

Summary:
- Pages: 45
- Sections: 127
- API endpoints documented: 34
- Code examples: 23

The API specification is now searchable!

Test it: /knowledge:search "POST /api/users endpoint"
```

### Supported File Formats

| Format | Extensions | Notes |
|--------|------------|-------|
| PDF | .pdf | Full text extraction |
| Markdown | .md | Native support |
| Word | .docx | Requires conversion |
| Text | .txt | Direct processing |
| Code | .js, .py, etc | Comment extraction |

## Adding Repositories

### Process

```bash
# Option 1: Use Archon UI
Open: http://localhost:3737
→ Select Project
→ Click "Add Source"
→ Choose "Repository"
→ Enter repo URL
→ Optionally add GitHub token
→ Configure options
→ Click "Process"

# Option 2: Use API
curl -X POST http://localhost:8181/api/sources/repository \
  -H "Content-Type: application/json" \
  -d '{
    "project_id": "your-project-id",
    "url": "https://github.com/organization/repo",
    "token": "github_pat_...",
    "include_patterns": ["docs/**", "README.md"],
    "extract_code_comments": true
  }'
```

### Example Interaction

**User:** "Add our internal component library docs from GitHub"

**Response:**
```
Adding GitHub repository documentation...

🔗 Repository: github.com/company/component-library
🔐 Authentication: Using provided token
📁 Branch: main

Scanning repository...
✓ Total files: 1,247
✓ Documentation files: 89
✓ README files: 12
✓ Code examples: 156

Processing documentation...
[████████████] 100% - 89/89 files

Extracting code comments...
✓ Documented components: 67
✓ Type definitions: 234
✓ Usage examples: 156

✅ Complete!

Summary:
- Documentation files: 89
- Components documented: 67
- Code examples: 156
- Total chunks: 523

The component library docs are now searchable!

Test it: /knowledge:search "Button component props"
```

### Repository Configuration Options

```json
{
  "branch": "main",                    // Default branch
  "include_patterns": [                // Files to include
    "docs/**",
    "README.md",
    "*.md"
  ],
  "exclude_patterns": [                // Files to skip
    "node_modules/**",
    "dist/**"
  ],
  "extract_code_comments": true,       // Parse JSDoc, docstrings
  "include_code_examples": true,       // Extract example code
  "follow_links": true                 // Process linked repos
}
```

## Batch Addition

For adding multiple sources at once:

**User:** "Add all our documentation: the main website, API PDF, and GitHub repo"

**Response:**
```
Adding multiple documentation sources...

📋 Batch Job Created:
1. Website: https://docs.company.com
2. File: api-specification.pdf
3. Repository: github.com/company/docs

Processing in parallel...

[1/3] Website crawling...
      [████████░░] 75% - 380/500 pages

[2/3] PDF processing...
      [████████████] 100% - Complete

[3/3] Repository cloning...
      [██████░░░░] 60% - 54/89 files

---

✅ All sources processed!

Total Summary:
- Websites: 1 (500 pages)
- Files: 1 (45 pages)
- Repositories: 1 (89 files)
- Total chunks: 2,847
- Total code examples: 678
- Processing time: 4m 32s

All documentation is now in the knowledge base!

Try searching: /knowledge:search "getting started"
```

## Update Existing Sources

To refresh content that's already in the knowledge base:

**User:** "/knowledge:add https://docs.framework.com" (already exists)

**Response:**
```
Source already exists in knowledge base.

📊 Current Status:
- Last updated: 3 days ago
- Pages: 247
- Status: Stale (updates available)

Would you like to:
1. ♻️  Refresh (re-crawl and update)
2. 🗑️  Delete and re-add
3. ⏭️  Skip (keep existing)

Recommend: Refresh to get latest updates
```

If user chooses refresh:
```
Refreshing documentation...

🔄 Re-crawling: https://docs.framework.com
✓ Detected changes: 18 pages modified, 3 new pages
✓ Re-processing: 21 pages
✓ Unchanged: 226 pages (skipped)

✅ Refresh complete!

Changes:
- Updated pages: 18
- New pages: 3
- Removed pages: 0
- New code examples: 34

Knowledge base is up to date!
```

## Monitoring & Validation

After adding sources, help users verify:

```
🔍 Validating knowledge base addition...

Running test queries:
1. "getting started" → ✓ 5 results found
2. "API authentication" → ✓ 3 results found
3. "code examples" → ✓ 12 results found

Checking embedding quality:
✓ Average relevance score: 0.82 (good)
✓ Coverage: 98% of content embedded
✓ Duplicates: 0 detected

Status: ✅ All checks passed

The documentation is properly indexed and searchable.
```

## Troubleshooting

### Website Crawl Fails

```
❌ Error: Cannot crawl website

Common issues:
1. robots.txt blocks crawlers → Try single page mode
2. JavaScript required → Enable JS rendering
3. Authentication required → Provide credentials
4. Rate limiting → Reduce concurrency

Suggested fix:
- Try: Enable JavaScript rendering
- Or: Download docs as PDF and upload instead
```

### File Upload Fails

```
❌ Error: Cannot process file

Possible causes:
1. Unsupported file format → Convert to PDF/MD
2. File too large (>50MB) → Split into smaller files
3. Corrupted file → Re-export or re-download
4. Password protected → Remove password first

Suggested fix:
- Check file format: {detected_format}
- Maximum size: 50 MB
- Your file size: {file_size}
```

### Repository Access Denied

```
❌ Error: Cannot access repository

Authentication required:
1. Repository is private
2. Need GitHub token with 'repo' scope

To fix:
1. Create token: https://github.com/settings/tokens
2. Scopes needed: 'repo' (full)
3. Add token to request
4. Try again

Example:
/knowledge:add github.com/org/repo --token ghp_your_token
```

## Best Practices

When helping users add documentation:

✅ **DO:**
- Verify sources are accessible before processing
- Estimate processing time for large sources
- Monitor progress and report status
- Validate results after completion
- Suggest test queries to verify

❌ **DON'T:**
- Process without checking file size/page count
- Add duplicate sources without notification
- Skip validation after adding
- Ignore errors or warnings
- Add without explaining what's being indexed

## Content Quality Tips

Share these tips with users:

**For Websites:**
- Official docs are better than blog posts
- Recent content is more valuable
- Exclude marketing/sales pages
- Include code examples and tutorials

**For Files:**
- PDFs should have selectable text (not scanned images)
- Break large documents into logical sections
- Include version numbers in filenames
- Keep documentation up to date

**For Repositories:**
- Focus on docs/ folders and README files
- Include code comments and docstrings
- Add usage examples
- Keep documentation close to code

## Next Steps

After successfully adding documentation:

```
✅ Documentation added successfully!

Next steps:
1. 🔍 Test search: /knowledge:search "your topic"
2. 🤖 Use in Claude: Context will auto-enhance prompts
3. 📅 Set refresh schedule: Recommend weekly for active docs
4. 📊 Monitor usage: Check which docs are most queried

Want to add more sources? Just let me know!
```

---

**Remember**: The quality of RAG results depends on the quality of indexed documentation. Help users curate high-quality, relevant content!
