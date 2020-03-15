from collections import deque
from collections import defaultdict
n=int(input('Введите количество компаний для ввода: '))
def companies(n):
    company_dict = defaultdict(list)
    avg=0
    companies_below = []
    companies_upper = []
    for i in range(1, n+1):
        name = (input(f'Введите название компании номер {i} '))
        company=deque()
        company.append(int(input(f'Введите прибыль за первый квартал компании {name} ')))
        company.append(int(input(f'Введите прибыль за второй квартал компании {name} ')))
        company.append(int(input(f'Введите прибыль за третий квартал компании {name} ')))
        company.append(int(input(f'Введите прибыль за четвертый квартал компании {name} ')))
        company.append(sum(company))
        company.appendleft(name)
        avg+=company[5]
        company_dict[i].append(company)
    avg=avg/n
    print(company_dict)
    for i in company_dict.keys():
        val1=company_dict.get(i)[0][5]
        val2=company_dict.get(i)[0][0]
        if val1 >= avg: companies_upper.append(val2)
        else: companies_below.append(val2)
    return f' Средняя выручка: {avg}, компании с выручкой меньше средней: {companies_below},компании с выручкой больше/равной средней: {companies_upper}'

print(companies(n))