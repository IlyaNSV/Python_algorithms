import random
MIN = (-100)
MAX = 100
SIZE = 100
massive=[random.randint(MIN,MAX) for i in range(SIZE)]
min = massive[0]
max = massive[0]

for i in massive:
    if i < min: min = i
    if i > max: max = i

if massive.index(min) < massive.index(max):
    start = massive.index(min)
    finish = massive.index(max)
else:
    start = massive.index(max)
    finish = massive.index(min)

answer = 0

for i in range(start + 1, finish):
    answer += massive[i]

print(f'Ответ:{answer}')
