# Using while loop display numbers Disending order from m - n.
m,n=[int(x) for x in input('enter numbers:').split(',')]
while m>=n:
    print(m)
    m-=1
