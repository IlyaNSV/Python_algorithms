import random
m=5
array=[random.randint(0,10) for i in range(2*m+1)]

print(array)
print(sorted(array))
def medi_finder(array):
    for i in range(len(array)):
        medi=array[i]
        right=0
        left=0
        same=0
        for j in range(len(array)):
            if j == i:
                same-=1
            if array[j]<array[i]:
                right+=1
            elif array[i]==array[j]:
                same+=1
            else:
                left+=1

        if right < left and right+same == left:
            return medi
        elif right > left and left+same==right:
            return medi
        elif right == left:
            return medi

print(medi_finder(array))
