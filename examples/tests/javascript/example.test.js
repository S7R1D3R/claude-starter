/**
 * Example test file demonstrating Jest best practices.
 *
 * Tests follow the AAA pattern:
 * - Arrange: Set up test data and preconditions
 * - Act: Execute the code being tested
 * - Assert: Verify the expected outcome
 */

// Simple unit test
describe('Basic Math Operations', () => {
  test('addition works correctly', () => {
    // Arrange
    const a = 2;
    const b = 3;
    const expected = 5;

    // Act
    const result = a + b;

    // Assert
    expect(result).toBe(expected);
  });

  test('multiplication works correctly', () => {
    expect(5 * 3).toBe(15);
  });
});

// Test suite grouping
describe('String Operations', () => {
  test('converts to uppercase', () => {
    const text = 'claude code';
    expect(text.toUpperCase()).toBe('CLAUDE CODE');
  });

  test('converts to lowercase', () => {
    const text = 'CLAUDE CODE';
    expect(text.toLowerCase()).toBe('claude code');
  });

  test('checks string contains substring', () => {
    const text = 'Claude Code Starter';
    expect(text).toContain('Code');
    expect(text).toMatch(/Starter$/);
  });
});

// Parametrized tests (test.each)
describe('Parametrized Tests', () => {
  test.each([
    [1, 2],
    [2, 4],
    [3, 6],
    [10, 20],
    [-5, -10],
  ])('doubles %i to get %i', (input, expected) => {
    expect(input * 2).toBe(expected);
  });
});

// Testing with setup and teardown
describe('Setup and Teardown', () => {
  let data;

  beforeEach(() => {
    // Runs before each test
    data = [];
  });

  afterEach(() => {
    // Runs after each test
    data = null;
  });

  beforeAll(() => {
    // Runs once before all tests in this suite
    console.log('Starting test suite');
  });

  afterAll(() => {
    // Runs once after all tests in this suite
    console.log('Finished test suite');
  });

  test('can push to array', () => {
    data.push(1);
    expect(data).toHaveLength(1);
    expect(data[0]).toBe(1);
  });

  test('starts with empty array', () => {
    expect(data).toHaveLength(0);
    expect(data).toEqual([]);
  });
});

// Testing objects and arrays
describe('Object and Array Matching', () => {
  test('object equality', () => {
    const user = {
      name: 'Test User',
      email: 'test@example.com',
      age: 25
    };

    expect(user).toEqual({
      name: 'Test User',
      email: 'test@example.com',
      age: 25
    });
  });

  test('object contains properties', () => {
    const user = { name: 'Alice', age: 30, role: 'admin' };

    expect(user).toHaveProperty('name');
    expect(user).toHaveProperty('age', 30);
    expect(user).toMatchObject({ name: 'Alice' });
  });

  test('array operations', () => {
    const numbers = [1, 2, 3, 4, 5];

    expect(numbers).toHaveLength(5);
    expect(numbers).toContain(3);
    expect(numbers).toEqual(expect.arrayContaining([2, 4]));
  });
});

// Testing exceptions
describe('Exception Handling', () => {
  test('throws error on division by zero', () => {
    const divideByZero = () => {
      throw new Error('Division by zero');
    };

    expect(divideByZero).toThrow();
    expect(divideByZero).toThrow(Error);
    expect(divideByZero).toThrow('Division by zero');
  });

  test('does not throw with valid input', () => {
    const safeDivide = () => 10 / 2;
    expect(safeDivide).not.toThrow();
  });
});

// Testing async code
describe('Async Operations', () => {
  test('promise resolves correctly', async () => {
    const fetchData = () => Promise.resolve('data');
    const data = await fetchData();
    expect(data).toBe('data');
  });

  test('promise rejects correctly', async () => {
    const fetchError = () => Promise.reject(new Error('Failed'));
    await expect(fetchError()).rejects.toThrow('Failed');
  });

  test('async function with timeout', async () => {
    const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));
    const start = Date.now();
    await delay(100);
    const elapsed = Date.now() - start;
    expect(elapsed).toBeGreaterThanOrEqual(100);
  });
});

// Mocking functions
describe('Mocking', () => {
  test('mock function calls', () => {
    const mockFn = jest.fn();
    mockFn('arg1', 'arg2');

    expect(mockFn).toHaveBeenCalled();
    expect(mockFn).toHaveBeenCalledTimes(1);
    expect(mockFn).toHaveBeenCalledWith('arg1', 'arg2');
  });

  test('mock function return values', () => {
    const mockFn = jest.fn()
      .mockReturnValueOnce(10)
      .mockReturnValueOnce(20)
      .mockReturnValue(30);

    expect(mockFn()).toBe(10);
    expect(mockFn()).toBe(20);
    expect(mockFn()).toBe(30);
    expect(mockFn()).toBe(30);
  });

  test('mock implementation', () => {
    const mockFn = jest.fn((x, y) => x + y);

    expect(mockFn(2, 3)).toBe(5);
    expect(mockFn).toHaveBeenCalledWith(2, 3);
  });
});

// Snapshot testing
describe('Snapshot Testing', () => {
  test('matches snapshot', () => {
    const data = {
      name: 'Claude Code',
      version: '1.0.0',
      features: ['hooks', 'commands', 'skills']
    };

    expect(data).toMatchSnapshot();
  });
});

// Testing with specific matchers
describe('Advanced Matchers', () => {
  test('number comparisons', () => {
    const value = 100;

    expect(value).toBeGreaterThan(50);
    expect(value).toBeLessThan(200);
    expect(value).toBeGreaterThanOrEqual(100);
    expect(value).toBeLessThanOrEqual(100);
  });

  test('floating point equality', () => {
    const value = 0.1 + 0.2;
    // Don't use toBe for floats
    expect(value).toBeCloseTo(0.3);
  });

  test('truthy and falsy', () => {
    expect(true).toBeTruthy();
    expect(1).toBeTruthy();
    expect('text').toBeTruthy();

    expect(false).toBeFalsy();
    expect(0).toBeFalsy();
    expect('').toBeFalsy();
    expect(null).toBeFalsy();
    expect(undefined).toBeFalsy();
  });

  test('null and undefined', () => {
    const n = null;
    expect(n).toBeNull();
    expect(n).toBeDefined();
    expect(n).not.toBeUndefined();

    let u;
    expect(u).toBeUndefined();
    expect(u).not.toBeNull();
    expect(u).not.toBeDefined();
  });
});

// Test skipping and focusing
describe('Test Control', () => {
  test('this test runs', () => {
    expect(true).toBe(true);
  });

  test.skip('this test is skipped', () => {
    expect(false).toBe(true); // Won't fail
  });

  // Use test.only to run only this test (useful for debugging)
  // test.only('only this test runs', () => {
  //   expect(true).toBe(true);
  // });
});

// User validation example
describe('UserService', () => {
  class UserService {
    validateEmail(email) {
      return email && email.includes('@') && email.includes('.');
    }

    normalizeEmail(email) {
      return email.trim().toLowerCase();
    }

    isAdult(age) {
      return age >= 18;
    }
  }

  let userService;

  beforeEach(() => {
    userService = new UserService();
  });

  describe('validateEmail', () => {
    test('accepts valid email', () => {
      expect(userService.validateEmail('user@example.com')).toBe(true);
    });

    test('rejects email without @', () => {
      expect(userService.validateEmail('userexample.com')).toBe(false);
    });

    test('rejects email without domain', () => {
      expect(userService.validateEmail('user@')).toBe(false);
    });

    test('rejects empty email', () => {
      expect(userService.validateEmail('')).toBe(false);
    });
  });

  describe('normalizeEmail', () => {
    test('trims whitespace', () => {
      expect(userService.normalizeEmail('  user@example.com  '))
        .toBe('user@example.com');
    });

    test('converts to lowercase', () => {
      expect(userService.normalizeEmail('USER@EXAMPLE.COM'))
        .toBe('user@example.com');
    });
  });

  describe('isAdult', () => {
    test.each([
      [18, true],
      [25, true],
      [100, true],
      [17, false],
      [0, false],
      [-1, false],
    ])('age %i returns %s', (age, expected) => {
      expect(userService.isAdult(age)).toBe(expected);
    });
  });
});
