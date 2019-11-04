# Creating our own Exception.
class MyException(Exception):
    def __init__(self,str):
        self.str=str
def check(dict):
    for k,v in dict.items():
        print('%-15s %.2f' %(k,v))
        if v<2000.00:
            raise MyException('balence amount is less')
bank={'raju':35600,'venkey':25641,'hari':1230,'suri':2564}
try:
    check(bank)
except MyException as m:
    print(m)
        
