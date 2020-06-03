class A(object):
    def method(self):
        print('A')
        super().method()
class B(object):
    def method(self):
        print('B')
        super().method()
class C(object):
    def method(self):
        print('C')
class X(A,B):
    def method(self):
        print('X')
        super().method()
class Y(B,C):
    def method(self):
        print('Y')
        super().method()
class P(X,Y,C):
    def method(self):
        print('p')
        super().method()
p=P()
p.method()
print(P.mro())
