def split_list(lst):

    midl = (len(lst) + 1) // 2
    first_half = lst[:midl]
    second_half = lst[midl:]
    return [first_half, second_half]

print(split_list([1, 2, 3, 4, 5, 6]))
print(split_list([1, 2, 3]))
print(split_list([1, 2, 3, 4, 5]))
print(split_list([1]))
print(split_list([]))