#To reverse a number.
n=int(input('enter a number:'))
while n!=0:
    digit=n%10
    print(digit,end="")
    n=int(n/10)