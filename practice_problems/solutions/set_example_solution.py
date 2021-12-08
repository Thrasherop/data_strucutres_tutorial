"""Find if a Python list has any duplicates. 
This should be done in O(n) using a set. """

def has_duplicates(list):

    # Create a set to store the values
    s = set()

    # Iterate through the list and add each value to the set
    for val in list:
        s.add(val)

    # If the length of the set is not equal to the length of the list,
    # then there were duplicates that weren't added to the set
    if len(s) != len(list):
        return True
    else:
        return False


# Test the function
print(has_duplicates([1, 2, 3, 4, 5])) # False
print(has_duplicates([1, 2, 3, 4, 5, 1])) # True
print(has_duplicates([1, 2, 3, 4, 5, 6])) # False
print(has_duplicates([1, 1, 1, 1, 1])) # True