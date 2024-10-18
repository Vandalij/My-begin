# int -> ціле число 12
# float -> дробове число 12.5
# bool -> логічний тип данних: True False
#  str -> рядок - масив (набір) символів

# Змінна - це іменована область оперативноі пам'яті значення можна змінювати
# number: int = 10 +2
# print(number)
# print(type(number))
# number = 20.5
# print(number)
# print(type(number))
# number = "Vasia"
# print(number)
# print(type(number))
# number = True
# print(number)
# print(type(number))

# a1 = 10 # не правильно і не понятно
# a2 = 20
# first_number = 10 # правильно і понятно
# second_number = 20
#
# userName1 = "Vasya" # CamelCase - верблюжа нотація
# print(userName1)
# user_name = "Petya" # SnaceCase - зміїна нотація (рекомендовано для Python)
# print(user_name)
#
# NUMBER = 10 # константа - незміне значеня
#
# name = "Vasya"
# age = 33

# user_name = name + str(age)
# print(user_name)

############
 # number1 = 10
# print(number1)
# print(number := 10+1) # моржовий оператор

#########
# оператори математичні і логічні
# унарні - меже бути тільки одтин операнд (наприклад -5) тут мінус унарний
# бінарні - працює з двома операндами (наприклад 2+2)
# операнд - це значення над яким проводить операцію оператор (математичний або логфічний)

# + - * /
# print(2 + 3)
# print(2 - 3)
# print(2 * 3)
# print(2 / 3)
# print(2 ** 3) # основа ** показник (зведення в ступінь)
# print(2 // 3) # ціла частина від розподілу
# print( 2 % 3) # залишок від ділення
# #
num1 = 15
num2 = 8
print(num1 // num2)
print(num1 % num2)
print(-4)

# ctrl + / = закоментувати

######
# ввести з клавіатури трьохзначне число та вивести суму цифр цього числа
# // %

# 274 => 2 + 7 + 4

number = 123
n1 = number // 100
# v1
n2 = number // 10 % 10
# v2
n2 = number % 100 //10
n3 = number % 10

print(n1)
print(n2)
print(n3)

result  = n1 + n2 + n3

print("Result: ", result)




