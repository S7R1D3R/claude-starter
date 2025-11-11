---
description: Start the development server for the project
---

# Start Development Server

Start the appropriate development server based on project type.

## Auto-Detection

Check for these markers and use the corresponding command:

### Node.js/JavaScript
- **package.json** with `"dev"` or `"start"` script → `npm run dev` or `npm start`
- **Vite** → `npm run dev`
- **Next.js** → `npm run dev`
- **React** (CRA) → `npm start`

### Python
- **manage.py** (Django) → `python manage.py runserver`
- **app.py** (Flask) → `flask run` or `python app.py`
- **main.py** (FastAPI) → `uvicorn main:app --reload`

### Ruby
- **Gemfile** with Rails → `rails server`
- **config.ru** (Rack) → `rackup`

### Go
- **main.go** → `go run main.go` or `go run .`

### Rust
- **Cargo.toml** → `cargo run`

### Java
- **Spring Boot** → `./mvnw spring-boot:run` or `./gradlew bootRun`

## Execution

1. **Detect** the framework/runtime
2. **Run** the server command **in the background** using `run_in_background: true`
3. **Report** the server URL (usually http://localhost:3000, :8000, :5000, etc.)
4. **Inform** the user how to stop the server (Ctrl+C or kill process)

## Port Configuration

- Check for environment variables (PORT, HOST)
- Check for configuration files
- Use framework defaults if not specified

**Arguments**: Accepts `$ARGUMENTS` to pass additional flags (e.g., custom port: `/dev:serve --port 3001`)
