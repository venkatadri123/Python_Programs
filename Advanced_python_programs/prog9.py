# Inner class demo using perameterized constructor.
class student:
    def __init__(self,r,n):
        self.rno=r
        self.name=n
    def display(self):
        print('rno=%d' %self.rno)
        print('name=%s' %self.name)
    class dob:
        def __init__(self,d,m,y):
            self.dd=d
            self.mm=m
            self.yy=y
        def display(self):
            print("dob=",self.dd,self.mm,self.yy)
w=int(input('enter roll no:'))
x=input('enter name:')
s=student(w,x)
s.display()
e=int(input('enter date:'))
g=int(input('enter month:'))
h=int(input('enter year:'))
f=s.dob(e,g,h)
f.display()
