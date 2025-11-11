---
description: Intelligent code refactoring with best practices
---

# Intelligent Refactoring

Perform systematic code refactoring following industry best practices and SOLID principles.

## Refactoring Process

### 1. Understand Scope

From $ARGUMENTS or current context:
- Specific file/function to refactor
- Module or component
- Entire codebase (use with caution)

### 2. Analyze Current Code

Before refactoring:
- Read and understand the code
- Identify code smells
- Check for anti-patterns
- Review test coverage
- Note dependencies

### 3. Identify Refactoring Opportunities

Common code smells:
- **Long functions** (>50 lines)
- **Large classes** (>300 lines)
- **Duplicated code**
- **Long parameter lists** (>3-4 parameters)
- **Complex conditionals**
- **Deep nesting** (>3 levels)
- **Magic numbers**
- **Inappropriate intimacy**
- **Feature envy**

### 4. Plan Refactoring Strategy

Choose appropriate refactoring:
- **Extract Method** - Break down long functions
- **Extract Class** - Separate concerns
- **Rename** - Improve clarity
- **Move Method** - Better organization
- **Replace Conditional with Polymorphism**
- **Introduce Parameter Object**
- **Remove Dead Code**
- **Simplify Conditional Expressions**

### 5. Apply SOLID Principles

Ensure code follows:
- **S**ingle Responsibility Principle
- **O**pen/Closed Principle
- **L**iskov Substitution Principle
- **I**nterface Segregation Principle
- **D**ependency Inversion Principle

### 6. Refactor Incrementally

For each refactoring:
1. **Run tests** - Ensure they pass
2. **Make one change** - Single refactoring at a time
3. **Run tests again** - Verify nothing broke
4. **Commit** - Small, focused commits
5. **Repeat**

## Refactoring Examples

### Extract Method

**Before:**
```javascript
function processOrder(order) {
  // Validate order (15 lines)
  // Calculate totals (20 lines)
  // Apply discounts (10 lines)
  // Save to database (15 lines)
}
```

**After:**
```javascript
function processOrder(order) {
  validateOrder(order);
  const totals = calculateTotals(order);
  const finalAmount = applyDiscounts(totals, order);
  saveOrder(order, finalAmount);
}

function validateOrder(order) { /* ... */ }
function calculateTotals(order) { /* ... */ }
function applyDiscounts(totals, order) { /* ... */ }
function saveOrder(order, amount) { /* ... */ }
```

### Extract Class

**Before:**
```python
class User:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.street = ""
        self.city = ""
        self.zip = ""
```

**After:**
```python
class User:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.address = Address()

class Address:
    def __init__(self):
        self.street = ""
        self.city = ""
        self.zip = ""
```

### Simplify Conditional

**Before:**
```javascript
if (user.role === 'admin' || user.role === 'moderator' || user.role === 'owner') {
  allowAccess();
}
```

**After:**
```javascript
const privilegedRoles = ['admin', 'moderator', 'owner'];
if (privilegedRoles.includes(user.role)) {
  allowAccess();
}

// Or better:
if (user.hasPrivilegedAccess()) {
  allowAccess();
}
```

## Safety Checks

Before refactoring:
- [ ] Tests exist and pass
- [ ] Code is in version control
- [ ] Branch is created for refactoring
- [ ] Team is notified (if large refactoring)

During refactoring:
- [ ] Run tests after each change
- [ ] Keep commits small and focused
- [ ] Don't change functionality
- [ ] Document non-obvious changes

After refactoring:
- [ ] All tests pass
- [ ] Code review performed
- [ ] Performance unchanged or improved
- [ ] Documentation updated

## Metrics to Improve

Track improvements in:
- **Cyclomatic Complexity** - Reduce branching
- **Lines of Code** - Shorter functions
- **Code Duplication** - DRY principle
- **Test Coverage** - Maintain or improve
- **Coupling** - Reduce dependencies
- **Cohesion** - Increase module focus

## Automated Refactoring Tools

Leverage IDE/language tools:
- **TypeScript**: VS Code refactoring tools
- **Python**: rope, autoflake
- **Java**: IntelliJ IDEA refactoring
- **Rust**: rust-analyzer
- **Go**: gofmt, goimports

## Arguments

- `/ai:refactor src/auth.js` - Refactor specific file
- `/ai:refactor --extract-methods` - Focus on extracting methods
- `/ai:refactor --solid` - Apply SOLID principles
- `/ai:refactor --dry-run` - Suggest refactorings without applying

## Output

Provide:
1. **Analysis** of current code quality
2. **Recommendations** with priority
3. **Before/After** examples
4. **Step-by-step** refactoring plan
5. **Testing strategy** to verify changes

**IMPORTANT**: Never change functionality during refactoring. Only improve structure and readability. Always run tests after each change.
