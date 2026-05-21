"""Combinations (nCr) module.

This module calculates combinations using the formula: nCr = n! / (r! * (n-r)!)
"""

def factorial(n):
    """Calculate factorial of n.
    
    Args:
        n (int): The number to calculate factorial for
    
    Returns:
        int: Factorial of n (n!)
    
    Raises:
        ValueError: If n is negative
    
    Example:
        >>> factorial(5)
        120
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


def n_cr(n, r):
    """Calculate nCr (combinations of n things taken r at a time).
    
    Formula: nCr = n! / (r! * (n-r)!)
    
    Args:
        n (int): Total number of items
        r (int): Number of items to choose
    
    Returns:
        int: Number of combinations
    
    Raises:
        ValueError: If n or r are invalid
    
    Example:
        >>> n_cr(8, 2)
        28
    """
    if r < 0 or n < 0:
        raise ValueError("n and r must be non-negative integers")
    
    if r > n:
        raise ValueError("r cannot be greater than n")
    
    fact_n = factorial(n)
    fact_r = factorial(r)
    fact_nmr = factorial(n - r)
    
    return fact_n // (fact_r * fact_nmr)


def n_pr(n, r):
    """Calculate nPr (permutations of n things taken r at a time).
    
    Formula: nPr = n! / (n-r)!
    
    Args:
        n (int): Total number of items
        r (int): Number of items to arrange
    
    Returns:
        int: Number of permutations
    
    Raises:
        ValueError: If n or r are invalid
    
    Example:
        >>> n_pr(8, 2)
        56
    """
    if r < 0 or n < 0:
        raise ValueError("n and r must be non-negative integers")
    
    if r > n:
        raise ValueError("r cannot be greater than n")
    
    fact_n = factorial(n)
    fact_nmr = factorial(n - r)
    
    return fact_n // fact_nmr


def main():
    """Main function to demonstrate combinations and permutations."""
    try:
        print("\n" + "=" * 50)
        print("Combinations (nCr) and Permutations (nPr)")
        print("=" * 50)
        
        n = 8
        r = 2
        
        # Calculate nCr
        print(f"\n--- Combinations ---")
        print(f"n = {n}, r = {r}")
        result_cr = n_cr(n, r)
        print(f"nCr (C({n}, {r})): {result_cr}")
        
        # More examples
        test_cases = [(5, 2), (10, 3), (7, 3)]
        for n_val, r_val in test_cases:
            result = n_cr(n_val, r_val)
            print(f"C({n_val}, {r_val}): {result}")
        
        # Calculate nPr
        print(f"\n--- Permutations ---")
        n = 8
        r = 2
        print(f"n = {n}, r = {r}")
        result_pr = n_pr(n, r)
        print(f"nPr (P({n}, {r})): {result_pr}")
        
        # More examples
        for n_val, r_val in test_cases:
            result = n_pr(n_val, r_val)
            print(f"P({n_val}, {r_val}): {result}")
        
        print("\n" + "=" * 50 + "\n")
        
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
