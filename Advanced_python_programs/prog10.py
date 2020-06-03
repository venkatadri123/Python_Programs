# Example of Abstraction.
class bank:
    def __init__(self,a,n,b,l):
        self.accno=a
        self.name=n
        self.bal=b
        self.__loan=l # providing sequrity using __ (double undersqoor)
    def display_to_clerk(self):
        print('accno=',self.accno)
        print('name=',self.name)
        print('balencee=',self.bal)
w=int(input('enter acc no:'))
x=input('enter name:')
y=float(input('enter acc bal:'))
z=float(input('enter loan amount:'))
b=bank(w,x,y,z)
b.display_to_clerk()

print(b._bank__loan) # breaking Abstraction (name mangling)

