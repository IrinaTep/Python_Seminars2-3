# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# n = int(input("Введите число: "))
# i = 0
# flag = 0
# a = 0
# b = 1

# while (n >= a):
#     print(f"{a} {i+1}")
#     if (a==n):
#         flag = 1
#     temp = a + b
#     a = b
#     b = temp
#     i += 1

# if flag==1:
#     print(f"Номер {i}")
# else:
#     print(f"Номер -1")

# Второй вариант решения (не учли, что ряд Фибоначчи начинается с 0)
# A = int(input("Введите число: "))
# x1 = 1
# x2 = 1
# n = 3

# while x2 < A:
#     sum = x1 + x2
#     x1 = x2
#     x2 = sum
#     n += 1
# else:
#     if A == x2:
#         print(f"n = {n}")
#     else:
#         print(f"Число {A} не входит в последовательность Фибоначчи")

# Третий вариант решения (нужно поправить индекс)
# print("Введите A: ")
# numb = int(input())
# fib1 = fib2 = 1
# fib_sum = 2
# fib_idx = 2

# while fib2 < numb:
#     fib_sum = fib2 + fib1
#     fib1 = fib2
#     fib2 = fib_sum
#     fib_idx += 1
#     # print(f"fib_idx = {fib_idx}, fib_sum = {fib_sum}")
# if(fib_sum == numb):
#     print(f"fib_idx = {fib_idx + 1}") # по примеру +1, в вики с 0 начало
# else:
#     print(f"-1")
# print(fib_idx if (fib2 == numb) else "-1")

# Четвертый вариант решения
# number = input("Enter a number: ")
# numPrev = 0
# numCur = 1
# numNext = 0
# fibo = str(numPrev) + " " + str(numCur)
# while int(number) >= numNext:
#     numNext = numCur + numPrev
#     fibo = fibo + " " + str(numNext)
#     numPrev = numCur
#     numCur = numNext
# fibo = fibo.split(" ")
# if number in fibo:
#     print(fibo.index(number) +1)
# else:
#     print(-1)

# print(fibo.index(number) +1 if number in fibo else -1) 


n = int(input("Введите число: "))
f_i = 2
f_1 = 0
f_2 = 1

while f_2 < n:
    # В Python можно сократить эту запись
    # temp = f_1 + f_2   
    # f_1 = f_2
    # f_2 = temp
    f_1, f_2 = f_2, f_1 + f_2
    f_i += 1

if (f_2 == n):
    print(f"Номер {f_i}")
else:
    print(f"Номер -1")