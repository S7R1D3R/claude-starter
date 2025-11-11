---
description: Run test suite and report results
---

# Run Tests

Execute the project's test suite and provide comprehensive results.

## Auto-Detect Test Framework

Check for test frameworks and run appropriate command:

### JavaScript/TypeScript
- **package.json** scripts:
  - `npm test` or `yarn test`
  - `npm run test:unit`
  - `npm run test:integration`
- **Jest**: `jest.config.js` → `jest`
- **Vitest**: `vitest.config.ts` → `vitest run`
- **Mocha**: `.mocharc.json` → `mocha`
- **Cypress**: `cypress.config.js` → `cypress run`
- **Playwright**: `playwright.config.ts` → `playwright test`

### Python
- **pytest**: `pytest.ini`, `pyproject.toml` → `pytest`
- **unittest**: Discover with → `python -m unittest discover`
- **nose**: → `nosetests`
- **tox**: `tox.ini` → `tox`

### Rust
- **Cargo**: `Cargo.toml` → `cargo test`

### Go
- **Go modules**: `go.mod` → `go test ./...`
- **Go packages**: → `go test -v`

### Ruby
- **RSpec**: `.rspec` → `rspec`
- **Minitest**: → `ruby -Itest test/**/*_test.rb`

### Java
- **Maven**: `pom.xml` → `mvn test`
- **Gradle**: `build.gradle` → `gradle test`
- **JUnit**: Discover and run

### PHP
- **PHPUnit**: `phpunit.xml` → `phpunit`

## Test Execution

1. **Detect** test framework
2. **Check** test files exist
3. **Run** tests with appropriate command
4. **Capture** output
5. **Parse** results
6. **Report** summary

## Coverage (if available)

If coverage tool configured:
- Run tests with coverage: `jest --coverage`, `pytest --cov`
- Report coverage percentage
- Highlight uncovered files
- Suggest coverage improvements if <80%

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧪 RUNNING TESTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Test Framework: Jest
Command: npm test

✓ User Authentication (auth.test.js)
  ✓ should login with valid credentials
  ✓ should reject invalid password
  ✓ should handle session timeout

✗ Payment Processing (payment.test.js)
  ✓ should process valid payment
  ✗ should handle payment failure
    Expected: 400
    Received: 500

✓ API Integration (api.test.js)
  ✓ should fetch user data
  ✓ should handle network errors

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Results: 8 passed, 1 failed, 0 skipped
Time: 2.34s
Coverage: 87.3%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ TESTS FAILED

Fix the failing test before committing:
  • payment.test.js:23 - Incorrect error code check

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Failed Test Handling

When tests fail:
1. Show which tests failed
2. Display error messages
3. Suggest fixes if obvious
4. Offer to help debug
5. Block commit recommendation until fixed

## Watch Mode (Optional)

If framework supports watch mode:
- Suggest running in watch mode for development
- Command: `npm test -- --watch` or `pytest --watch`

## Arguments

- `/quality:test` - Run all tests
- `/quality:test src/auth` - Run specific test suite
- `/quality:test --watch` - Run in watch mode
- `/quality:test --coverage` - Run with coverage report
- `/quality:test --verbose` - Detailed output

**IMPORTANT**: If tests fail, clearly communicate that changes should not be committed until tests pass.
