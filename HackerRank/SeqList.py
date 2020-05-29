"""Create a list seqlist of N empty sequences, where each sequence is indexed 
from 0 to N-1. the elements within each of the N sequenses also use 0-indexing"""

firstLN=list(map(int,input().split()))
N=firstLN[0]
Q=firstLN[1]

seqlist=[]
lastans=0

for i in range(0,N):
    q_number=list(map(int,input().split()))
    q_type=q_number[0]
    x=q_number[1]
    y=q_number[2]
    
    if q_type==1:
        seq=seqlist[(x*lastans)%N]
        seq.append(y)
    elif q_type==2:
        seq=seqlist[x*lastans)%N]
        lastans=seq[y%len(seq)]
        print(lastans)