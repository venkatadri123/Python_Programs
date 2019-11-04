#Using for loop display a multiplication table.
n=int(input('enter a number'))
for i in range(1,11):
    print('%2dx%2d=%3d' %(i,n,i*n))
    print('{:2d}x{:2d}={:3d}'.format(i,n,i*n))
