# Creating Abstract class.
from abc import ABC, abstractmethod
class myclass(ABC):
    def display(self):
        print('iam concrete method')
    @abstractmethod
    def cal(self,x):
        pass
class sub1(myclass):
    def cal(self,x):
        print('square value=',x*x)
import math
class sub2(myclass):
    def cal(self,x):
        print('square root value=',math.sqrt(x))

s1=sub1()
s1.display()
s1.cal(16)
s2=sub2()
s2.display()
s2.cal(16)
