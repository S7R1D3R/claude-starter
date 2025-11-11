# Rust Project Template

Basic Rust project with cargo configuration.

## Features

- **Cargo** - Build system and package manager
- **rustfmt** - Code formatting
- **clippy** - Linting
- **cargo test** - Testing framework
- **cargo doc** - Documentation generation

## Usage

```bash
# Build project
cargo build

# Build for release
cargo build --release

# Run project
cargo run

# Run tests
cargo test

# Run tests with output
cargo test -- --nocapture

# Format code
cargo fmt

# Lint
cargo clippy

# Generate documentation
cargo doc --open

# Check without building
cargo check
```

## Project Structure

```
project/
├── src/
│   ├── lib.rs or main.rs
│   └── modules/
├── tests/
│   └── integration_test.rs
├── Cargo.toml
└── README.md
```
