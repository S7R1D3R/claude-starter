"""
Example test file demonstrating pytest best practices.

Tests should follow the AAA pattern:
- Arrange: Set up test data and preconditions
- Act: Execute the code being tested
- Assert: Verify the expected outcome
"""

import pytest


# Simple unit test example
def test_addition():
    """Test that addition works correctly."""
    # Arrange
    a = 2
    b = 3
    expected = 5

    # Act
    result = a + b

    # Assert
    assert result == expected


# Test with multiple assertions
def test_string_operations():
    """Test various string operations."""
    text = "Claude Code"

    assert text.upper() == "CLAUDE CODE"
    assert text.lower() == "claude code"
    assert len(text) == 11
    assert "Code" in text


# Parametrized test (DRY principle)
@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
    (10, 20),
    (-5, -10),
])
def test_double(input, expected):
    """Test doubling numbers with multiple inputs."""
    assert input * 2 == expected


# Test with fixture
@pytest.fixture
def sample_data():
    """Fixture providing sample data for tests."""
    return {
        "name": "Test User",
        "email": "test@example.com",
        "age": 25
    }


def test_with_fixture(sample_data):
    """Test using a fixture for setup."""
    assert sample_data["name"] == "Test User"
    assert "@" in sample_data["email"]
    assert sample_data["age"] > 0


# Test exception handling
def test_division_by_zero():
    """Test that division by zero raises expected error."""
    with pytest.raises(ZeroDivisionError):
        result = 10 / 0


# Test with marker (for categorization)
@pytest.mark.unit
def test_fast_operation():
    """Fast unit test (isolated, no dependencies)."""
    result = [x * 2 for x in range(10)]
    assert len(result) == 10
    assert result[0] == 0
    assert result[9] == 18


@pytest.mark.integration
def test_with_external_dependency():
    """Integration test (might involve I/O, database, etc)."""
    # This would normally test actual integration
    # Here we just demonstrate the marker
    pass


@pytest.mark.slow
def test_slow_operation():
    """Test marked as slow (useful for selective test running)."""
    # Simulate slow operation
    import time
    time.sleep(0.1)
    assert True


# Test class grouping related tests
class TestUserValidation:
    """Group of tests for user validation logic."""

    def test_valid_email(self):
        """Test email validation with valid email."""
        email = "user@example.com"
        assert "@" in email
        assert "." in email

    def test_invalid_email(self):
        """Test email validation with invalid email."""
        email = "invalid-email"
        assert "@" not in email

    def test_email_normalization(self):
        """Test that emails are normalized correctly."""
        email = "  USER@EXAMPLE.COM  "
        normalized = email.strip().lower()
        assert normalized == "user@example.com"


# Test with setup and teardown
class TestWithSetup:
    """Example of test class with setup/teardown."""

    def setup_method(self):
        """Run before each test method."""
        self.data = []

    def teardown_method(self):
        """Run after each test method."""
        self.data = None

    def test_append(self):
        """Test list append operation."""
        self.data.append(1)
        assert len(self.data) == 1
        assert self.data[0] == 1

    def test_extend(self):
        """Test list extend operation."""
        self.data.extend([1, 2, 3])
        assert len(self.data) == 3


# Test with mocking (using pytest-mock)
def test_with_mock(mocker):
    """Example of mocking external dependencies."""
    # Mock a function
    mock_func = mocker.Mock(return_value=42)

    # Call the mock
    result = mock_func()

    # Verify
    assert result == 42
    mock_func.assert_called_once()


# Test with temporary files (using tmp_path fixture)
def test_file_operations(tmp_path):
    """Test file operations using temporary directory."""
    # Create a temporary file
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello, Claude!")

    # Read and verify
    content = test_file.read_text()
    assert content == "Hello, Claude!"
    assert test_file.exists()


# Test with skip condition
@pytest.mark.skipif(
    not hasattr(__builtins__, 'breakpoint'),
    reason="Requires Python 3.7+ for breakpoint()"
)
def test_modern_feature():
    """Test that only runs on Python 3.7+."""
    assert hasattr(__builtins__, 'breakpoint')


# Test with custom fail message
def test_with_custom_message():
    """Test with descriptive failure message."""
    value = 10
    assert value > 5, f"Expected value > 5, but got {value}"
    assert value < 20, f"Expected value < 20, but got {value}"
