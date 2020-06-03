# To display only Negetive numbers from a list.
lst=[int(x) for x in input('enter numbers:').split(',')]
n=len(lst)
i=0
while i<n:
    if lst[i]<0: print(lst[i])
    i+=1
