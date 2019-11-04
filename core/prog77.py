# To multiply two matrices.
from numpy import*
a=array([[1,2,3],[4,5,6],[7,8,9]])
b=array([[1,2,3],[4,5,6],[7,8,9]])
m1=matrix(a)
m2=matrix(b)
m3=m1+m2
print('sum of matrix=',m3)
m3=m1-m2
print('sub os matrix=',m3)
m3=m1*m2
print('product of matrix=',m3)
m3=m1/m3
print('div of matrix=',m3)
