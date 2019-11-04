#To check x is devisable by y or not.
x=float(input('enter x value:'))
y=float(input('enter y value:'))
if x==0:
    print('x is zero')
elif x%y==0:
    print('yes x is devisable by y')
else:
    print('no x is not devisable by y')