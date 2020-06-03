"""Two arrays are called similar if one can be obtained from another by swapping
at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar."""


def areSimilar(a, b):
    s = sorted(a) == sorted(b)
    lst=[]
    for i in range(len(a)):
        if a[i]==b[i]:
            pass
        else:
            lst.append(i)
    return len(lst)<=2  and s
    # d = [i for i in range(len(a)) if a[i] != b[i]]
    # return len(d) <= 2 and s
