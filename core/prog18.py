# Find the sum of elements in a given list.
lst=[int(x) for x in input('enter numbers:').split(',')]
sum=0
n=len(lst)
i=0
while i<n:
    sum+=lst[i]
    i+=1
print('sum=',sum)
