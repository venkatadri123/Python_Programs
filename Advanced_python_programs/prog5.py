# Write a program to calculate the no.of objects are created for a class.
class sample:
    x=0
    def __init__(self):
        sample.x+=1

    @staticmethod
    def display():
        print('no.of objects are created:',sample.x)
s1=sample()
s2=sample()
s3=sample()
sample.display()
