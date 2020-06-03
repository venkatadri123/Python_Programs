# add corresponding elements of two lists and store then in another list.
a=[1,2,3,4,5,6]
b=[4,5,6,7,8,9]
lst=[]
for i in range(len(a)):
    lst.append(a[i]+b[i])
print(lst)

# To convert into List Comprehension.

lst=[a[i]+b[i] for i in range(len(a))]
print(lst)
