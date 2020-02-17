from random import *

print('Введите целочисленный диапазон')
a1=int(input('От: '))
a2=int(input('До: '))
print('Ваше число: '+str(randint(a1,a2)))

print('Введите диапазон для существенного числа')
b1=float(input('От: '))
b2=float(input('До: '))
print('Ваше число: '+str(uniform(b1,b2)))

print('Введите буквенный диапазон значений: ')
s1=input('Введите первую букву: ')
s2=input('Введите вторую букву: ')
s1=ord(s1)
s2=ord(s2)
s3=randint(s1,s2)
s3=chr(s3)
print('Ваша буква: '+s3)
