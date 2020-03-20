# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых
# чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

#Python 3.7.0 (default, Jun 28 2018, 08:04:48) [MSC v.1912 64 bit (AMD64)] on win32

import random
import collections
import sys

n=8
def show(obj):
    print(f'type={type(obj)}, size={sys.getsizeof(obj)}, value={obj}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                show(key)
                show(value)
        elif not isinstance(obj, str):
            for item in obj:
                show(item)
    return sys.getsizeof(obj)


def show1(obj_list):
    sum=0
    for obj in obj_list:
        show(obj)
        sum+=sys.getsizeof(obj)
    return f'ВСЕГО ПАМЯТИ: {sum}'

def var1(n):
    obj_list=[]
    p = random.randint(10**40,10**41)
    l = p
    obj_list.append(p)
    obj_list.append(l)
    times = 0
    obj_list.append(times)
    while l != 0:
        x = l % 10
        if x == n:
            times += 1
        l = l // 10
    obj_list.append(l%10) #так мы посчитаем первый х, чтобы не вытаскивать его из цикла
    obj_list.append(times)
    #return times
    return show1(obj_list)
    #ВСЕГО ПАМЯТИ: 164

def var2(n):
    obj_list=[]
    p = str(random.randint(10 ** 40, 10 ** 41))
    obj_list.append(p)
    n = str(n)
    obj_list.append(n)
    new_p=collections.Counter(p)
    obj_list.append(new_p)
    obj_list.append(new_p[n])
    #return new_p[n],
    return show1(obj_list)
    #ВСЕГО ПАМЯТИ: 552

def var3(n):
    obj_list=[]
    p = random.randint(10 ** 40, 10 ** 41)
    result = []
    obj_list.append(p)
    while p > 0:
        result.append(p % 10)
        p //= 10
    result.reverse()
    obj_list.append(n)
    obj_list.append(result)
    obj_list.append(result.count(n))
    #return result.count(n),
    return show1(obj_list)
    #ВСЕГО ПАМЯТИ: 532

print(var1(n))
print(var2(n))
print(var3(n))

#ВЫВОД: Исходя из трех вариантов решений задачи, наиболее эффективным с точки зрения занимаемой памяти оказался первый,
# т.к он использует всего 4 переменных типа int и изменяет некоторые в процессе работы, второй и третий вариант работают
# с коллекцией/списком, которые "кушают" в разы больше памяти.