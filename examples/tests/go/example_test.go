// Example test file for Go
// Test files must end with _test.go
// Test functions must start with Test and take *testing.T

package example

import (
	"errors"
	"strings"
	"testing"
)

// Simple functions to test
func Add(a, b int) int {
	return a + b
}

func Multiply(a, b int) int {
	return a * b
}

func Divide(a, b int) (int, error) {
	if b == 0 {
		return 0, errors.New("division by zero")
	}
	return a / b, nil
}

// User struct for testing
type User struct {
	Name  string
	Email string
	Age   int
}

func NewUser(name, email string, age int) *User {
	return &User{
		Name:  name,
		Email: email,
		Age:   age,
	}
}

func (u *User) IsAdult() bool {
	return u.Age >= 18
}

func (u *User) ValidateEmail() bool {
	return strings.Contains(u.Email, "@") && strings.Contains(u.Email, ".")
}

// ===== TESTS =====

// Basic test
func TestAdd(t *testing.T) {
	result := Add(2, 3)
	expected := 5

	if result != expected {
		t.Errorf("Add(2, 3) = %d; want %d", result, expected)
	}
}

func TestMultiply(t *testing.T) {
	result := Multiply(2, 3)
	expected := 6

	if result != expected {
		t.Errorf("Multiply(2, 3) = %d; want %d", result, expected)
	}
}

// Test with subtests
func TestDivide(t *testing.T) {
	t.Run("success", func(t *testing.T) {
		result, err := Divide(10, 2)
		if err != nil {
			t.Errorf("Unexpected error: %v", err)
		}
		if result != 5 {
			t.Errorf("Divide(10, 2) = %d; want 5", result)
		}
	})

	t.Run("division by zero", func(t *testing.T) {
		_, err := Divide(10, 0)
		if err == nil {
			t.Error("Expected error for division by zero, got nil")
		}
	})
}

// Table-driven tests (Go idiom)
func TestAddTableDriven(t *testing.T) {
	tests := []struct {
		name     string
		a        int
		b        int
		expected int
	}{
		{"positive numbers", 2, 3, 5},
		{"negative numbers", -2, -3, -5},
		{"mixed signs", -2, 3, 1},
		{"zero", 0, 0, 0},
		{"large numbers", 1000, 2000, 3000},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := Add(tt.a, tt.b)
			if result != tt.expected {
				t.Errorf("Add(%d, %d) = %d; want %d",
					tt.a, tt.b, result, tt.expected)
			}
		})
	}
}

// Test User struct
func TestUserCreation(t *testing.T) {
	user := NewUser("Alice", "alice@example.com", 25)

	if user.Name != "Alice" {
		t.Errorf("user.Name = %s; want Alice", user.Name)
	}
	if user.Email != "alice@example.com" {
		t.Errorf("user.Email = %s; want alice@example.com", user.Email)
	}
	if user.Age != 25 {
		t.Errorf("user.Age = %d; want 25", user.Age)
	}
}

func TestUserIsAdult(t *testing.T) {
	tests := []struct {
		name     string
		age      int
		expected bool
	}{
		{"adult", 18, true},
		{"over 18", 25, true},
		{"minor", 17, false},
		{"child", 5, false},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			user := NewUser("Test", "test@example.com", tt.age)
			result := user.IsAdult()
			if result != tt.expected {
				t.Errorf("IsAdult() with age %d = %v; want %v",
					tt.age, result, tt.expected)
			}
		})
	}
}

func TestUserValidateEmail(t *testing.T) {
	tests := []struct {
		name     string
		email    string
		expected bool
	}{
		{"valid email", "user@example.com", true},
		{"no at symbol", "userexample.com", false},
		{"no domain", "user@", false},
		{"no local part", "@example.com", false},
		{"empty", "", false},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			user := NewUser("Test", tt.email, 25)
			result := user.ValidateEmail()
			if result != tt.expected {
				t.Errorf("ValidateEmail(%s) = %v; want %v",
					tt.email, result, tt.expected)
			}
		})
	}
}

// Helper function example
func assertEqual(t *testing.T, got, want interface{}) {
	t.Helper() // Marks this as a helper function
	if got != want {
		t.Errorf("got %v; want %v", got, want)
	}
}

func TestWithHelper(t *testing.T) {
	result := Add(2, 3)
	assertEqual(t, result, 5)
}

// Benchmark example
func BenchmarkAdd(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Add(2, 3)
	}
}

func BenchmarkMultiply(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Multiply(2, 3)
	}
}

// Example test (appears in documentation)
func ExampleAdd() {
	result := Add(2, 3)
	println(result)
	// Output: 5
}

// Parallel test example
func TestParallel(t *testing.T) {
	t.Run("group", func(t *testing.T) {
		t.Run("test1", func(t *testing.T) {
			t.Parallel()
			// Test runs in parallel with test2
			result := Add(1, 1)
			assertEqual(t, result, 2)
		})

		t.Run("test2", func(t *testing.T) {
			t.Parallel()
			// Test runs in parallel with test1
			result := Add(2, 2)
			assertEqual(t, result, 4)
		})
	})
}

// Test with cleanup
func TestWithCleanup(t *testing.T) {
	// Setup
	data := make([]int, 0)

	// Cleanup will run after test completes
	t.Cleanup(func() {
		data = nil
	})

	// Test
	data = append(data, 1, 2, 3)
	if len(data) != 3 {
		t.Errorf("len(data) = %d; want 3", len(data))
	}
}

// Skip test conditionally
func TestSkipped(t *testing.T) {
	if testing.Short() {
		t.Skip("Skipping test in short mode")
	}
	// Long-running test code here
}
