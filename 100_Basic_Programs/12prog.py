"""12.Write a program, which will find all such numbers between 1000 and
3000 (both included) such that each digit of the number is an even
number.
The numbers obtained should be printed in a comma-separated sequence
on a single line.
"""
l=['0','2','4','6','8']
for i in range(1000,3001):
    for p in str(i):
        if p not in l:
            break
    else:
        print(i)
