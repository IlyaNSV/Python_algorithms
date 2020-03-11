# Условие задачи 3 урока номер 5: В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
# позицию в массиве. Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два
# абсолютно разных значения.

import random
import timeit
import cProfile

SIZE=100

massive1 = [random.randint(-10000, 10000) for i in range(SIZE)]
massive2 = [random.randint(-10000, 10000) for i in range(2*SIZE)]
massive4 = [random.randint(-10000, 10000) for i in range(4*SIZE)]
massive8 = [random.randint(-10000, 10000) for i in range(8*SIZE)]
massive16 = [random.randint(-10000, 10000) for i in range(16*SIZE)]
massive_cube= [random.randint(-10000, 10000) for i in range(SIZE**4)]

def cycle_method(massive):
    minus_massive=[]
    for i in massive:
        if i < 0: minus_massive.append(i)

    answer=minus_massive[0]

    for i in minus_massive:
        if i > answer: answer = i

    return f'Ответ:{answer}'



print(timeit.timeit('cycle_method(massive1)', number=100, globals=globals())) #0.012831699999999994
print(timeit.timeit('cycle_method(massive2)', number=100, globals=globals())) #0.0260696
print(timeit.timeit('cycle_method(massive4)', number=100, globals=globals())) #0.05177180000000001
print(timeit.timeit('cycle_method(massive8)', number=100, globals=globals())) #0.095798
print(timeit.timeit('cycle_method(massive16)', number=100, globals=globals())) #0.19032600000000002

cProfile.run('cycle_method(massive_cube)')

# 49998393 function calls in 13.295 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.470    0.470   13.295   13.295 <string>:1(<module>)
#         1    8.847    8.847   12.824   12.824 Les3_task5_variations.py:18(cycle_method)
#         1    0.000    0.000   13.295   13.295 {built-in method builtins.exec}
#  49998389    3.977    0.000    3.977    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

def function_method(massive):
    minus_massive = []
    massive.sort()
    for i in massive:
        if i < 0: minus_massive.append(i)
        else: break

    answer = max(minus_massive)
    return f'Ответ:{answer}'

print(timeit.timeit('function_method(massive1)', number=100, globals=globals())) #0.012580199999999986
print(timeit.timeit('function_method(massive2)', number=100, globals=globals())) #0.026386100000000023
print(timeit.timeit('function_method(massive4)', number=100, globals=globals())) #0.054767399999999966
print(timeit.timeit('function_method(massive8)', number=100, globals=globals())) #0.10675009999999996
print(timeit.timeit('function_method(massive16)', number=100, globals=globals())) #0.21706740000000002

cProfile.run('function_method(massive_cube)')

# 49998395 function calls in 52.770 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    1.561    1.561   52.770   52.770 <string>:1(<module>)
#         1   13.351   13.351   51.209   51.209 Les3_task5_variations.py:51(function_method)
#         1    0.000    0.000   52.770   52.770 {built-in method builtins.exec}
#         1    4.383    4.383    4.383    4.383 {built-in method builtins.max}
#  49998389    4.011    0.000    4.011    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1   29.464   29.464   29.464   29.464 {method 'sort' of 'list' objects}

def another_cycle_method(massive):
    answer=min(massive)
    for i in massive:
        if i < 0:
            if i > answer: answer = i
    return answer

print(timeit.timeit('another_cycle_method(massive1)', number=100, globals=globals())) #0.012290000000000134
print(timeit.timeit('another_cycle_method(massive2)', number=100, globals=globals())) #0.024346300000000154
print(timeit.timeit('another_cycle_method(massive4)', number=100, globals=globals())) #0.04701770000000005
print(timeit.timeit('another_cycle_method(massive8)', number=100, globals=globals())) #0.09402109999999997
print(timeit.timeit('another_cycle_method(massive16)', number=100, globals=globals())) #0.19425500000000007

cProfile.run('another_cycle_method(massive_cube)')

# 5 function calls in 24.043 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   24.043   24.043 <string>:1(<module>)
#         1   15.218   15.218   24.043   24.043 Les3_task5_variations.py:82(another_cycle_method)
#         1    0.000    0.000   24.043   24.043 {built-in method builtins.exec}
#         1    8.825    8.825    8.825    8.825 {built-in method builtins.min}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# По сути все три алгоритма похожи по смыслу, но немного отличаются в исполнении:
# 1) В первом мы циклом отбирали отрицательные элементы, а потом другим циклом сравнивали значения для поиска максимума
# 2) Во втором мы сократили цикл тем, что отсортировали изначальный список и оттуда вытащили все элементы до положительных чисел в другой,
# отрицательный список, где нашли максимум через функцию max
# 3) В третьем варианте мы сразу искали ответ, проходя по исходному списку через ряд условий
# ВЫВОД: Несмотря на разные скрипты для решения задачи, время ее выполнения примерно одинаковое при небольших объемах данных,
# зависимость от количества данных N линейная, но когда объем данных больше, 1 функция оказывается самой эффективной (13.3 секунды),
# 2 функция самая неэффективная (52,77 секунды), только функция sort в ней занимает 29.5 секунды, 3 (24 секунд) функция похоже на 1,
# но разница во времени между ними обусловлена поиском функциии min (8,8 секунды).


