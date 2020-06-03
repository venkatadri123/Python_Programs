# Write a List comprehension to retrive common elements from two lists.
a=[10,20,30,40,50,60,70,80]
b=[15,40,20,10,25,26,24,30]
lst=[]
for i in a:
    if i in b:
        lst.append(i)
print(lst)

# To convert into List Comprehension.

lst=[i for i in a if i in b]
print(lst)
