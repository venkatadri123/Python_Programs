#To display even numbers from m-n without using step size.
m=int(input('enter a number'))
n=int(input('enter b value'))
for i in range(m,n):
    if i%2==0:
        print(i)
