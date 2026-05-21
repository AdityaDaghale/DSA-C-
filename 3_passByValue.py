"""Pass by value demonstration module.

This module demonstrates the difference between pass by value in C++ 
and how Python handles object references.
"""

def change_x(x):
    """Modify a number (demonstrates pass by value behavior).
    
    In Python, immutable objects like integers are passed by value.
    Changes made to x inside this function don't affect the original.
    
    Args:
        x (int): The number to modify
    
    Returns:
        int: The modified value (2 * x)
    """
    x = 2 * x
    print(f"Inside function - x = {x}")
    return x


def change_list(lst):
    """Modify a list (demonstrates pass by reference behavior).
    
    In Python, mutable objects like lists are passed by reference.
    Changes made to the list persist after the function call.
    
    Args:
        lst (list): The list to modify
    """
    lst.append(100)
    print(f"Inside function - list = {lst}")


def main():
    """Main function to demonstrate pass by value and reference."""
    try:
        print("\n" + "=" * 50)
        print("Pass by Value vs Pass by Reference")
        print("=" * 50)
        
        # Pass by value (immutable type - int)
        print("\n--- Pass by Value (Immutable - Integer) ---")
        x = 5
        print(f"Before function call - x = {x}")
        result = change_x(x)
        print(f"After function call - x = {x} (unchanged)")
        print(f"Returned value = {result}")
        
        # Pass by reference (mutable type - list)
        print("\n--- Pass by Reference (Mutable - List) ---")
        my_list = [1, 2, 3, 4, 5]
        print(f"Before function call - list = {my_list}")
        change_list(my_list)
        print(f"After function call - list = {my_list} (modified)")
        
        print("\n" + "=" * 50)
        print("Note: In C++, 'x' would remain 5 (pass by value).")
        print("Python demonstrates pass by value for immutables,")
        print("but pass by reference for mutable objects.")
        print("=" * 50 + "\n")
        
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
