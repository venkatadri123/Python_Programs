# Write a function that calculates power value of a number.

#Power value of a number.
def power_value(m,n):
    a=m**n
    print('power value is:',a)
power_value(5,2)

#      OR

def power_value(m,n):
    a=m**n
    return a
res=power_value(5,2)
print('power value is:',res)
