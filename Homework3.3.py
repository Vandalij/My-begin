def split_list(lst):

    mid = (len(lst) + 1) // 2
    first_half = lst[:mid]
    second_half = lst[mid:]
    return [first_half, second_half]

print(split_list([1, 2, 3, 4, 5, 6]))
print(split_list([1, 2, 3]))
print(split_list([1, 2, 3, 4, 5]))
print(split_list([1]))
print(split_list([]))