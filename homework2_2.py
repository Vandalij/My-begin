number = int(input("enter your number: "))

n1 = number // 10000
n2 = (number // 1000) % 10
n3 = (number // 100) % 10
n4 = (number // 10) % 10
n5 = number %10

reversed_result = n5 * 10000 + n4 * 1000 + n3 * 100 + n2 * 10 + n1

print(f"your number result: {reversed_result}")