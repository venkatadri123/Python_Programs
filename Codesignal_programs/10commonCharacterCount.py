"""Given two strings, find the number of common characters between them."""


def commonCharacterCount(s1, s2):
    c = 0
    for i in s1:
        if i in s2:
            s2 = s2.replace(i, "", 1)
            c += 1
    return c
