"""15.Write a program that computes the value of a+aa+aaa+aaaa with a given
digit as the value of a.
"""

a=input('enter:')
l=[]
for i in range(1,a+1):
    s=a*i
    l.append(s)
print("+".join(l))

# x='a'
# t=[]
# for i in range(1,5):
#     s=x*i
#     t.append(s)
# print("+".join(t))