#.Given a sequence of integers as an array, determine whether it is possible to obtain a strictly
# increasing sequence by removing no more than one element from the array.

# Note: sequence a0, a1, ..., an is considered to be a strictly increasing
# if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.


def almostIncreasingSequence(sequence):
    fail = 0
    inc = 0

    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            fail += 1

    for i in range(len(sequence) - 2):
        if sequence[i] >= sequence[i + 2]:
            inc += 1

    return (fail < 2) and (inc < 2)
