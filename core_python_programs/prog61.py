# Recursive function.
def fact(n):
    if n==0:
        res=1
    else:
        res=n*fact(n-1)
    return res
r=fact(5)
print('result=',r)


# Recursive function(2).
def fact(n):
    if n==0:
        res=1
    else:
        res=n*fact(n-1)
    return res
num=int(input('enter a no:'))
r=fact(num)
print('factorial of {} is {}'.format(num,r))
