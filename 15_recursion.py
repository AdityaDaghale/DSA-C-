"""Recursion Examples - Fibonacci, Power, GCD"""

def fibonacci(n):
    """Fibonacci sequence - O(2^n)"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_optimized(n, memo={}):
    """Fibonacci with memoization - O(n)"""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_optimized(n - 1, memo) + fibonacci_optimized(n - 2, memo)
    return memo[n]

def power(base, exp):
    """Calculate base^exp recursively"""
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

def gcd(a, b):
    """Greatest Common Divisor using Euclidean algorithm"""
    if b == 0:
        return a
    return gcd(b, a % b)

if __name__ == "__main__":
    print("Fibonacci(10):", fibonacci_optimized(10))
    print("2^5:", power(2, 5))
    print("GCD(48, 18):", gcd(48, 18))
