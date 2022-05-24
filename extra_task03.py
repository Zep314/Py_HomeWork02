# Экстразадача 3
# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. 
# Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.


# мое решение (сильно долго для больших чисел)
# def fib(n):
#     fib1 = fib2 = 1
#     while n > 1:
#         fib1, fib2 = fib2, fib1 + fib2
#         n -= 1
#     return fib2

import time
# ===== стырено отсюда: https://habr.com/ru/post/261159/  ===========
def pow(x, n, I, mult):
    """
    Возвращает x в степени n. Предполагает, что I – это единичная матрица, которая 
    перемножается с mult, а n – положительное целое
    """
    if n == 0:
        return I
    elif n == 1:
        return x
    else:
        y = pow(x, n // 2, I, mult)
        y = mult(y, y)
        if n % 2:
            y = mult(x, y)
        return y


def identity_matrix(n):
    """Возвращает единичную матрицу n на n"""
    r = list(range(n))
    return [[1 if i == j else 0 for i in r] for j in r]


def matrix_multiply(A, B):
    BT = list(zip(*B))
    return [[sum(a * b
                 for a, b in zip(row_a, col_b))
            for col_b in BT]
            for row_a in A]


def fib(n):
    F = pow([[1, 1], [1, 0]], n, identity_matrix(2), matrix_multiply)
    return F[0][1]

# ========= Конец стыренного ==============

# fib(1000000) - считается за 3 секунды!!!  >8-()


#N = 1000000

start_time = time.time()
#print(fib(34)) # для отладки

n = 2
limit = 4000000
summ = 0

fb = fib(0) # Тут уже сосчитаем первый элемент
while fb<limit:
    summ += fb
    n += 2
    fb = fib(n)

print(f'Сумма всех четных элементов ряда Фибоначчи, которые не превышают {limit} равна {summ}')
print(f'Самый большой элемент fib({n-2}) = {fib(n-2)}')
print(f'Программа работала {time.time() - start_time} секунд [{time.strftime("%H:%M:%S",time.gmtime(time.time() - start_time))}]')
