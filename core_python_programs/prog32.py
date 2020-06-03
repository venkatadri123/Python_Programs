# To display given value if it exist in a list.
lst=[10,20,30,'venkey','hari',54,'suri',13,25]
n=int(input('enter a value:'))
for i in lst:
    if i==n:
        print('found')
        break
else:
    print('not found')
print('end')
