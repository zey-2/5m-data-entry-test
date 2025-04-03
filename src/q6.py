def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    print(f"\nSearching for the 1st negative in {lst}")

    index = 0
    while index < len(lst):
        if lst[index] < 0:
            print(f"Found negative: {lst[index]}")
            return lst[index]
        index += 1
    print("No negatives found")
    return "No negatives"

if __name__ == "__main__":
    # Task 2
    # Invoke the function "find_first_negative" using the following scenario:
    # - [3, 5, -1, 7, -2, 8]
    # - [2, 10, 7, 0]
    find_first_negative([3, 5, -1, 7, -2, 8])
    find_first_negative([2, 10, 7, 0])
