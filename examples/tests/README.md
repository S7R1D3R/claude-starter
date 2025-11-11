# Test Infrastructure Examples

This directory contains example test configurations and test files for popular testing frameworks across different languages.

## Directory Structure

```
examples/tests/
├── python/           # Python/pytest examples
│   ├── pytest.ini           # Pytest configuration
│   └── test_example.py      # Example test file
├── javascript/       # JavaScript/Jest examples
│   ├── jest.config.js       # Jest configuration
│   └── example.test.js      # Example test file
├── rust/            # Rust testing examples
│   └── lib.rs              # Example tests (inline)
└── go/              # Go testing examples
    └── example_test.go     # Example test file
```

## Using These Examples

### Python (pytest)

**1. Install pytest:**
```bash
pip install pytest pytest-cov pytest-mock
```

**2. Copy configuration:**
```bash
cp examples/tests/python/pytest.ini .
```

**3. Create tests directory:**
```bash
mkdir -p tests
cp examples/tests/python/test_example.py tests/
```

**4. Run tests:**
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test
pytest tests/test_example.py::test_addition

# Run with markers
pytest -m unit  # Only unit tests
pytest -m "not slow"  # Exclude slow tests
```

**Key features:**
- Coverage reporting (80% threshold)
- Test markers for categorization
- Parametrized tests
- Fixtures for setup/teardown
- Comprehensive assertions

---

### JavaScript (Jest)

**1. Install Jest:**
```bash
npm install --save-dev jest @types/jest
# or
yarn add --dev jest @types/jest
```

**2. Copy configuration:**
```bash
cp examples/tests/javascript/jest.config.js .
```

**3. Create tests:**
```bash
mkdir -p __tests__
cp examples/tests/javascript/example.test.js __tests__/
```

**4. Add script to package.json:**
```json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage"
  }
}
```

**5. Run tests:**
```bash
# Run all tests
npm test

# Watch mode
npm run test:watch

# With coverage
npm run test:coverage

# Specific test
npm test -- example.test.js
```

**Key features:**
- Coverage thresholds (80%)
- Snapshot testing
- Async test support
- Mocking capabilities
- Parametrized tests with test.each

---

### Rust (cargo test)

**1. Project structure:**
```
my-project/
├── Cargo.toml
├── src/
│   └── lib.rs  (or main.rs)
└── tests/
    └── integration_test.rs
```

**2. Copy example:**
```bash
# For unit tests (in src/lib.rs)
cat examples/tests/rust/lib.rs >> src/lib.rs

# For integration tests
mkdir -p tests
cp examples/tests/rust/lib.rs tests/integration_test.rs
```

**3. Run tests:**
```bash
# Run all tests
cargo test

# Run specific test
cargo test test_add

# Run with output
cargo test -- --nocapture

# Run ignored tests
cargo test -- --ignored

# Run tests in parallel
cargo test -- --test-threads=4
```

**Key features:**
- Unit tests inline with code (#[cfg(test)])
- Integration tests in tests/ directory
- Result-based testing
- should_panic attribute
- Benchmark tests
- Doc tests in comments

---

### Go (go test)

**1. Project structure:**
```
my-project/
├── go.mod
├── example.go
└── example_test.go
```

**2. Copy example:**
```bash
cp examples/tests/go/example_test.go .
```

**3. Run tests:**
```bash
# Run all tests
go test

# Verbose output
go test -v

# With coverage
go test -cover
go test -coverprofile=coverage.out
go tool cover -html=coverage.out

# Run specific test
go test -run TestAdd

# Run benchmarks
go test -bench=.

# Parallel execution
go test -parallel 4

# Short mode (skip long tests)
go test -short
```

**Key features:**
- Table-driven tests (Go idiom)
- Subtests with t.Run
- Benchmark tests
- Example tests (for documentation)
- Parallel test execution
- Test helpers

---

## Test Best Practices

### General Guidelines

1. **Follow AAA Pattern**
   - **Arrange**: Set up test data
   - **Act**: Execute the code
   - **Assert**: Verify the outcome

2. **Test Naming**
   - Descriptive names: `test_user_login_with_invalid_password`
   - Pattern: `test_<what>_<condition>_<expected>`

3. **One Assertion Per Test** (when possible)
   - Makes failures easier to diagnose
   - Each test should verify one behavior

4. **Test Categories**
   - **Unit**: Fast, isolated, no dependencies
   - **Integration**: Test component interactions
   - **E2E**: Full user workflows

5. **Coverage Goals**
   - Aim for 80%+ code coverage
   - 100% coverage for critical paths
   - Don't sacrifice quality for coverage numbers

### What to Test

✅ **Do test:**
- Public APIs and interfaces
- Edge cases and boundaries
- Error handling
- Security-critical code
- Complex business logic

❌ **Don't test:**
- Third-party library internals
- Simple getters/setters
- Framework code
- Trivial code

### Test Organization

```
project/
├── src/              # Source code
│   ├── module1/
│   └── module2/
└── tests/            # Test files
    ├── unit/         # Unit tests
    ├── integration/  # Integration tests
    └── e2e/          # End-to-end tests
```

### Mocking Guidelines

**When to mock:**
- External APIs
- Databases
- File system
- Network calls
- Time/random values

**When NOT to mock:**
- Code you own
- Simple functions
- Value objects
- Over-mocking makes tests brittle

---

## Running Tests with Claude Code

### Using Slash Commands

```bash
# Run full test suite
/quality:test

# Run tests with coverage
/quality:test --coverage

# Run specific test file
/quality:test tests/test_user.py

# Watch mode
/quality:test --watch
```

### Hooks Integration

The post-tool-use hook can automatically run affected tests after code changes:

Edit `.claude/hooks/post-tool-use.py` to enable.

---

## CI/CD Integration

### GitHub Actions

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: |
          # Python
          pip install pytest pytest-cov
          pytest --cov

          # JavaScript
          npm install
          npm test

          # Rust
          cargo test

          # Go
          go test ./...
```

---

## Troubleshooting

### Tests Not Found

**Python:**
- Ensure files start with `test_` or end with `_test.py`
- Check `testpaths` in pytest.ini

**JavaScript:**
- Check `testMatch` pattern in jest.config.js
- Ensure files end with `.test.js` or `.spec.js`

**Rust:**
- Tests must be in `#[cfg(test)]` module or `tests/` directory
- Run `cargo test --help` for options

**Go:**
- Files must end with `_test.go`
- Functions must start with `Test`
- Import `testing` package

### Coverage Too Low

1. Identify uncovered code:
   ```bash
   pytest --cov --cov-report=html  # Python
   npm test -- --coverage          # JavaScript
   cargo tarpaulin                 # Rust (install first)
   go test -coverprofile=cover.out # Go
   ```

2. Add tests for uncovered branches

3. Focus on critical paths first

### Tests Running Slow

**Solutions:**
- Use test markers to skip slow tests during development
- Run tests in parallel
- Mock external dependencies
- Use in-memory databases for testing

---

## Additional Resources

- [pytest documentation](https://docs.pytest.org/)
- [Jest documentation](https://jestjs.io/)
- [Rust testing guide](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Go testing package](https://pkg.go.dev/testing)

---

**Version:** 1.0.0
**Last Updated:** 2025-11-11
