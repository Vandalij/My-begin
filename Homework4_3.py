import random

original_list = [random.randint(1, 20) for _ in range(random.randint(3, 10))]

new_list = [original_list[0], original_list[2], original_list[-2]]

print("Original list:", original_list)
print("New list:", new_list)