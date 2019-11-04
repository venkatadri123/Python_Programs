"""7.Write a program which takes 2 digits, X,Y as input and generates a 2-
dimensional array. The element value in the i-th row and j-th column
of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡Y-1.
"""

x=input('enter x,y values:')
dim=[int(i) for i in x.split(',')]
row=dim[0]
col=dim[1]
list=[[0 for c in range(col)] for r in range(row)]
for c in range(col):
    for r in range(row):
        list[r][c]=r*c

print(list)