def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    print(f"\nOriginal list: {lst}")
    print(f"Value to find: {find_val}")
    print(f"Value to replace with: {replace_val}")
    lst_output = []
    for item in lst:
        if item == find_val:
            lst_output.append(replace_val)
        else:
            lst_output.append(item)
    print(f"Modified list: {lst_output}")
    return lst_output

if __name__ == "__main__":
    # Task 2
    # Invoke the function "find_and_replace" using the following scenarios:
    # - [1, 2, 3, 4, 2, 2], 2, 5
    # - ["apple", "banana", "apple"], "apple", "orange"

    find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)

    find_and_replace(["apple", "banana", "apple"], "apple", "orange")


