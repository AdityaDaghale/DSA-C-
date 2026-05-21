"""Functions module - Basic arithmetic operations.

This module demonstrates basic function definitions and operations.
"""

def sum_numbers(a, b):
    """Calculate the sum of two numbers.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: Sum of a and b
    
    Example:
        >>> sum_numbers(10, 5)
        15
    """
    s = a + b
    return s


def min_of_two(a, b):
    """Find the minimum of two numbers.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: The minimum of a and b
    
    Example:
        >>> min_of_two(15, 5)
        5
    """
    if a < b:
        return a
    else:
        return b


def main():
    """Main function to demonstrate basic operations."""
    try:
        print("=" * 40)
        print("Basic Arithmetic Operations")
        print("=" * 40)
        
        # Sum of two numbers
        result_sum = sum_numbers(10, 5)
        print(f"Sum of 10 and 5: {result_sum}")
        
        # Min of two numbers
        result_min = min_of_two(15, 5)
        print(f"Minimum of 15 and 5: {result_min}")
        
        print("=" * 40)
        
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
