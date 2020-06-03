#To accept square root values from key board and display.
# a.how many numbers are there.
# b.their combination product.
import math
a=[float(x) for x in input('enter values:').split(',')]
a=a**0.5
print('square root values:',a)
n=len(0)
for i in a:
    print(i)
    i+=len(i)
