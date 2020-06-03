#3.reduce function.
# Create a lambda function to calculate cumilative product of elements of a list.
from functools import*
lst=[1,2,3,4]
res=reduce(lambda x,y:x*y ,lst)
print('cumilative product is:',res)
