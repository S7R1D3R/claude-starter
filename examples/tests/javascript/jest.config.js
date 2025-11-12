/**
 * Jest configuration for Claude Code Starter
 * @see https://jestjs.io/docs/configuration
 */

module.exports = {
  // Test environment
  testEnvironment: 'node', // or 'jsdom' for browser-like environment

  // Test file patterns
  testMatch: [
    '**/__tests__/**/*.[jt]s?(x)',
    '**/?(*.)+(spec|test).[jt]s?(x)'
  ],

  // Files to ignore
  testPathIgnorePatterns: [
    '/node_modules/',
    '/build/',
    '/dist/',
    '/coverage/'
  ],

  // Coverage configuration
  collectCoverage: true,
  coverageDirectory: 'coverage',
  coverageReporters: ['text', 'lcov', 'html'],

  // Coverage thresholds (fail if below)
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  },

  // Files to collect coverage from
  collectCoverageFrom: [
    'src/**/*.{js,jsx,ts,tsx}',
    '!src/**/*.d.ts',
    '!src/**/*.stories.{js,jsx,ts,tsx}',
    '!src/**/__tests__/**',
    '!src/**/index.{js,ts}'
  ],

  // Module paths
  moduleDirectories: ['node_modules', 'src'],

  // Module file extensions
  moduleFileExtensions: ['js', 'jsx', 'ts', 'tsx', 'json', 'node'],

  // Transform files
  transform: {
    '^.+\\.(js|jsx|ts|tsx)$': 'babel-jest',
  },

  // Setup files
  // setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],

  // Clear mocks between tests
  clearMocks: true,

  // Reset mocks between tests
  resetMocks: true,

  // Restore mocks between tests
  restoreMocks: true,

  // Verbose output
  verbose: true,

  // Max workers (parallel test execution)
  maxWorkers: '50%',

  // Timeout for tests
  testTimeout: 10000,

  // Show individual test results
  notify: false,

  // Globals available in tests
  globals: {
    'ts-jest': {
      tsconfig: {
        jsx: 'react',
        esModuleInterop: true
      }
    }
  }
};
