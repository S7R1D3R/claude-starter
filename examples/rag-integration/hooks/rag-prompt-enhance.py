#!/usr/bin/env python3
"""
RAG-Enhanced Prompt Hook for Claude Code + Archon Integration

This hook automatically queries the Archon knowledge base to add relevant
context to user prompts before they're sent to Claude.

Setup:
1. Install and run Archon: https://github.com/coleam00/Archon
2. Populate knowledge base with project docs
3. Copy this file to .claude/hooks/rag-prompt-enhance.py
4. Enable in .claude/settings.json:
   {
     "hooks": {
       "userPromptSubmit": {
         "command": ".claude/hooks/rag-prompt-enhance.py",
         "enabled": true
       }
     }
   }

Author: Claude Code Community
License: MIT
"""

import sys
import json
import requests
from typing import Dict, List, Optional
from urllib.parse import urljoin

# Configuration
ARCHON_API_BASE = "http://localhost:8181/api"
ARCHON_MCP_BASE = "http://localhost:8051"
MAX_RESULTS = 3
MIN_RELEVANCE = 0.65
REQUEST_TIMEOUT = 5  # seconds

# Feature flags
ENABLE_CODE_EXAMPLES = True
ENABLE_RELEVANCE_SCORES = True
VERBOSE_LOGGING = False


def log_debug(message: str):
    """Log debug messages to stderr"""
    if VERBOSE_LOGGING:
        print(f"[RAG Hook] {message}", file=sys.stderr)


def search_knowledge(query: str, max_results: int = MAX_RESULTS) -> List[Dict]:
    """
    Query Archon's knowledge base for relevant documentation

    Args:
        query: Search query string
        max_results: Maximum number of results to return

    Returns:
        List of search results with title, excerpt, score, etc.
    """
    try:
        log_debug(f"Searching knowledge base for: {query}")

        response = requests.post(
            urljoin(ARCHON_API_BASE, "/knowledge/search"),
            json={
                "query": query,
                "limit": max_results,
                "min_relevance": MIN_RELEVANCE,
                "include_code_examples": ENABLE_CODE_EXAMPLES
            },
            timeout=REQUEST_TIMEOUT
        )

        if response.status_code == 200:
            results = response.json().get("results", [])
            log_debug(f"Found {len(results)} relevant results")
            return results

        log_debug(f"Search returned status {response.status_code}")
        return []

    except requests.exceptions.Timeout:
        log_debug("Knowledge search timed out")
        return []

    except requests.exceptions.ConnectionError:
        log_debug("Cannot connect to Archon (is it running?)")
        return []

    except Exception as e:
        log_debug(f"Knowledge search error: {e}")
        return []


def format_context(results: List[Dict]) -> str:
    """
    Format search results into readable context

    Args:
        results: List of search results from Archon

    Returns:
        Formatted context string to append to prompt
    """
    if not results:
        return ""

    lines = [
        "",
        "=" * 70,
        "📚 RELEVANT CONTEXT FROM PROJECT KNOWLEDGE BASE",
        "=" * 70,
        ""
    ]

    for i, result in enumerate(results, 1):
        # Title and source
        title = result.get("title", "Untitled")
        source = result.get("source", "Unknown source")
        lines.append(f"{i}. {title}")
        lines.append(f"   Source: {source}")

        # Relevance score (optional)
        if ENABLE_RELEVANCE_SCORES:
            score = result.get("score", 0)
            lines.append(f"   Relevance: {score:.0%}")

        # Content excerpt
        excerpt = result.get("excerpt", result.get("content", ""))
        if excerpt:
            # Wrap long excerpts
            max_excerpt_length = 300
            if len(excerpt) > max_excerpt_length:
                excerpt = excerpt[:max_excerpt_length] + "..."

            lines.append(f"   {excerpt}")

        # Code example (if available)
        if ENABLE_CODE_EXAMPLES and "code_example" in result:
            code = result["code_example"]
            language = result.get("language", "")

            lines.append("")
            lines.append(f"   Example Code:")
            lines.append(f"   ```{language}")
            lines.append(f"   {code}")
            lines.append(f"   ```")

        # Link to full document
        if "url" in result:
            lines.append(f"   📖 Full document: {result['url']}")

        lines.append("")

    lines.extend([
        "=" * 70,
        "END CONTEXT",
        "=" * 70,
        ""
    ])

    return "\n".join(lines)


def should_enhance_prompt(prompt: str) -> bool:
    """
    Determine if a prompt should be enhanced with RAG

    Skip enhancement for:
    - Very short prompts (< 10 chars)
    - Meta/system commands
    - Greetings
    """
    if len(prompt) < 10:
        return False

    # Skip for meta commands
    skip_patterns = [
        "/help",
        "/clear",
        "/exit",
        "hello",
        "hi",
        "hey",
        "thanks",
        "thank you"
    ]

    prompt_lower = prompt.lower().strip()
    for pattern in skip_patterns:
        if prompt_lower.startswith(pattern) or prompt_lower == pattern:
            return False

    return True


def enhance_prompt(original_prompt: str) -> tuple[str, Optional[str]]:
    """
    Add relevant context to user prompt

    Args:
        original_prompt: Original user prompt

    Returns:
        Tuple of (enhanced_prompt, status_message)
    """
    # Check if enhancement is needed
    if not should_enhance_prompt(original_prompt):
        log_debug("Skipping enhancement for short/meta prompt")
        return original_prompt, None

    # Search for relevant knowledge
    results = search_knowledge(original_prompt)

    if not results:
        log_debug("No relevant context found")
        return original_prompt, None

    # Format and append context
    context = format_context(results)
    enhanced = original_prompt + "\n" + context

    status_msg = f"✨ Added {len(results)} relevant document(s) from knowledge base"

    return enhanced, status_msg


def main():
    """Main hook execution"""
    try:
        # Read hook input
        input_data = json.loads(sys.stdin.read())
        prompt = input_data.get("prompt", "")

        log_debug(f"Processing prompt: {prompt[:50]}...")

        # Enhance prompt with RAG
        enhanced_prompt, status_message = enhance_prompt(prompt)

        # Prepare response
        result = {
            "prompt": enhanced_prompt
        }

        if status_message:
            result["message"] = status_message

        # Output result
        print(json.dumps(result))
        sys.exit(0)

    except json.JSONDecodeError:
        log_debug("Invalid JSON input")
        # Return original input on error
        print(json.dumps({"prompt": sys.stdin.read()}))
        sys.exit(0)

    except Exception as e:
        log_debug(f"Unexpected error: {e}")
        # Fail gracefully - return original prompt
        print(json.dumps({"prompt": ""}))
        sys.exit(0)


if __name__ == '__main__':
    main()
