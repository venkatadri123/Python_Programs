# Write a Function Decorater that decrease the result of another functin by 10%.
def decor(fun):
    def inner():
        res=fun()
        n=res/10
        res-=n
        return res
    return inner
@decor
def myfunction():
    return 150
x=myfunction()
print('result=',x)