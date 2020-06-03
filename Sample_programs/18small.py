#To check the smallest number given three numbers.
a=int(input('Enter a value='))
b=int(input('Enter b value='))
c=int(input('Enter c value='))
if a<b and a<c:
    print('a is small')
elif b<a and b<c:
    print('b is small')
else:
    print('c is small')