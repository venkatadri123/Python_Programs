"""Ticket numbers usually consist of an even number of digits. A ticket number is
considered lucky if the sum of the first half of the digits is equal to the sum of the second half."""


def isLucky(n):
    a=list(str(n))
    b=len(a)
    c=int(b/2)
    l=[0,0]
    # for i in range(c):
    #     l[0]+=int(a[i])
    # for j in range(c,b):
    #     l[1]+=int(a[j])
    # if l[0]==l[1]:
    #     return True
    # else:
    #     return False

    for i in range(b):
        if i<c:
            l[0]+=int(a[i])
        else:
            l[1]+=int(a[i])
    return l[0]==l[1]