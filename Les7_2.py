import random

array=[round(random.uniform(0,50),2) for i in range(20)]

def merge_sort(array):
    if len(array)==1:
        return array
    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array

    left=merge_sort(array[:len(array)//2])
    right=merge_sort(array[len(array)//2:])
    i=j=0

    while len(left)>i and len(right)>j:
        if left[i]<right[j]:
            array[i+j]=left[i]
            i+=1
        else:
            array[i+j]=right[j]
            j+=1

    while len(left) > i:
        array[i+j]=left[i]
        i+=1
    while len(right) > j:
        array[i+j]=right[j]
        j+=1
    return array

print(array)
print(merge_sort(array))


