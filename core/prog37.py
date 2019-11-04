# To display a given string is found or not and display position no also.
lst=['hari','venkey','suri','hello']
n=input('enter a string:')
a=len(n)
l=len(lst)
for i in lst:
    if i==n:
        print('found')
        break
else:
    print('not found')
print(a)
print('end')    
