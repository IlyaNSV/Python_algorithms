# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
n = int(input('Введи число n: '))
number = 1
i = 1
summ = 0

while i <= n:
    summ += number
    number = number / (-2)
    i += 1

print(summ)
