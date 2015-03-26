# Assignment-6Assignment 6
1. Radioactivity Decay:
We simulates the radioactive decay of 10000 atoms of 213Bi by dividing time into slices of length dt = 1 s each.
Keeping the tract of the number of atoms of ach of the four isotopes at all times for 20000 seconds, 
we then plot a single graph that shows the four isotope numbers 213Bi, 209Tl, 209Pb, and 209Bi atoms as a function of time on the same axes. (Program 6_1.py)
 
2.   Monte Carlo Integration
We computes the value of the integral ∫_0^1▒x^(-1/2)/(e^x+1) dx  using Monte Carlo integration with weight,w=x^(-1/2). 
The probability distributions p(x) is calculated as p=1/(2√x)  .Then the transformation formula is derived 
which generates random numbers between 0 and 1 from this distribution, which is   x=z^2. 
We use a sample N = 1000000 random points and evaluated the integral. The integral I is calculated with a value of 0.839.

The output of the program 6_2b.py 
Integral, I = 0.839
