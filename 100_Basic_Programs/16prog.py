"""16.Use a list comprehension to square each odd number in a list. The list
is input by a sequence of comma-separated numbers."""
l=input("enter:")
lst=[x for x in l.split(',') if int(x)%2!=0]
print(lst)
for i in lst:
    print(int(i)*int(i),end=',')
