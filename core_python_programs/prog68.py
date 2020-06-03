# Generator.

#Write a function using while loop that displays number from m to n.
def mygen(m,n):
    while m<=n:
        print(m)
        m+=1
mygen(1,10)

#Write a function using while loop that displays number from m to n.
def mygen(m,n):
    while m<=n:
        yield m
        m+=1
obj=mygen(10,20)
print(obj)
for i in obj: print(i)
