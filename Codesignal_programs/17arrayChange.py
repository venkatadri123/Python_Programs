"""You are given an array of integers. On each move you are allowed to increase exactly
one of its element by one. Find the minimal number of moves required to obtain a strictly
increasing sequence from the input."""


def arrayChange(inputArray):
    x = inputArray
    y = 0
    for i in range(len(x) - 1):
        a = x[i]
        b = x[i + 1]
        if a >= b:
            y += a + 1 - b
            x[i + 1] = a + 1
    return y
