"""Given a rectangular matrix of characters, add a border of asterisks(*) to it."""


def addBorder(picture):
    a=picture
    l=["*"*(len(a[0])+2)]
    i=0
    for i in a:
        l.append("*"+i+"*")
    l.append(l[0])
    return l
