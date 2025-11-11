---
description: Install project dependencies based on auto-detected package manager
---

# Setup Project Dependencies

Install all project dependencies using the appropriate package manager.

## Auto-Detection Priority

Check for these files in order and use the corresponding command:

1. **package.json** → `npm install` or `yarn install`
2. **requirements.txt** → `pip install -r requirements.txt`
3. **Pipfile** → `pipenv install`
4. **pyproject.toml** → `poetry install` or `pip install -e .`
5. **Cargo.toml** → `cargo build`
6. **go.mod** → `go mod download`
7. **pom.xml** → `mvn install`
8. **build.gradle** → `gradle build`
9. **Gemfile** → `bundle install`
10. **composer.json** → `composer install`

## Execution Steps

1. **Detect** the package manager by checking for marker files
2. **Verify** the tool is installed (e.g., `which npm`)
3. **Run** the appropriate installation command
4. **Report** success or any errors
5. **Suggest** next steps (run tests, start server)

## Additional Setup

Also check for and run:
- Git submodule initialization: `git submodule update --init --recursive`
- Pre-commit hooks: If `.pre-commit-config.yaml` exists, run `pre-commit install`
- Database setup: Check for migration files

## Error Handling

If the package manager is not installed:
- Provide installation instructions for the user's OS
- Suggest alternative approaches

**Arguments**: Optionally accepts `$ARGUMENTS` to specify a different package manager.
