---
description: Explain complex code sections in detail
---

# Explain Code

Provide detailed, educational explanations of complex code sections.

## Explanation Process

### 1. Identify Code to Explain

From $ARGUMENTS:
- Specific file path
- Function/class name
- Line numbers
- Component name

If not specified, ask what needs explanation.

### 2. Read and Analyze Code

Load the code section with context:
- Read the file
- Understand surrounding code
- Check imports/dependencies
- Review related files if needed

### 3. Provide Multi-Level Explanation

#### Level 1: High-Level Overview (ELI5)
Explain in simple terms what the code does:
```
This function handles user login. It checks if the username and password
are correct, and if so, creates a session for the user.
```

#### Level 2: Step-by-Step Breakdown
Walk through the code line by line:
```
1. Line 5: Extract username and password from request
2. Line 7: Query database for user with that username
3. Line 9: If no user found, return error
4. Line 12: Compare password with stored hash
5. Line 15: If password matches, create session token
6. Line 18: Return success with session token
```

#### Level 3: Technical Details
Explain algorithms, patterns, and edge cases:
```
- Uses bcrypt for password hashing (lines 12-14)
- Implements JWT for session management (line 15)
- Handles race conditions with database locks (line 8)
- Prevents timing attacks by always checking password (line 12)
```

### 4. Explain Design Decisions

Why was it written this way?
- What problem does it solve?
- Why this algorithm/pattern?
- What are the trade-offs?
- Are there alternatives?

### 5. Identify Potential Issues

Point out:
- Edge cases not handled
- Performance concerns
- Security vulnerabilities
- Maintainability issues
- Unclear naming

### 6. Provide Context

Explain:
- Where this fits in the larger system
- What calls this function
- What this function calls
- Related components

## Explanation Format

```markdown
## Code Explanation: [Function/Class Name]

### Overview
[High-level description]

### What It Does
[Step-by-step walkthrough]

### How It Works

\`\`\`language
[Code with inline comments]
\`\`\`

1. **[Step 1 Title]**
   - [Explanation]
   - Why: [Reasoning]

2. **[Step 2 Title]**
   - [Explanation]
   - Why: [Reasoning]

[Continue...]

### Key Concepts

- **[Concept 1]**: [Explanation]
- **[Concept 2]**: [Explanation]

### Design Patterns Used

- [Pattern name]: [How it's applied]

### Edge Cases Handled

- [Case 1]: [How it's handled]
- [Case 2]: [How it's handled]

### Potential Improvements

1. [Suggestion with explanation]
2. [Suggestion with explanation]

### Related Code

- `[file.js]`: [How it's related]
- `[other.js]`: [How it's related]

### Example Usage

\`\`\`language
[Example of using this code]
\`\`\`

### Diagram (if complex)

\`\`\`
[ASCII diagram or flowchart]
\`\`\`
```

## Complex Code Scenarios

### Algorithms
- Explain time/space complexity
- Show visual representation
- Provide step-by-step trace
- Compare with alternatives

### Async Code
- Explain execution flow
- Show promise chain
- Identify race conditions
- Explain error handling

### Recursive Functions
- Explain base case
- Explain recursive case
- Show call stack
- Provide iterative alternative

### Design Patterns
- Name the pattern
- Explain why it's used
- Show structure
- Provide simpler alternative

### Database Queries
- Explain query logic
- Show execution plan
- Identify performance issues
- Suggest optimizations

## Interactive Explanation

After initial explanation, offer:
- "Would you like me to explain any specific part in more detail?"
- "Should I show alternative implementations?"
- "Would a diagram help?"
- "Do you want to see test cases?"

## Visual Aids

Create when helpful:
- **Flowcharts** for complex logic
- **Sequence diagrams** for interactions
- **State diagrams** for state machines
- **Tree diagrams** for recursive functions

Example ASCII diagram:
```
┌─────────────┐
│   Request   │
└──────┬──────┘
       │
       ▼
┌─────────────┐     ┌──────────────┐
│  Validate   │────>│   Rejected   │
└──────┬──────┘     └──────────────┘
       │ Valid
       ▼
┌─────────────┐
│   Process   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Response  │
└─────────────┘
```

## Arguments

- `/ai:explain src/auth.js` - Explain entire file
- `/ai:explain src/auth.js:45` - Explain specific line
- `/ai:explain calculateTotal` - Explain function by name
- `/ai:explain --simple` - ELI5 mode
- `/ai:explain --technical` - Deep technical explanation

**IMPORTANT**: Tailor explanation depth to the complexity of the code. Always be clear, accurate, and educational.
