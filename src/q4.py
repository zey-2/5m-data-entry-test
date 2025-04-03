def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    print(f"\nOriginal string: {s}")
    if isinstance(s, str):
        s_reversed = s[::-1]
        print(f"Reversed string: {s_reversed}")
        return s_reversed
    else:
        print("Error: Input must be a string.")

    return None

if __name__ == "__main__":
    # Task 2
    # Invoke the function "string_reverse" using the following scenarios:
    # - "Hello World"
    # - "Python"
    string_reverse("Hello World")
    string_reverse("Python")
