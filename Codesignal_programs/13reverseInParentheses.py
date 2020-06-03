"""Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s."""


def reverseInParentheses(inputString):
    l=inputString
    for i in range(len(l)):
        if l[i]=='(':
            a=i
        if l[i]==')':
            z=i
            return reverseInParentheses(l[:a]+(l[a+1:z][::-1]+l[z+1:]))
    return l
