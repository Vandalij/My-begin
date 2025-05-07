import string
import keyword

def is_valid_variable_name(name):
    if not name:
        return False
    if name[0].isdigit():
        return False
    if any(char.isupper() for char in name):
        return False
    if any((char in string.punctuation and char != "_") or char.isspace() for char in name):
        return False
    if name == "_":
        return True
    if name.count("_") == len(name):
        return False
    if name in keyword.kwlist:
        return False
    return True

name = input("Enter a variable name: ")
result = is_valid_variable_name(name)
print(result)