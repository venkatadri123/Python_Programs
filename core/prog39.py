#exception handling
try:
    n=int(input('enter a number:'))
    assert n>=10 and n<=20, 'wrong input'
    print('u entered:',n)
except assersonerror:
    print('enter number between 10-20 only:')
