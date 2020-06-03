"""Given an array of integers, find the maximal absolute difference between any two of its adjacent elements."""


def arrayMaximalAdjacentDifference(inputArray):
    a=inputArray
    m=0
    for i in range(len(a)-1):
            t=abs(a[i]-a[i+1])
            if m<t:
                m=t
    return m