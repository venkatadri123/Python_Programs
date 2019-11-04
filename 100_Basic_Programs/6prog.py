"""6.Write a program that calculates and prints the value according to the
given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a
comma-separated sequence.
"""


"""from math import *
c=50
h=30
while True:
    d=int(input('enter value:'))
    x=int(sqrt((2*c*float(d))/h))
    print(x)"""

import math
c=50
h=30
l=[]
item=[x for x in input('enter:').split(',')]
for d in item:
    l.append(int(round(math.sqrt((2*c*float(d))/h))))
print(l)