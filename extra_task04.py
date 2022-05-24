# Экстразадача 4
# Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?
import time

def my_max_dividers(n):
   ret = []
   d = 2
   while d * d <= n: # Используется свойство числа , 
                     # Макс. делитель меньше или равен квадратному корню числа
       if n % d == 0:
           ret.append(d)
           n //= d
       else:
           d += 1
   if n > 1:
       ret.append(n)
   return ret

M = 600851475143

start_time = time.time()
print(f'Наибольший делитель числа {M}, являющийся простым числом - {max(my_max_dividers(M))}')
print(f'Программа работала {time.time() - start_time} секунд [{time.strftime("%H:%M:%S",time.gmtime(time.time() - start_time))}]')

