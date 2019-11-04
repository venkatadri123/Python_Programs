"""11.Write a program which accepts a sequence of comma separated 4 digit
binary numbers as its input and then check whether they are divisible
by 5 or not. The numbers that are divisible by 5 are to be printed in
a comma separated sequence.
"""

v=[]
item=[x for x in input('enter:').split(',')]
for p in item:
    intp=int(p,2)
    if intp%5==0:
        v.append(p)
print(v)
