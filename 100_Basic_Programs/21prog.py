"""21.A robot moves in a plane starting from the original point (0,0). The
robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The
trace of robot movement is shown as the following:
"""

from math import *
l=[0,0]
while True:
    n=input('enter:')
    if not n:
        break
    move=n.split(" ")
    dir=move[0]
    step=int(move[1])
    if dir=="up":
        l[0]+=step
    elif dir=="down":
        l[0]-=step
    elif dir=="left":
        l[1]+=step
    elif dir=="right":
        l[1]-=step
    else:
        pass
print(int(round(sqrt(l[1]**2+l[0]**2))))
