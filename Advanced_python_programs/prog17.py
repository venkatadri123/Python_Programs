# Example for Method overloading.
class A:
    def display(self):
        print('class A')
class B(A):
    def display(self):
        print('class B')
b=B()
b.display
