# Testing Skill

Transform Claude into a testing expert with knowledge of test strategies, frameworks, and best practices.

## Expertise

This skill provides Claude with comprehensive knowledge of:
- Test-driven development (TDD)
- Unit testing strategies
- Integration testing
- End-to-end testing
- Test coverage analysis
- Mocking and stubbing
- Test frameworks for all major languages
- Testing best practices

## When to Use

Invoke this skill when:
- Writing tests
- Improving test coverage
- Debugging test failures
- Designing test strategies
- Setting up testing infrastructure

## Testing Principles

### Test Pyramid

```
         /\
        /E2E\       Few: Slow, brittle, expensive
       /------\
      /  INT   \    Some: Medium speed, focused
     /----------\
    /   UNIT     \  Many: Fast, isolated, cheap
   /--------------\
```

### FIRST Principles

Tests should be:
- **F**ast - Run quickly
- **I**solated - Independent of each other
- **R**epeatable - Same result every time
- **S**elf-validating - Pass or fail clearly
- **T**imely - Written at the right time (preferably before code)

### AAA Pattern

Structure tests with:
- **Arrange**: Set up test data and conditions
- **Act**: Execute the code being tested
- **Assert**: Verify the results

## Test Strategies by Language

### JavaScript/TypeScript (Jest, Vitest, Mocha)

```javascript
describe('UserService', () => {
  describe('createUser', () => {
    it('should create user with valid data', () => {
      // Arrange
      const userData = { name: 'John', email: 'john@example.com' };

      // Act
      const user = userService.createUser(userData);

      // Assert
      expect(user).toMatchObject(userData);
      expect(user.id).toBeDefined();
    });

    it('should throw error for invalid email', () => {
      // Arrange
      const invalidData = { name: 'John', email: 'invalid' };

      // Act & Assert
      expect(() => userService.createUser(invalidData))
        .toThrow('Invalid email');
    });
  });
});
```

### Python (pytest, unittest)

```python
class TestUserService:
    def test_create_user_with_valid_data(self):
        # Arrange
        user_data = {'name': 'John', 'email': 'john@example.com'}

        # Act
        user = user_service.create_user(user_data)

        # Assert
        assert user.name == 'John'
        assert user.email == 'john@example.com'
        assert user.id is not None

    def test_create_user_with_invalid_email(self):
        # Arrange
        invalid_data = {'name': 'John', 'email': 'invalid'}

        # Act & Assert
        with pytest.raises(ValueError, match="Invalid email"):
            user_service.create_user(invalid_data)
```

### Go

```go
func TestCreateUser(t *testing.T) {
    t.Run("creates user with valid data", func(t *testing.T) {
        // Arrange
        userData := UserData{Name: "John", Email: "john@example.com"}

        // Act
        user, err := CreateUser(userData)

        // Assert
        assert.NoError(t, err)
        assert.Equal(t, "John", user.Name)
        assert.NotEmpty(t, user.ID)
    })
}
```

### Rust

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_create_user_with_valid_data() {
        // Arrange
        let user_data = UserData {
            name: "John".to_string(),
            email: "john@example.com".to_string(),
        };

        // Act
        let user = create_user(user_data).unwrap();

        // Assert
        assert_eq!(user.name, "John");
        assert!(!user.id.is_empty());
    }

    #[test]
    #[should_panic(expected = "Invalid email")]
    fn test_create_user_with_invalid_email() {
        let invalid_data = UserData {
            name: "John".to_string(),
            email: "invalid".to_string(),
        };
        create_user(invalid_data).unwrap();
    }
}
```

## Test Coverage Goals

- **Unit Tests**: 80%+ coverage
- **Integration Tests**: Critical paths covered
- **E2E Tests**: Happy path + critical flows

## Mocking Strategies

### When to Mock

- External APIs
- Database calls
- File system operations
- Time-dependent operations
- Third-party services

### When NOT to Mock

- Simple functions
- Pure logic
- Value objects
- DTOs

## Test Categories

### 1. Unit Tests

Test individual functions/methods in isolation:
- Fast execution
- No external dependencies
- Mock all dependencies
- Test one thing at a time

### 2. Integration Tests

Test components working together:
- Database integration
- API endpoints
- Service layer
- Use test database
- Slower than unit tests

### 3. End-to-End Tests

Test complete user workflows:
- Full application stack
- Real browser (Cypress, Playwright)
- Critical user journeys
- Slowest, most brittle

### 4. Performance Tests

Test system performance:
- Load testing
- Stress testing
- Benchmark tests

### 5. Security Tests

Test security measures:
- Authentication tests
- Authorization tests
- Input validation tests
- Injection attack prevention

## Test Naming Conventions

Format: `test_[function]_[scenario]_[expected]`

Examples:
- `test_login_with_valid_credentials_returns_token`
- `test_create_user_with_duplicate_email_raises_error`
- `test_calculate_total_with_empty_cart_returns_zero`

## Edge Cases to Test

Always test:
- **Empty input**: `[]`, `""`, `null`, `undefined`
- **Boundary values**: `0`, `-1`, `MAX_INT`
- **Invalid input**: Wrong types, malformed data
- **Large input**: Scalability
- **Concurrent access**: Race conditions
- **Error conditions**: Network failures, timeouts

## Test Data Management

### Use Factories/Builders

```javascript
function createUser(overrides = {}) {
  return {
    id: '123',
    name: 'Test User',
    email: 'test@example.com',
    ...overrides
  };
}
```

### Use Fixtures

For consistent test data across tests.

### Reset State

Clean up after each test to ensure isolation.

## Assertions Best Practices

- **Be Specific**: `expect(user.email).toBe('test@example.com')` not `expect(user).toBeTruthy()`
- **One Assertion Per Concept**: Test one behavior
- **Meaningful Messages**: Custom error messages when helpful
- **Avoid Logic**: Tests should be simple, no conditionals

## Common Testing Mistakes

❌ **Testing Implementation Details**
- Test behavior, not implementation

❌ **Tightly Coupled Tests**
- Tests should be independent

❌ **Slow Tests**
- Mock external dependencies

❌ **Flaky Tests**
- Avoid time dependencies, race conditions

❌ **Testing Framework Code**
- Don't test libraries, test your code

## Test Quality Metrics

Good tests are:
- **Readable**: Clear what's being tested
- **Maintainable**: Easy to update
- **Fast**: Quick feedback loop
- **Reliable**: Consistent results
- **Focused**: Test one thing

## Integration

This skill integrates with:
- `/quality:test` command
- `/dev:init` for test setup
- CI/CD pipelines
- Pre-commit hooks

## References

Based on:
- Test Driven Development (Kent Beck)
- Growing Object-Oriented Software (Freeman & Pryce)
- xUnit Test Patterns (Meszaros)
- Testing JavaScript Applications (Bodner)
