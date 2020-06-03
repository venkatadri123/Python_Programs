# Inner class demo.
class student:
    def __init__(self):
        self.rno=125
        self.name='venkatadri'
    def display(self):
        print('rno=%d' %self.rno)
        print('name=%s' %self.name)
    class dob:
        def __init__(self):
            self.dd=26
            self.mm=12
            self.yy=1994
        def display(self):
            print("dob=",self.dd,self.mm,self.yy)

s=student()
s.display()

f=s.dob()
f.display()
