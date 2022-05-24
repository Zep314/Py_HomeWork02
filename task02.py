# Задача 2
# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

import random
import math

# задаем начальные случайные данные
maxN = 11 
my_list = [random.randint(0,9) for i in range(0,maxN)]
#my_list = [2, 3, 4, 5, 6]


def mul_pairs(local_list): # math.ceil() - округление в большую сторону
    return [local_list[i] * local_list[len(local_list)-1-i] for i in range(0, math.ceil(len(local_list)/2) )]

print('Начальный список:')
print(my_list)
print('Посчитанный список:')
print(mul_pairs(my_list))
