// Example test file for Rust
// Tests are typically placed in a `tests` module within the same file
// or in separate files in a `tests/` directory

// Simple function to test
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

pub fn multiply(a: i32, b: i32) -> i32 {
    a * b
}

pub fn divide(a: i32, b: i32) -> Result<i32, String> {
    if b == 0 {
        Err(String::from("Division by zero"))
    } else {
        Ok(a / b)
    }
}

#[derive(Debug, PartialEq)]
pub struct User {
    pub name: String,
    pub email: String,
    pub age: u32,
}

impl User {
    pub fn new(name: String, email: String, age: u32) -> Self {
        User { name, email, age }
    }

    pub fn is_adult(&self) -> bool {
        self.age >= 18
    }

    pub fn validate_email(&self) -> bool {
        self.email.contains('@') && self.email.contains('.')
    }
}

// Unit tests module
#[cfg(test)]
mod tests {
    use super::*;

    // Basic test
    #[test]
    fn test_add() {
        assert_eq!(add(2, 3), 5);
        assert_eq!(add(-1, 1), 0);
        assert_eq!(add(0, 0), 0);
    }

    #[test]
    fn test_multiply() {
        assert_eq!(multiply(2, 3), 6);
        assert_eq!(multiply(-2, 3), -6);
        assert_eq!(multiply(0, 100), 0);
    }

    // Test with Result
    #[test]
    fn test_divide_success() {
        assert_eq!(divide(10, 2), Ok(5));
        assert_eq!(divide(9, 3), Ok(3));
    }

    #[test]
    fn test_divide_by_zero() {
        assert!(divide(10, 0).is_err());
        assert_eq!(
            divide(10, 0),
            Err(String::from("Division by zero"))
        );
    }

    // Test with should_panic
    #[test]
    #[should_panic(expected = "index out of bounds")]
    fn test_panic() {
        let v = vec![1, 2, 3];
        let _ = v[10]; // This will panic
    }

    // Test struct
    #[test]
    fn test_user_creation() {
        let user = User::new(
            String::from("Alice"),
            String::from("alice@example.com"),
            25,
        );

        assert_eq!(user.name, "Alice");
        assert_eq!(user.email, "alice@example.com");
        assert_eq!(user.age, 25);
    }

    #[test]
    fn test_user_is_adult() {
        let adult = User::new(
            String::from("Bob"),
            String::from("bob@example.com"),
            18,
        );
        assert!(adult.is_adult());

        let minor = User::new(
            String::from("Charlie"),
            String::from("charlie@example.com"),
            17,
        );
        assert!(!minor.is_adult());
    }

    #[test]
    fn test_user_validate_email() {
        let valid_user = User::new(
            String::from("Alice"),
            String::from("alice@example.com"),
            25,
        );
        assert!(valid_user.validate_email());

        let invalid_user = User::new(
            String::from("Bob"),
            String::from("invalid-email"),
            30,
        );
        assert!(!invalid_user.validate_email());
    }

    // Test with custom assertion message
    #[test]
    fn test_with_message() {
        let result = add(2, 3);
        assert_eq!(result, 5, "Expected 2 + 3 to equal 5, got {}", result);
    }

    // Test with assert! macros
    #[test]
    fn test_boolean_assertions() {
        assert!(true);
        assert!(1 > 0);
        assert!(!false);
    }

    // Ignored test (skipped unless explicitly run with --ignored)
    #[test]
    #[ignore]
    fn expensive_test() {
        // This test is expensive and only runs when explicitly requested
        assert_eq!(1, 1);
    }
}

// Integration tests would go in tests/ directory
// Example: tests/integration_test.rs
