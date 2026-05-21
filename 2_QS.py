"""Mathematical operations module - Sum and Factorial.

This module provides functions to calculate sum of n numbers and factorial.
"""

def sum_n(n):
    """Calculate the sum of first n natural numbers.
    
    Args:
        n (int): The upper limit for summation
    
    Returns:
        int: Sum of numbers from 1 to n
    
    Raises:
        ValueError: If n is negative
    
    Example:
        >>> sum_n(5)
        15
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def fact_n(n):
    """Calculate factorial of n.
    
    Args:
        n (int): The number to calculate factorial for
    
    Returns:
        int: Factorial of n (n!)
    
    Raises:
        ValueError: If n is negative
    
    Example:
        >>> fact_n(5)
        120
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


def main():
    """Main function to demonstrate mathematical operations."""
    try:
        print("\n" + "=" * 50)
        print("Mathematical Operations: Sum and Factorial")
        print("=" * 50)
        
        # Sum of n numbers
        print("\n--- Sum of N Numbers ---")
        sum_15 = sum_n(15)
        print(f"Sum of first 15 numbers: {sum_15}")
        
        sum_88 = sum_n(88)
        print(f"Sum of first 88 numbers: {sum_88}")
        
        # Factorial of n numbers
        print("\n--- Factorial of N ---")
        fact_3 = fact_n(3)
        print(f"Factorial of 3: {fact_3}")
        
        fact_10 = fact_n(10)
        print(f"Factorial of 10: {fact_10}")
        
        print("\n" + "=" * 50)
        
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
