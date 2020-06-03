#To find sum ofgiven digits.
n=int(input("Enter a number:"))
total=0
while(n>0):
    digit=n%10
    total=total+digit
    n=int(n/10)
print("The total sum of digits is:",total)