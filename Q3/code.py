import numpy as np 
from itertools import groupby
import pandas as pd 

def mdt_calc(seq):
    dfmdt = pd.DataFrame([])
    for element in np.unique(seq):
        seq2 = [seq[0]]
        for i in range(1,len(seq)):
            if seq[i] != seq2[-1]:
                seq2 = seq2 + [seq[i]]
    
        count_dups = [sum(1 for _ in group) for _, group in groupby(seq)]
        idx = np.where(np.array(seq2)==element)
        dt = np.array(count_dups)[idx]
        mdt = np.mean(dt)

        tmpdf = pd.DataFrame([])
        tmpdf['Element'] = [element]
        tmpdf['MDT'] = [mdt]
        
        dfmdt = pd.concat((dfmdt, tmpdf), ignore_index=True)

    return(dfmdt)

seq = [1,1,1,1,1,1, 2,2,2,2, 3,3,3, 1,1,1,1, 2,2, 3, 1,1,1, 4,4, 1,1, 3,3,3, 2]
mdt = mdt_calc(seq)
print(mdt)