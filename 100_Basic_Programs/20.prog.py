"""20.Define a class with a generator which can iterate the numbers,
which are divisible by 7, between a given range 0 and n."""


# def gen(n):
#     a = 0
#     l=[]
#     while a<n:
#         j=a
#         j+=1
#         if j%7==0:
#             yield j
#         for i in range(70):
#             l.append(i)
#         print(l)

def putNumbers(n):
    i=0
    while i<n:
        if i%7==0:
            yield i
        i += 1
x=int(input('enter:'))
res=putNumbers(x)
print(list(res))