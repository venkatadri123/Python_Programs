"""Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. It is always possible to win the game.

For each game, Emma will get an array of clouds numbered  if they are safe or  if they must be avoided. For example,  indexed from . The number on each cloud is its index in the list so she must avoid the clouds at indexes  and . She could follow the following two paths:  or . The first path takes  jumps while the second takes ."""

def jumpingOnClouds(c):
    clear_jumps = lambda n: len(n) // 2
    thunder = [n for n, cloud in enumerate(c) if cloud == 1]
    
    if len(thunder) == 0:
        return clear_jumps(c)
    
    last = -1
    jumps = 0
    section = []
    
    for t in thunder:
        section = c[last + 1:t]
        last = t
        jumps += clear_jumps(section) + 1

    section = c[last + 1:]
    jumps += clear_jumps(section)
        
    return jumps
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
