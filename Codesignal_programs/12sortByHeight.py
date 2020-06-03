"""Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to
rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!"""


def sortByHeight(a):
    l=len(a)
    l1=[]
    l2=[]
    for i in range(l):
        if a[i]==-1:
            l1.append(i)
        else:
            l2.append(a[i])
    l2.sort()
    for j in range(len(l1)):
        l2.insert(l1[j],-1)
    return l2