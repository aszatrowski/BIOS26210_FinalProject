#!/usr/bin/env python
# coding: utf-8

# In[31]:


### TESTING
import numpy as np #package for work with arrays and matrices
import matplotlib.pyplot as plt #package with plotting capabilities

dt = 1 #set the time step
Tmax = 20000 #set the maximum time duration
ts = np.arange(0,Tmax, dt)
Niter = int(np.ceil(Tmax/dt)) #determine the number of iterations
x = np.zeros(Niter) #preallocate the solution array
x[0] = 240 #set the initial value


A = 270
B1 = 2441
B2 = 90.02
T1 = 19.6
T2 = 200
DImin = 53.5
n = 1          #make it 1 or 2 maybe play around with other values later on
ts = 200

for i in range(Niter-1):
    x[i+1] = A - B1*np.exp((x[i]-n*ts)/T1) - B2*np.exp((x[i]-n*ts)/T2)
    if n*ts - x[i+1] <= DImin:
        x[i+1] = -1*(DImin - n*ts)
        
#     if x[i+1] <= DImin:
#         x[i+1] = DImin

# for i in range(Niter-1):
#     plt.scatter(ts, x[i+1])
plt.ylim(-100, 400) 


plt.plot(x)


# In[27]:


### MODEL TESTING
def func(ts, X0):
    x[0] = X0
    for i in range(Niter-1):
        x[i+1] = A - B1*np.exp((x[i]-n*ts)/T1) - B2*np.exp((x[i]-n*ts)/T2)
        if n*ts - x[i+1] <= DImin:
            x[i+1] = (-1*DImin) + n*ts

    #     if x[i+1] <= DImin:
    #         x[i+1] = DImin

    # for i in range(Niter-1):
    #     plt.scatter(ts, x[i+1])
    plt.ylim(-100, 400) 


    plt.plot(x)
    plt.title("APD v Time ts="+ str(ts)+ " Xo="+ str(X0) )
    plt.xlabel("Time")
    plt.ylabel("APD")
    plt.figure()

func(0, 240)
func(10, 240)
func(20, 240)
func(50, 240)
func(80, 240)
func(160, 240)
func(220, 240)
func(250, 240)
func(300, 240)


# In[28]:


func(0, 270)
func(10, 270)
func(20, 270)
func(50, 270)
func(80, 270)
func(160, 270)
func(220, 270)
func(250, 270)
func(300, 270)

