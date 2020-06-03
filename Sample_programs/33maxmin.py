#To find big & small number from the list.
l=[25,54,56,85,6,7,8,9,10,25,45]
max=l[0]
min=l[0]
n=len(l)
for i in range(1,n):
    if l[i]>max:
        max=l[i]
    if l[i]<min:
        min=l[i]
print('biggest=',max)
print('min=',min)