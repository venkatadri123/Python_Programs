# Return.
#Write a function that returns squar root values in calling place.
def squ_root(n):
    m=n**0.5
    return m
res=squ_root(25)
print('square root value is:',res)

             #    OR
import math
def sqe(n):
    m=math.sqrt(n)
    return m
res=sqe(81)
print('square root value is:',res)
