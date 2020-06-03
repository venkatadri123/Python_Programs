# Function Decorater:
#it returns another function, it decorates (or modifies) the value of another function.
# def decor(fun):
#     def inner():
#         res=fun()
#         res+=10
#         return res
#     return inner
# def myfunction():
#     return 100
# x=decor(myfunction)
# print('result=',x())

# Function Decorater:
def decor(fun):
    def inner():
        n=int(input('enter:'))
        res=fun()
        res+=n
        return res
    return inner
@decor
def myfunction():
    return 100
x=myfunction()
print('result=',x)
