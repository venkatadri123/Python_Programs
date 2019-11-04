# Write a list comprehension to get even numbers upto 10.
lst=[]
for i in range(2,11):
    if i%2==0:
        lst.append(i)
print(lst)

# to convert into List comprehention.
lst=[i for i in range(2,11) if i%2==0]
print(lst)
