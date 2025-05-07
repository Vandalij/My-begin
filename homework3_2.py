def move_last_to_first(lst):

    if len(lst) <= 1:
        return lst
    else:
        return [lst[-1]] + lst[:-1]

print(move_last_to_first([12, 3, 4, 10]))       # Виведе: [10, 12, 3, 4]
print(move_last_to_first([1]))                  # Виведе: [1]
print(move_last_to_first([]))                   # Виведе: []
print(move_last_to_first([12, 3, 4, 10, 8]))