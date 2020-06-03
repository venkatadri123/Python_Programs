#. Given an array of integers, find the pair of adjacent elements that has the
# largest product and return that product.


def adjacentElementsProduct(inputArray):
    a = inputArray
    lenth = len(a)
    sum = []
    for i in range(lenth-1):
        sum.append(a[i]*a[i+1])
    return max(sum)
