# To retrive only even numbers from a list using while loop.
lst=[10,12,-10,-20,23,-25,-21,41]
n=len(lst)
i=0
while i<n:
    if lst[i]%2==0:
        print('even numbers=',lst[i])
    i+=1
