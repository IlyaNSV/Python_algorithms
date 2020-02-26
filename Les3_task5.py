import random
MIN = (-100)
MAX = 100
SIZE = 100
massive=[random.randint(MIN,MAX) for i in range(SIZE)]
minus_massive=[]
for i in massive:
    if i < 0: minus_massive.append(i)

answer=minus_massive[0]
for i in minus_massive:
    if i > answer: answer = i

print(minus_massive)
print(f'Ответ:{answer}, позиция в списке: {minus_massive.index(answer)+1}')


