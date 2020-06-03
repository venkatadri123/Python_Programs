"""Call two arms equally strong if the heaviest weights they each are able to lift are equal.

Call two people equally strong if their strongest arms are equally strong
(the strongest arm can be both the right and the left), and so are their weakest arms.

Given your and your friend's arms' lifting capabilities find out if you two are equally strong."""


def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    a = yourLeft
    b = yourRight
    c = friendsLeft
    d = friendsRight
    if a == c and d == b or a == d and c == b:
        return True
    else:
        return False
