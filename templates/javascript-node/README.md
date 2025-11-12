# Node.js Project Template

Modern Node.js/Express project with TypeScript support.

## Features

- **Express.js** - Web framework
- **TypeScript** - Type safety
- **Jest** - Testing framework
- **ESLint** - Linting
- **Prettier** - Code formatting
- **nodemon** - Auto-restart during development

## Usage

```bash
# Install dependencies
npm install

# Development mode (with auto-restart)
npm run dev

# Build for production
npm run build

# Start production server
npm start

# Run tests
npm test

# Run tests in watch mode
npm run test:watch

# Lint
npm run lint

# Format
npm run format
```

## Project Structure

```
project/
├── src/
│   ├── index.ts       # Entry point
│   ├── routes/        # API routes
│   ├── controllers/   # Business logic
│   ├── models/        # Data models
│   └── middleware/    # Express middleware
├── tests/
│   └── index.test.ts
├── package.json
├── tsconfig.json
├── .eslintrc.json
└── .prettierrc
```
