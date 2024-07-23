import numpy as np 
from itertools import groupby

def mdt_calc(seq, element):
    seq2 = [seq[0]]
    for i in range(1,len(seq)):
        if seq[i] != seq2[-1]:
            seq2 = seq2 + [seq[i]]
    
    count_dups = [sum(1 for _ in group) for _, group in groupby(seq)]
    idx = np.where(np.array(seq2)==element)
    dt = np.array(count_dups)[idx]
    mdt = np.mean(dt)

    return(mdt)

seq = [1,1,1,1,1,1, 2,2,2,2, 3,3,3, 1,1,1,1, 2,2, 3, 1,1,1, 4,4, 1,1, 3,3,3, 2]
element = 3
mdt = mdt_calc(seq, element)
print(f'mdt({element}) = {mdt}')