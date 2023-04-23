# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите число: "))
num_list = []
norm_x = [0, 1]
for i in range(n):
    # Гоняем цикл до тех пор пока пользователь не введёт значение из контрольного списка norm_x
    flag = True
    while flag:
        zn = int(input("Введите сторону монетки: "))
        if zn in norm_x:
            flag = False
        else:
            print("Некоррректный ввод")
        
    num_list.append(zn)
        
print(num_list)

tails_counter = 0
eagle_counter = 0
for i in range(0, len(num_list)):
    if num_list[i] == 0:
        tails_counter += 1
    else:
        eagle_counter += 1

if tails_counter < eagle_counter:
    print(f"Необходимо перевернуть {tails_counter} монетки")
else:
    print(f"Необходимо перевернуть {eagle_counter} монетки")
