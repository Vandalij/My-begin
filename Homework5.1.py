import string
import keyword

def is_valid_variable_name(name):
    if not name:
        return False
    if name[0].isdigit():
        return False
    if any(char.isupper() for char in name):
        return False
    if any(char in (set(string.punctuation) - {"_"}) or char.isspace() for char in name):
        return False
    if "__" in name:
        return False
    if name in keyword.kwlist:
        return False
    return True
examples = [
    "_",
    "__",
    "___",
    "x",
    "get_value",
    "get value",
    "get!value",
    "some_super_puper_value",
    "Get_value",
    "get_Value",
    "getValue",
    "3m",
    "m3",
    "assert",
    "assert_exception"
]

for name in examples:
    result = is_valid_variable_name(name)
    print(f"{name} => {result}")
