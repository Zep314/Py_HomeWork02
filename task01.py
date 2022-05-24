# Задача 1
# Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

import random

# задаем начальные случайные данные
maxN = 5 
my_list = [random.randint(0,9) for i in range(0,maxN)]

def sum_odd(local_list):
    return sum([local_list[i] for i in range(0,len(local_list),2)]) # тут цикл for с шагом 2
                                                                    # по нечетный элементам
print('Начальный список')
print(my_list)
print(f'Сумма всех нечетных элементов списка равна {sum_odd(my_list)}')
