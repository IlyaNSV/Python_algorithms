import random


# вывод матрицы в ровном виде признаюсь нашел в интернете.
def printMatrix(matrix):
    for row in matrix:
        for x in row:
            print("{:4d}".format(x), end="")
        print()


length = 20
height = 10
matrix = [[random.randint(1, 100) for i in range(length)] for j in range(height)]
printMatrix(matrix)
min_list = []

for i in range(length):
    j = 0
    min = matrix[j][i]
    for j in range(height):
        if matrix[j][i] < min: min = matrix[j][i]
    min_list.append(min)
    j += 1

print(f'Список минимальных значений из каждого столбца:{min_list}')

max = min_list[0]

for i in range(len(min_list)):
    if min_list[i] > max: max = min_list[i]

print(f'Ответ: {max}')
