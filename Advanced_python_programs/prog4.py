# Write a program to understand class variables.
class myclass:
    x=10
    @classmethod
    def modify(cls):
        cls.x+=1
m1=myclass()
m2=myclass()
print(m1.x, m2.x)

#Modify x value in class namespace.
myclass.modify()
print(m1.x,m2.x)

#Modify x value in instance namespce.
m1.x+=1
print(m1.x,m2.x)
