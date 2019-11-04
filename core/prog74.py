# 1.Filter functin.
# Create a lambda that returns evens from a list.
lst=[1,5,6,4,2,16,14,17]
obj=filter(lambda x:x%2==0,lst)
print(list(obj))
