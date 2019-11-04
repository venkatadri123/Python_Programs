"""18.A website requires the users to input username and password to
register. Write a program to check the validity of password input by
users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and
will check them according to the above criteria. Passwords t"""


import re
value=[]
x=[x for x in input("enter password:").split(',')]
for i in x:
    if len(i)<6 and len(i)>20:
        continue
    else:
        pass
    if not re.search("[0-9]",i):
        continue
    elif not re.search("[a-z]",i):
        continue
    elif not re.search("[A-Z]",i):
        continue
    elif not re.search("[@#$]",i):
        continue
    else:
        value.append(i)

print(value)