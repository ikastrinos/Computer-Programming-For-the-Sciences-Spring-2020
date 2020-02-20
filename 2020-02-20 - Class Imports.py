#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


x=randn(1000)
y=randn(1000)


# In[4]:


subplot(2,1,1)
plot(x,y,'ro')

subplot(2,1,2)
plot(x,y,'bo')


# In[5]:


# subplot(number of rows of the plot, number of cols in the plot, which subplot)

subplot(2,2,1)
plot(x,y,'ro')

subplot(2,4,3)
plot(x,y,'bo')
title('here')

subplot(2,1,2)
plot(x,y,'go')
title('there')


# In[6]:


subplot(2,2,1)
plot(x,y,'ro')

subplot(2,2,2)
plot(x,y,'bo')

subplot(2,1,1)
plot(x,y,'go')


# ## example with storage

# In[7]:


# parameters

k=2
m=1

# initial values

x=0
v=3
t=0

# time parameters
dt=0.001
max_time=10
number_of_steps=int(max_time/dt)

t_list=[]
x_list=[]
v_list=[]

for i in range(number_of_steps):
    
    # changes
    dx=(v)*dt
    dv=(-k*x/m)*dt
    
    #update values
    t=t+dt
    x=x+dx
    v=v+dv
    
    #saving the values
    t_list.append(t)
    x_list.append(x)
    v_list.append(v)
    
    
t=array(t_list)
x=array(x_list)
v=array(v_list)
    





# In[8]:


subplot(2,1,1)
plot(t,x)
ylabel('position')

subplot(2,1,2)
plot(t,v)

plot(t,2*v)
ylabel('velocity')
xlabel('time')


# In[9]:


# parameters

k=2
m=1

# initial values

x=0
v=3
t=0

# time parameters
dt=0.001
max_time=10
number_of_steps=int(max_time/dt)

S=Storage()

for i in range(number_of_steps):
    
    # changes
    dx=(v)*dt
    dv=(-k*x/m)*dt
    
    #update values
    t=t+dt
    x=x+dx
    v=v+dv
    
    #saving the values
    S+=t,x,v
    
    
t,x,v=S.arrays()    





# In[11]:


subplot(2,1,1)
plot(t,x)
ylabel('position')

subplot(2,1,2)
plot(t,v)

plot(t,2*v)
ylabel('velocity')
xlabel('time')


# In[ ]:




