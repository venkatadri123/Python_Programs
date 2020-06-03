# Accept day number and display day name.
import sys
n=int(input('enter a number:'))
if n<1 and n>7:
    print('please enter no betweet 1-7 only',n)
    sys.exit()
elif n==1:
    print('sunday')
elif n==2:
    print('monday')
elif n==3:
    print('tuesday')
elif n==4:
    print('wednesday')
elif n==5:
    print('thursday')
elif n==6:
    print('friday')
else:
    print('saturday')
sys.exit()
