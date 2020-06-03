# Creating log files.
import logging
logging.basicConfig(filename="mylog.txt", level=logging.ERROR)

try:
    a=int(input('enter a vavue:'))
    b=int(input('enter b value:'))
    c=a/b
except Exception as e:
    
    logging.exception(e)
else:
    print('result=',c)
