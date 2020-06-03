# Write a static method to calculate square root value of a number.
class squ_root:
    @staticmethod
    def display(x):
        res=x**0.5
        return res

x=int(input('enter no:'))
res=squ_root.display(x)
print('result=',res)
