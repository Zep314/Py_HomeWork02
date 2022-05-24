# Задача 3
# В заданном списке вещественных чисел найдите разницу между максимальным и 
# минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
import math

# задаем начальные случайные данные
maxN = 6 
my_list = [random.random()*20 for i in range(0,maxN)]
#my_list = [1.1, 1.2, 3.1, 5, 10.01]

def my_diff(local_list):  # math.trunc() - возвращает целую часть числа
    work_list = [my_list[i]-math.trunc(my_list[i]) for i in range(0,len(local_list))]
    return max(work_list)-min(work_list)

print('Начальный список:')
print(my_list)
print(f'Разница между максимальным и минимальным значениями дробной части элементов списка равна {my_diff(my_list)}')
