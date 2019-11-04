# Write a python program to accept values from keyboard and display its transpose.
from numpy import*
r,c=[int(i) for i in input('enter rows,columns:').split()]
arr=zeros((r,c),dtype=int)
print('enter the matrix:')
for i in range(r):
    arr[i]=[int(x) for x in input().split()]
m=matrix(arr)
print('transpose:')
print(m.transpose())
