"""17.Write a program that computes the net amount of a bank account based a
transaction log from console input. The transaction log format is
shown as following:
D 100
W 200
"""

net=0
while True:
    s=input('enter:')
    if not s:
        break
    val=s.split(' ')
    oper=val[0]
    amount=int(val[1])
    if oper=="d":
        net+=amount
    elif oper=="w":
        net-=amount
    else:
        pass
print(net)