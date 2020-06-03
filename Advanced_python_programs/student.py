# Import some code from teacher class using Inheritance.
from teacher import*
class student(teacher):
    def setmarks(self,marks):
        self.marks=marks
    def getmarks(self):
        return self.marks
s=student()
s.setid(14)
s.setname('venkatadri')
s.setage('25 Years')
s.setheight('5.11 Inch')
s.setaddress('vindur,gudur,nellore,andrapradesh')
s.setmarks(965)
print('id no=',s.getid())
print('name=',s.getname())
print('age=',s.getage())
print('height=',s.getheight())
print('address=',s.getaddress())
print('marks=',s.getmarks())
