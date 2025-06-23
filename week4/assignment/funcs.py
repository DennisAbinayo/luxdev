# FUNCTIONS

## Exercises

def greet(name):
    """Print a greeting message with the given name."""
    print(f"Hello, {name}")

def add(a, b):
    """Return the sum of two numbers and print whether the result is even or odd."""
    result = a + b
    print("even" if result % 2 == 0 else "odd")
    return result



# Challenge
def calculator(a, b, operation):
    """Perform a mathematical operation on two numbers."""
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Error: Invalid operation"

def demonstrate_function_calls():
    """Demonstrate calling functions from within another function."""
    print("Demonstrating function calls:")
    
    # Call greet function
    greet("Alice")
    
    # Call add function
    sum_result = add(5, 3)
    print(f"The sum is: {sum_result}")
    
    # Call add function again
    add(4, 6)
    
    # Test calculator function
    print("\nTesting calculator function:")
    print(f"10 + 5 = {calculator(10, 5, '+')}")
    print(f"10 - 5 = {calculator(10, 5, '-')}")
    print(f"10 * 5 = {calculator(10, 5, '*')}")
    print(f"10 / 5 = {calculator(10, 5, '/')}")

# Example usage
if __name__ == "__main__":
    # Test individual functions
    greet("World")
    result = add(10, 5)
    print(f"Result: {result}")
    
    # Demonstrate calling functions from within another function
    demonstrate_function_calls()


