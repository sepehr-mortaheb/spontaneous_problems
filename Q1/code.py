import numpy as np 
import matplotlib.pylab as plt

N = 25

def xy_finder(N):
    if np.remainder(N, 2) == 0: # if N is even 
        xList = np.array(range(2, N, 2)) # also x should be even 
    else: # if N is odd
        xList = np.array(range(1, N, 2)) # also x should be odd
    diff = []
    for x in list(xList):
        diff = diff + [np.abs(N/2 - 1.5*x)]
        
    idx_min = np.argmin(np.array(diff))
    x = xList[idx_min]
    y = int((N - x) / 2)

    return x, y, xList, diff

x, y, xList, diff = xy_finder(N) 
print(f"x = {x}, y = {y}")
plt.plot(xList, diff,marker="o")
plt.grid(True)
plt.xlabel('x', size=15)
plt.ylabel('|y - x|', size=15)
plt.show()
