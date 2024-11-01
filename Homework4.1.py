def move_zeros_to_end(lst):

    non_zero_elements = [num for num in lst if num != 0]
    zero_count = lst.count(0)
    result = non_zero_elements + [0] * zero_count
    return result

print(move_zeros_to_end([0, 1, 0, 12, 3]))
print(move_zeros_to_end([0]))
print(move_zeros_to_end([1, 0, 13, 0, 0, 0, 5]))
print(move_zeros_to_end([9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]))
