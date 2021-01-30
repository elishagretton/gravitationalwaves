## -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.optimize import curve_fit
csv = 'assignment3.csv'
data =  pd.read_csv(csv)
freq = data["frequency"] # i added a row on top of my data and labelled the first column time and the second column frequency so i could easily refer to them.
time = data["time"]
x= []
y= []
x=list(time)
y=list(freq)
plt.scatter(x,y,5,label='simulated data')
plt.xlabel('time (s)')
plt.ylabel('frequency (Hz)')
plt.legend()
plt.title('Simulation of a gravitational wave chirp: data')
plt.savefig('freqvstime.png')
plt.show()
m = 1
N = len(x)
G = 6.674 *(10**-11)
c = 2.998*(10**8)
X = np.zeros((N,m))
def phi(t):
    return (-t)**(-3/8)
def beta(b):
    return (((5/(b*8*np.pi))**(8/5))*(c**3))/(5*G)
for i in range(N):
    X[i,0] = phi(x[i])
a = np.reshape(X,(1,N)) #X^T so (1,200) is new shape X is X (200,1) shape
A = np.dot(a,X) #X^T multipled by X
b = np.dot(a,y) #X^T dot y (frequencies)
par = np.linalg.solve(A,b) #gives beta, solves the normal equation
print("Beta is ", par)
print("Chirp mass is:",beta(par)) #finds M 
print("Chirp mass in terms of mass of the sun is: ", (beta(par))*(1.989 *10**30),"/1.989 x 10^30kg.")
y_est =(par)*X #beta times by outputs of function
plt.scatter(x,y,5, label='simulated data')
plt.plot(x,y_est,'r-', label = 'best-fit model')
plt.xlabel('time (s)')
plt.ylabel('frequency (Hz)')
plt.legend()
plt.title('Simulation of a gravitational wave chirp: data + model')
plt.savefig('bestfitmodel.png')
plt.show()
