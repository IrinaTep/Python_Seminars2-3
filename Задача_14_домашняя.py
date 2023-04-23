# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# n = int(input("Введите число: "))
# x = 1
# y = 2
# res = 0
# num_list = []
# for i in range(n):
#     while res <= n:
#         res = int(x*)
#         num_list.extend([res])
#         n = res
# print(num_list)

n = int(input("Введите число N: "))

# инициализируем переменную, которая будет хранить текущую степень двойки
power_of_two = 1

# выводим все степени двойки, пока они не превышают число N
while power_of_two <= n:
    print(power_of_two)
    power_of_two *= 2
