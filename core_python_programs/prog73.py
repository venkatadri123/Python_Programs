# Write a lambda function to test weather a given number is even or odd.
def even_odd(n):
    if n==0:
        str='it is zero'
    elif n%2==0:
        str='even'
    else:
        str='not even'
    return str
x=even_odd(10)
print('x is',x)

# Converting into lambda function.
f=lambda n:'even' if n%2==0 else 'not even'
print('n is',f(6))
