import random
matrix=[[int(input('Введите число:')) for i in range(4)] for j in range(4)]
print(matrix)
for i in range(len(matrix)):
    summ=0
    for j in range(len(matrix[i])):
        summ+=matrix[i][j]
    matrix[i].append(summ)
    print(matrix[i])
