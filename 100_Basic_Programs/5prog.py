# 5.Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class InputOutString():
    def __index__(self):
        self.s=''
    def getString(self):
        self.s=input('enter string:')
    def printString(self):
        print(self.s.upper())
obj=InputOutString()
obj.getString()
obj.printString()