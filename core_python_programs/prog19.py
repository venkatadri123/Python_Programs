# Find the biggest element in a list.
lst=[int(x) for x in input('enter numbers:').split(',')]
max=lst[0]
i=1
n=len(lst)
while i<n:
    if lst[i]>max:
        max=lst[i]
    i+=1
print('biggest number=',max)

