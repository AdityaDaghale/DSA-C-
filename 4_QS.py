"""Sum of digits module.

This module provides functionality to calculate the sum of digits in a number.
"""

def sum_of_digits(num):
    """Calculate the sum of all digits in a number.
    
    Args:
        num (int): The number to process (must be non-negative)
    
    Returns:
        int: The sum of all digits in the number
    
    Raises:
        ValueError: If num is negative
    
    Example:
        >>> sum_of_digits(14505)
        15
        >>> sum_of_digits(999)
        27
    """
    if num < 0:
        raise ValueError("Number must be non-negative")
    
    dig_sum = 0
    
    while num > 0:
        last_digit = num % 10
        num = num // 10
        dig_sum += last_digit
    
    return dig_sum


def sum_of_digits_alternative(num):
    """Alternative approach using string conversion.
    
    Args:
        num (int): The number to process (must be non-negative)
    
    Returns:
        int: The sum of all digits in the number
    
    Raises:
        ValueError: If num is negative
    """
    if num < 0:
        raise ValueError("Number must be non-negative")
    
    return sum(int(digit) for digit in str(num))


def main():
    """Main function to demonstrate sum of digits calculation."""
    try:
        print("\n" + "=" * 50)
        print("Sum of Digits Calculation")
        print("=" * 50)
        
        test_numbers = [14505, 999, 123, 100, 0]
        
        print("\n--- Using While Loop Method ---")
        for num in test_numbers:
            result = sum_of_digits(num)
            print(f"Sum of digits in {num}: {result}")
        
        print("\n--- Using String Conversion Method ---")
        for num in test_numbers:
            result = sum_of_digits_alternative(num)
            print(f"Sum of digits in {num}: {result}")
        
        print("\n" + "=" * 50 + "\n")
        
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
