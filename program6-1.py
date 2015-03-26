#This program computes the value of the given integral (x^(-1/2)/(exp(x)+1))dx
# with limits (0,1)using Monte Carlo integration.
# Sample N=1000000 random points are used. 

from math import exp
from random import random

def f(x):
    return x**(-1/2)/(exp(x)+1)
def w(x):
    return x**(-1/2)

N = 1000000
sum = 0.0

for i in range(N):
    x = (random())**2.0
    sum += f(x)/w(x)
    I = 2*sum/N
    
print("Integral, I = {0:.4f}".format(I)) 


