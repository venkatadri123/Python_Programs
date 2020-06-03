"""Given a string, find out if its characters can be rearranged to form a palindrome."""


def palindromeRearranging(inputString):
    a=set()
    for i in inputString:
        if i in a:
            a.remove(i)
        else:
            a.add(i)
    return len(a)<=1
