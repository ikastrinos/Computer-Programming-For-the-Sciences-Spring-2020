#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from defaults import *


# https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology#The_SIR_model_without_vital_dynamics
# 
# 
# $$
# \frac{dS}{dt} = -\beta \frac{S I}{N} - \mu S
# $$
# 
# $$
# \frac{dI}{dt} = +\beta \frac{S I}{N} - \gamma I -\mu I
# $$
# 
# $$
# \frac{dR}{dt} =+ \gamma I -\mu R
# $$
# 

# 1. what are the variables:
#    * S
#    * I
#    * R
# 2. what are the parameters?
#    * $\beta$
#    * $\gamma$
#    * $\mu$

# In[11]:


# initial values of variables
t=0
S=100
I=1
R=0

# parameters
β=1
γ=0.1
μ=0


# deal with time
dt=0.0001
maximum_time=60
number_of_times_to_repeat=int(maximum_time/dt)

# initial lists for variables
S_list=[S]
I_list=[I]
R_list=[R]
t_list=[t]
for i in range(number_of_times_to_repeat):
    
    # how the variables change
    N=S+I+R
    
    dS=(-β*S*I/N -μ*S)*dt
    dI=(β*S*I/N -γ*I -μ*I)*dt
    dR=(γ*I -μ*R)*dt
    
    # update the variable values, and time
    S=S+dS
    I=I+dI
    R=R+dR
    t=t+dt
    
    # store the results in a list
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)
    t_list.append(t)
    


# In[12]:


plot(t_list,I_list)


# In[ ]:




