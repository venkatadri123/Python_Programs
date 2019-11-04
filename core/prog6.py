# write a python program to find sum of all given numbers.
lst=[float(i) for i in input('enter values:').split(',')]
sum=0
for i in lst:
    sum+=i
print('sum=',sum)    
