# Wrte employee class with accessor and mulator methods.
class emp:
    def setid(self,id):
        self.id=id
    def getid(self):
        return self.id
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    def setsal(self,sal):
        self.sal=sal
    def getsal(self):
        return self.sal
e=emp()
e.setid(int(input('enter id no:')))
e.setname(input('enter name'))
e.setsal(float(input('enter salory:')))
print('id=',e.getid())
print('name=',e.getname())
print('salory=',e.getsal())
