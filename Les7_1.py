import random
length=20
array = [random.randint(-100,99) for i in range(length)]

def bubble(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return f'Отсортированный массив: {array}'

print(f'Исходный массив: {array}')
print(bubble(array))
