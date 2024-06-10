import numpy as np 
import matplotlib.pylab as plt

P0 = float(input("Initial Value = "))
P = float(input("The amount of money you want to add at the end of each period = "))
r = float(input("Annual Interest Rate = "))
n = int(input("Number of periods within each year = "))
t = int(input("Number of years = "))

# The effect of rate on the initial value 
sum1 = P0
for _ in range(n*t):
    sum1 += (r/n)*(sum1)

# The effect of rate on the periodically added value 
sum2 = 0 
for i in range(n*t):
    sum2 += (1+r/n)**(i)

FV = sum1 + P*sum2

print(f"Final Value = {FV}")
