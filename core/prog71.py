# Write a function that returns square value of a number, and convert into lambda.
def squre(n):
    m=n*n
    return m
res=squre(5)
print('squre value=',res)

# Above function converting into lambda function.
f=lambda x: x*x
print('square value=',f(5))
