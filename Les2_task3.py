# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.

num = int(input('Введите число: '))


def change(num):
    x = num % 10
    new_num = num // 10
    if new_num == 0:
        return f'{x}'
    else:
        return f'{x}{change(new_num)}'


print(change(num))
