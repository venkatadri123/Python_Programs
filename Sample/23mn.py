#To display even numbers from m to n.
m=int(input('enter m value:'))
n=int(input('enter n value:'))
while m<=n:
    if m%2==0:
        print(m)
    m=m+1