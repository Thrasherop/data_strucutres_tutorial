def reverse_string(string):
    all_letters_stack = []

    for character in string:
        all_letters_stack.append(character)

    
    reversed_string = ""

    while len(all_letters_stack) > 0:
        reversed_string += all_letters_stack.pop()

    return reversed_string

print(reverse_string("foo"))