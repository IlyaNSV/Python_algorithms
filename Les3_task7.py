import random
MIN = (-100)
MAX = 100
SIZE = 100
massive=[random.randint(MIN,MAX) for i in range(SIZE)]
min = massive[0]
for i in massive:
    if i < min: min = i

massive.remove(min)
min1 = massive[0]
for i in massive:
    if i < min1: min1 = i

print(min,min1)