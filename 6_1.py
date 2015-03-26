# This program simlulates the radioactive decay of 10000 213Bi atoms.
# It gives the output plot 4 numbers of 213Bi,209Tl,209Pb, and 209Bi atoms
# as a function of time for 20000 seconds.


from random import random
from numpy import arange
from pylab import plot,xlabel,ylabel,legend,show 

NBi1 = 10000                        # Initial number of 213Bi bismuth atoms
NTl = 0                             # Initial number of 209Tl thallium atoms
NPb = 0                             # Initial number of 209Pb lead atoms
NBi2 = 0                            # Initial number of 209Bi bismuth atoms
tau_Bi = 46.0*60                    # Half-life of 213Bi in seconds
tau_Tl = 2.2*60                     # Half-life of 209Tl in seconds
tau_Pb = 3.3*60                     # Half-life of 209Pb in seconds
h = 1.0                             # Size of time-step  in seconds

p_Bi = 1.0 - 2.0**(-h/tau_Bi)       # Probability of decay of 213Bi in one step
p_Tl = 1.0 - 2.0**(-h/tau_Tl)       # Probability of decay of 209Tl in one step
p_Pb = 1.0 - 2.0**(-h/tau_Pb)       # Probability of decay of 209Pb in one step
tmax = 20000                        # Total time in seconds

# Lists of plot points

tpoints = arange(0.0, tmax, h)
Bi1points = []
Bi2points = []
Tlpoints = []
Pbpoints = []

#Main loop

for t in tpoints:
  Bi1points.append(NBi1)
  Bi2points.append(NBi2)
  Tlpoints.append(NTl)
  Pbpoints.append(NPb)

#Calculating te number of atoms that decay

  decay_Pb = 0
  for i in range(NPb):              # Calculating the number of 209Pb atoms that decay
    if random() < p_Pb:             
      decay_Pb += 1
  NPb -= decay_Pb                   # Subtracting decayed atoms from 209Pb
  NBi2 += decay_Pb                  # Adding decayed atoms to 209Bi
  decay_Tl=0

  for j in range(NTl):              # Calculating the number of 209Tl atoms that decay 
    if random() < p_Tl:
      decay_Tl += 1
  NTl -= decay_Tl                   # Subtracting decayed atoms from 209Tl
  NPb += decay_Tl                   # Adding decayed atoms 209Pb
  decay_Bi_path1 = 0                # Number of atoms which decay to 209Pb(route 1)
  decay_Bi_path2 = 0                # Number of atoms which decay to 209Tl(route 2)

  for k in range(NBi1):
    if random() < p_Bi:             # Probability of 213Bi decaying 
      if random()-0.9791 < 1e-6:    
        decay_Bi_path1 += 1         # Probabilty of 0.9791 within 1e-6 precision of 213Bi decaying to 209Pb
      else:                         
        decay_Bi_path2 += 1         # Otherwise decaying to 209Tl with probability of 0.0209

  NBi1 -= decay_Bi_path1            # Subtracting number of Bi decaying to Pb
  NBi2 -= decay_Bi_path2            # ubtracting number of Bi decaying to Tl
  NPb += decay_Bi_path1             # Adding number of Bi decaying to Pb
  NTl += decay_Bi_path2             # Adding number of Bi decaying to Tl


#Plotting the number of atoms of 4 isotopes as a function of time

plot(tpoints,Bi1points,label = "213Bi")
plot(tpoints,Tlpoints,label = "209Tl")
plot(tpoints,Pbpoints,label = "209Pb")
plot(tpoints,Bi2points,label = "209Bi")
xlabel("Time(s)",fontsize=26)
ylabel("Number of Atoms(N)",fontsize=26)
legend(loc='upper right')
show()
