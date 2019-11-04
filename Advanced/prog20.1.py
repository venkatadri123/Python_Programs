# (20.1) Using try block and except method.
try:
    print('Open the file')
    a,b=[int(i) for i in input('enter two numbers:').split()]
    c=a/b
    print('result=',c)
    print('close all files')

except ZeroDivisionError:
    print('division by 0 happent')
    print('please do not input 0')
print('close all files')
