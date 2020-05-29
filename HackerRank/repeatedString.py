"""Lilah has a string, , of lowercase English letters that she repeated infinitely many times.

Given an integer, , find and print the number of letter a's in the first  letters of Lilah's infinite string.

For example, if the string  and , the substring we consider is , the first  characters of her infinite string. There are  occurrences of a in the substring."""

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    len_str=len(s)
    num_strs=n//len_str
    remainder=n%len_str
    count1=0
    count2=0
    for i in range(len_str):
        if s[i]=='a':
            count1+=1
        if s[i]=='a' and i<remainder:
            count2+=1
    total=count1*num_strs+count2
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
