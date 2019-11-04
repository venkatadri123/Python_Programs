# Create an employee class with Id,name,salory and address, display these details along with 10% increment in salory.
class employee:
     def __init__(self,i,n,s,a):
         self.id=i
         self.name=n
         self.salory=s
         self.address=a
     def display(self):
         print('id no=',self.id)
         print('name=',self.name)
         print('salory=',self.salory)
         print('address=',self.address)
         e=self.salory/10
         print('incremental value:',self.salory+e)
w=int(input('enter id:'))
x=input('enter name:')
y=float(input('enter salory:'))
z=[str(p) for p in input('enter address:').split()]
s1=employee(w,x,y,z)
s1.display()
         
