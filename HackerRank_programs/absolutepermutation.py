"""We define P to be a permutation of the first n natural numbers in the range
[1,n]. Let pos[i] denote the value at position i in permutation P using 1-based indexing.

P is considered to be an absolute permutation if |pos[i]-i| = K holds true for every i."""

import math
import os
import random
import re
import sys


# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    solution = []
    s = set(range(1, n + 1))

    for pos in xrange(1, n + 1):
        if pos - k in s:
            solution.append(pos - k)
            s.remove(pos - k)
        elif pos + k in s:
            solution.append(pos + k)
            s.remove(pos + k)
        else:
            return [-1]

    return solution


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        nk = raw_input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()