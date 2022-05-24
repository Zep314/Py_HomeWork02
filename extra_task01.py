# Экстразадача 1
#  Написать программу преобразования двоичного числа в десятичное.

def bin2dec(bin_str):
    my_list = list(map(int,bin_str))  # разбиваем строку на список посимвольно
    return  sum([my_list[i] * 2 ** (len(my_list) - 1 - i) for i in range(0,len(my_list))])

binstr='10010110'

print(f'Двоичное число {binstr} это {bin2dec(binstr)} десятичное')
