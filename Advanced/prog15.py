# To create duck typing in polymorphism.
class duck:
    def talk(self):
        print('quack quack')
class dog:
    def talk(self):
        print('bow wow')
def call_talk(obj):
    obj.talk()
d=duck()
call_talk(d)
