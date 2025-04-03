def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    print(f"\nOriginal values: x = {x}, y = {y}")
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        print("Error: x and y must be numeric.")
        return -1
    
    x, y = y, x
    print(f"Swapped values: x = {x}, y = {y}")
    return

if __name__ == "__main__":


    # Task 2
    # Invoke the function "swap" using the following scenarios:
    # - "Apple", 10
    # - 9, 17
    swap("Apple", 10)  # Expected output: -1
    swap(9, 17)  # Expected output: 17 9