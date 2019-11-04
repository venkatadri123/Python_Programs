"""2.Write a program which can compute the factorial of a given numbers.
 The results should be printed in a comma-separated sequence on a
 single line."""


def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
res=fact(8)
print(res)