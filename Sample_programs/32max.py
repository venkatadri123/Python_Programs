#To find a giggest number in a list.
l=[10,12,14,15,-20,22,11]
max=l[0]
n=len(l)
for i in range(1,n):
    if l[i]>max:
        max=l[i]
print('max=',max)