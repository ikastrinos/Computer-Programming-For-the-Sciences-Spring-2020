#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from defaults import *


# Example simulation

# In[3]:



for a in [0.5,1.2,2.3]:

    y=0
    t=0
    #a=2.3
    b=1
    c=2

    dt=0.0001

    maximum_time=20
    number_of_times_to_repeat=int(maximum_time/dt)

    y_list=[y]
    t_list=[t]
    for i in range(number_of_times_to_repeat):
        dy=(a+b*sin(c*t))*dt
        y=y+dy
        t=t+dt

        if i%100 == 0 :
            y_list.append(y)
            t_list.append(t)


    plot(t_list,y_list,label=f'a={a}')
    
xlabel('time [s]')
ylabel('position [m]')
legend()


# logistic growth
# 
# $$
# \frac{dy}{dt} = a y \cdot (1-y/K)
# $$
# 
# $$
# dy = a y \cdot (1-y/K) \cdot dt
# $$

# In[5]:



for a in [0.5,1.2,2.3]:

    # variables
    y=1
    t=0
    
    
    # parameters
    #a=2.3
    K=10
    

    dt=0.0001

    maximum_time=20
    number_of_times_to_repeat=int(maximum_time/dt)

    y_list=[y]
    t_list=[t]
    for i in range(number_of_times_to_repeat):
        dy=(a*y*(1-y/K))*dt
        y=y+dy
        t=t+dt

        if i%100 == 0 :
            y_list.append(y)
            t_list.append(t)


    plot(t_list,y_list,label=f'a={a}')
    
xlabel('time [s]')
ylabel('position [m]')
legend()


# In[ ]:




