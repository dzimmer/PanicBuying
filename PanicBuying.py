# -*- coding: utf-8 -*-
"""
Simulation of a panic buying cycle. 
(c) 2020 by Dirk Zimmer, free to use and modify for educational purposes
"""

#import plotting and numeric tools
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Time units and vectors ======================================================
day = 1.0 # per definition
week = 7*day 
duration = 20*week # timespan of simulation
time = np.arange(0.0, duration, day) # time vector
n = time.shape[0] #number of resulting simulation steps

#Parameters of the simulation ================================================
S_cap = 1 #capacity of stock in store. Is 1 per defintion


#seting up time series for time-variant variables ============================
S = np.zeros(n) #stock in supermarket
L = np.zeros(n) #local storage at homes
U = np.zeros(n) #daily usage of good
W = np.zeros(n) #wanted level of local storage
C = np.zeros(n) #daily consumption
D = np.zeros(n) #daily demand

#Set initial conditions ======================================================
S[0] = 0.6 #60% stocked
L[0] = 0.7 #slightly higher local storage


#perform integration over time ===============================================
for t in range(n-1):
        
    U[t] = 0.4/week #default usage rate
    #uncomment next line for panic inducing stimulus
    #U[t] = 0.4/week if t < 2.5*7 or t > 3.0*7 else 0.6/week
      
    W[t] = (S_cap/S[t])*U[t]*week
    D[t] = max(0.0,(W[t]-L[t])/week+U[t])
    C[t] = min(S[t],D[t])
            
    S[t+1] = S[t] - day*C[t] + day*(S_cap-S[t])/week 
    L[t+1] = L[t] + day*C[t] - day*U[t]

    
#plot simulation results over time ===========================================
matplotlib.rcParams.update({'font.size': 18})
fig, ax = plt.subplots()
ax.plot(time/week, S)
ax.plot(time/week, L)
ax.legend(['stock' ,'local storage'])
ax.set(xlabel='time [weeks]', ylabel='nominal capacity ')
plt.show()


#plot trajectory in state-space and vector field =============================
#fig, ax = plt.subplots()
#ax.plot(L,S)
#Sg,Lg = np.meshgrid(np.linspace(0.05,1,25),
#                    np.linspace(0.05,max(1.5,max(L*1.1)),35))
#U = U[0]
#Wg = (S_cap/Sg)*U*week
#Cg = np.clip((Wg-Lg)/week+U,a_min = 0, a_max = Sg)
#dS = -day*Cg + day*(S_cap-Sg)/week
#dL = -day*U + day*Cg
#ax.quiver(Lg,Sg,dL,dS)
#ax.grid()
#ax.set(xlabel='local storage', ylabel='stock')
#plt.show()


