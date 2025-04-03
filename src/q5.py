def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    print(f"\nChecking divisibility of {num} by {divisor}...")
    if divisor == 0:
        print("Divisor cannot be zero.")
        return False
    if num % divisor == 0:
        print(f"{num} is divisible by {divisor}.")
        return True
    else:
        print(f"{num} is not divisible by {divisor}.")
        return False

if __name__ == "__main__":
    # Task 2
    # Invoke the function "check_divisibility" using the following scenarios:
    # - 10, 2
    # - 7, 3
    check_divisibility(10, 2)
    check_divisibility(7, 3)
