# Write a function that calculates power value of a number.
def power(x,n):
    res=x**n
    return res,x,n
num=float(input('enter value:'))
powe=float(input('enter value:'))
res,x,n=power(num,powe)
print('%.2f raised to the power of %.2f is %.2f' %(x,n,res))
