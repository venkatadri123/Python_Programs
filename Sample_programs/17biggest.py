# Biggest among three numbers
a=int(input('enter a value:'))
b=int(input('enter b value:'))
c=int(input('enter c value:'))
if (a>b) and (a>c):
    largest=a
elif(b>a) and (b>c):
    largest=b
else:
    largest=c
print('largest number is:',largest)