def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    # Print the dictionary before updating
    print(f"\nDictionary before update: {dct}")

    # Check if the key already exists in the dictionary
    if key in dct:
        # Print the original value
        print(f"The key is already present. Updated value from {dct[key]} to {value}.")
        # Update the value for the existing key
        dct[key] = value
    else:
        # If the key does not exist, add it to the dictionary
        print(f"The key is not present. Adding key-value pair: {key}: {value}.")
        dct[key] = value
    # Return the updated dictionary
    print(f"Dictionary after update: {dct}")
    return dct

if __name__ == "__main__":
    # Task 2
    # Invoke the function "update_dictionary" using the following scenarios:
    # - {}, "name", "Alice"
    # - {"age": 25}, "age", 26
    update_dictionary({}, "name", "Alice")
    update_dictionary({"age": 25}, "age", 26)


