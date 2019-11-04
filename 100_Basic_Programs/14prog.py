"""14.Write a program that accepts a sentence and calculate the number of
upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
"""

x=input('enter:')
d={'Upper':0,'Lower':0}
for i in x:
    if i.isupper():
        d['Upper']+=1
    elif i.islower():
        d['Lower']+=1
    else:
        pass
print('Uppercase letters:',d['Upper'])
print('Lowercase letters:',d['Lower'])