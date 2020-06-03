# 2.Map functin.
# Create a lambda function to calculate square of all elements in a list.
lst=[1,2,3,4]
obj=map(lambda x: x*x ,lst)
res=list(obj)
print('square value=',res)
