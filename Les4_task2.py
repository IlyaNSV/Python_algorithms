# coding=utf-8
import math
import timeit
import cProfile

easy_numbers=[]
n=2

def easy_check(number):
    i = number-1
    while i > 1:
        if number % i != 0:
            i -= 1
        else: return 'no'
    return number

def prime(i):
    n=1
    while len(easy_numbers) <= i:
        if easy_check(n) != 'no':
            easy_numbers.append(n)
        n+=1
    return (easy_numbers[i])

print(timeit.timeit('prime(n)', number=100, globals=globals())) #2.6700000000004498e-05
print(timeit.timeit('prime(n*2)', number=100, globals=globals())) #2.1199999999998997e-05
print(timeit.timeit('prime(n*4)', number=100, globals=globals())) #2.2499999999994746e-05

cProfile.run('prime(n**12)')

# 81659 function calls in 57.483 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   57.483   57.483 <string>:1(<module>)
#         1    0.037    0.037   57.483   57.483 Les4_task2.py:15(prime)
#     38783   57.439    0.001   57.439    0.001 Les4_task2.py:7(easy_check)
#         1    0.000    0.000   57.483   57.483 {built-in method builtins.exec}
#     38784    0.006    0.000    0.006    0.000 {built-in method builtins.len}
#      4088    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

def sieve(p):
    n=math.ceil((p**1.0859)*4.8361) #используем степенную регрессию для поиска длины изначального списка,
    # чтобы в нем было простое число с позицией p
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    sieve = [i for i in sieve if i != 0]
    return sieve[p-1]

print(timeit.timeit('sieve(n)', number=100, globals=globals())) #0.00032200000000000284
print(timeit.timeit('sieve(n*2)', number=100, globals=globals())) #0.0008797000000000006
print(timeit.timeit('sieve(n*4)', number=100, globals=globals())) #0.0010005000000000014

cProfile.run('sieve(n**12)')
# 7 function calls in 0.015 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.015    0.015 <string>:1(<module>)
#         1    0.013    0.013    0.015    0.015 Les4_task2.py:44(sieve)
#         1    0.002    0.002    0.002    0.002 Les4_task2.py:47(<listcomp>)
#         1    0.001    0.001    0.001    0.001 Les4_task2.py:56(<listcomp>)
#         1    0.000    0.000    0.015    0.015 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method math.ceil}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#ВЫВОД Классический способ проверки каждого числа выигрывает решето только при поиске простого числа с небольшой позицией,
# но при поиске с большой или очень большой позицией решето делает это быстрее в 3832 ГОСПОДИ РАЗА. Вот это было круто.