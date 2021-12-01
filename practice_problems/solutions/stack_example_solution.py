# Make a function that can verify that
# every opening brace has a corrosponding 
# opening brace



def verify_braces(string):
    
    # Create a stack to keep track of braces
    braces_stack = []

    # Loops through all the characters in the string
    for char in string:

        # If it is an opening brace, append it to the stack
        if char == '{':
            braces_stack.append(char)

        # Attempt to close the brace
        if char == '}':

            # If there is a closing brace but no more
            # Opening braces, then the } is does not match
            # and the function returns false
            if len(braces_stack) < 1:
                return False

            else:
                braces_stack.pop()

    # If the stack is empty, that means all braces were
    # closed and it returns true. Otherwise it returns false

    if len(braces_stack) != 0:
        return False
    else:
        return True




# Test cases
print(verify_braces("{Berries and cream}")) # True
print(verify_braces("{{{Berries and {ream}}")) # False
print(verify_braces("I'm a little}lad who loves{ berries and cream}")) # False
print(verify_braces("{Up the octive{ go for it!}}")) # True

