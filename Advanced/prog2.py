# Create a student class with roll number,name,marks in three subjects and total marks.
class student:
    def __init__(self,r,n,m):
        self.rno=r
        self.name=n
        self.marks=m
    def display(self):
        print('rno=',self.rno)
        print('name=',self.name)
        print('marks=',self.marks)
        print('total marks=',sum(self.marks))
        print('average marks=',sum(self.marks)/len(self.marks))
s1=student(10,'venkey',[45,55,78])
s1.display()
