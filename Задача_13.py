# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. 
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, 
# помогающую синоптикам в работе. Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается 
# N целых чисел. Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50.
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

n = int(input("Введите количество чисел: "))
count = 0
countMax = 0

# range(5) -> 0, 1, 2, 3, 4 - генератор, который возвращает по одному элементу, но не хранит их памяти; 
# range можно модифицировать range (5, 10) -> 5, 6, 7, 8, 9
# range (1, 10, 2) -> 1, 3, 5, 7, 9
for i in range(n): # for используется, когда известно точное количество итераций (когда неизвестно, используем while)
    if int(input(f"Температура {i+1}:")) > 0:
        count += 1
        if count > countMax:
            countMax = count
    else:
       count = 0

print(f"Самая длинная оттепель {countMax} дней")