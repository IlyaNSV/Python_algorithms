from collections import deque
from collections import defaultdict

numb_dict=defaultdict(int)
numb_dict.update({'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15})

def check(el):
    if el.isdigit() == True:
        return int(el)
    elif el == ' ' or el == '' : return 0
    else: return int(numb_dict.get(el))

def get_key(value):
    for k, v in numb_dict.items():
        if v == value:
            return k

fnstr=input('1: ').upper()
snstr=input('2: ').upper()

fnstr.split()
snstr.split()

fn=deque(fnstr)
sn=deque(snstr)

while len(fn) < len(sn): fn.appendleft(' ')
while len(fn) > len(sn): sn.appendleft(' ')

print(fn,'+',sn, sep='\n')

fn.reverse()
sn.reverse()
answer=deque()
temp_el=0
for i in range(len(fn)):
    el1=check(fn[i])
    el2=check(sn[i])
    sum = el1 + el2 + temp_el
    temp_el=0
    if sum > 9 and sum <= 15: sum=get_key(sum)
    elif sum > 15:
        sum = sum-16
        temp_el+=1
        if sum > 9 : sum=get_key(sum)
    answer.append(sum)

answer.reverse()
print('____________________________')

print(answer)

