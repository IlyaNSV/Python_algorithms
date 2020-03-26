import hashlib,sys,cProfile

def show(obj):
    #print(f'type={type(obj)}, size={sys.getsizeof(obj)}, value={obj}')
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

def just_find(s):
    hash_list = []
    s = list(s)
    el_numb=1
    while el_numb < len(s):
        for i in range(len(s)):
            el = s[i]
            if el_numb!=1:
                for j in range(1,el_numb):
                    try:
                        el+=s[i+j]
                    except LookupError:
                        break
            if el not in hash_list:
                hash_list.append(el)
        el_numb+=1
    return f'Ответ:{len(hash_list)}', show1(hash_list)

print(just_find('мама мыла раму'))
cProfile.run("just_find('мама мыла раму')")

def hash_and_find(s):
    hash_list = []
    s = [hashlib.sha1(i.encode('utf-8')).hexdigest() for i in s]
    el_numb=1
    while el_numb < len(s):
        for i in range(len(s)):
            el = s[i]
            if el_numb!=1:
                for j in range(1,el_numb):
                    try:
                        el+=s[i+j]
                    except LookupError:
                        break
            if el not in hash_list:
                hash_list.append(el)
        el_numb+=1
    return f'Ответ:{len(hash_list)}', show1(hash_list)

print(hash_and_find('мама мыла раму'))
cProfile.run("hash_and_find('мама мыла раму')")