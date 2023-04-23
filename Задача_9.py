# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 
# 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120

N = int(input("Введите число: "))
i = 1
res = 1

while i <= N:
    res *= i
    i += 1

print(res)

# Второй вариант решения:
# a = int(input("Введите число: "))
# count = 1
# while a > 1:
#     count = count*a  # factorial *= a
#     a -= 1
# print(count)
# print("Цикл окончен")