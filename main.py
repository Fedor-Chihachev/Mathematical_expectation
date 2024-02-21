import numpy as np

# Считываем входные данные
a = np.array(list(map(int, input().split())))
k = int(input())

# Вычисляем уникальные значения и их частоты в массиве a
c = np.unique(a, return_counts=True)

# Инициализируем переменную для математического ожидания всех чисел после первого
vt = 0
count_numbers = len(a)

# Вычисляем математическое ожидание всех чисел после первого
for i in range(len(c[1])):
    vt += ((c[1][i] / count_numbers) * (count_numbers - c[1][i]) / count_numbers) * c[0][i]

# Вычисляем математическое ожидание для первого числа
mat = sum(a) / count_numbers

# Вычисляем математическое ожидание суммы согласно формуле
ex = mat + (k-1) * vt

# Выводим результат
print(ex)
