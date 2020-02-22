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


# In[14]:


# parameters

k=20
m=1

# initial values

x=0
v=3
t=0

# time parameters
dt=0.001
max_time=100
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





# In[17]:


subplot(2,1,1)
plot(t,x)
ylabel('position')

subplot(2,1,2)
plot(t,v,'r-')
ylabel('velocity')
xlabel('time')


# In[18]:


# parameters

k=20
m=1

# initial values

variables=array([0,3])
# x=0
# v=3
t=0

# time parameters
dt=0.001
max_time=100
number_of_steps=int(max_time/dt)

S=Storage()

for i in range(number_of_steps):
    
    # changes
    x,v=variables
    change_in_variables=array([v,-k*x/m])
#     dx=(v)*dt
#     dv=(-k*x/m)*dt
    
    #update values
    t=t+dt
    variables=variables+change_in_variables*dt
#     x=x+dx
#     v=v+dv
    
    #saving the values
    x,v=variables
    S+=t,x,v
    
    
t,x,v=S.arrays()    





# In[19]:


subplot(2,1,1)
plot(t,x)
ylabel('position')

subplot(2,1,2)
plot(t,v,'r-')
ylabel('velocity')
xlabel('time')


# In[22]:


pip install "git+git://github.com/bblais/pyndamics" --upgrade


# In[23]:


from pyndamics import Simulation


# In[28]:


sim=Simulation()

sim.add(" x' = v ",0,plot=True)
sim.add(" v' = -k*x/m ",3,plot=True)

sim.params(k=2,m=1)
sim.run(100)


# # infinite integers

# In[29]:


def factorial(N):
    
    value=1
    for i in range(1,N+1):
        value=value*i
        
    return value


# In[30]:


factorial(5)


# In[31]:


factorial(70)


# In[32]:


factorial(700)


# In[33]:


factorial(7000)


# In[34]:


def factorial(N):
    
    value=1.0
    for i in range(1,N+1):
        value=value*i
        
    return value


# In[45]:


factorial(170)


# In[57]:


def beta(h,N,θ):
    return factorial(N+1)/factorial(h)/factorial(N-h)*θ**h*(1-θ)**(N-h)


# In[58]:


beta(3,12,0.5)


# In[61]:


θ=linspace(0,1,100)
dθ=θ[1]-θ[0]
p=beta(3,12,θ)
plot(θ,p)
title(sum(p*dθ))


# In[ ]:




