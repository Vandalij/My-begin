def sum_even_index_and_multiply_last(lst):
    if not lst:
        return 0

    sum_even_index = sum(lst[i] for i in range(0, len(lst), 2))
    result = sum_even_index * lst[-1]

    return result

print(sum_even_index_and_multiply_last([0, 1, 7, 2, 4, 8]))
print(sum_even_index_and_multiply_last([1, 3, 5]))
print(sum_even_index_and_multiply_last([6]))
print(sum_even_index_and_multiply_last([]))
