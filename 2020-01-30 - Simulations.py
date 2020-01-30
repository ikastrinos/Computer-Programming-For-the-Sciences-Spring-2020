#!/usr/bin/env python
# coding: utf-8

# In[26]:


get_ipython().run_line_magic('pylab', 'inline')


# this text is in markdown syntax.
# 
# 
# * Differential equations
# 
# $$
# \frac{dn}{dt} = r\cdot n
# $$
# 
# Equations are given in LaTeX format.
# 
# 

# In[1]:


print("here")
No=2000000

n=No
t=0
r=0.1
dt=0.0001

# this a comment for later
maximum_time=20
number_of_times_to_repeat=int(maximum_time/dt)
for i in range(number_of_times_to_repeat):
#     print(i)
#     print("this")
    dn=r*n*dt
    n=n+dn
    t=t+dt
#     print(t,n)
    
print("there")
print(t,n)


# $$
# \frac{dx}{dt} = ax\cdot (1-x/K)
# $$
# 

# In[4]:


print("here")
No=2

x=No
t=0
a=0.5
dt=0.0001
K=200

# this a comment for later
maximum_time=20
number_of_times_to_repeat=int(maximum_time/dt)
for i in range(number_of_times_to_repeat):
#     print(i)
#     print("this")
    dx=(a*x*(1-x/K))*dt
    x=x+dx
    t=t+dt
    print(t,x)
    
print("there")
print(t,x)


# In[5]:


number_of_times_to_repeat


# # explore lists a little

# In[10]:


L=[3,-20,35,42]


# In[11]:


L


# In[12]:


L.append(6)


# In[13]:


L


# In[14]:


L[3]


# In[15]:


L[0]


# In[17]:


for i in range(5+1):
    print(i)


# add up all numbers from 1 to 100

# In[19]:


mysum=0
for i in range(1,100+1):
    #print(i)
    mysum=mysum+i
    
print(mysum)


# In[20]:


x_list=[]
for i in range(5):
    x_list.append(2*i)
    
x_list


# back to the simulation, but keeping x and t

# In[34]:


print("here")
No=2

n=No
t=0
a=0.5
dt=0.0001
K=100

maximum_time=20
number_of_times_to_repeat=int(maximum_time/dt)

n_list=[n]
t_list=[t]
for i in range(number_of_times_to_repeat):
    dn=(a*n*(1-n/K))*dt
    n=n+dn
    t=t+dt
    
    n_list.append(n)
    t_list.append(t)
    
print("there")
print(t,n)


# In[35]:


plot(t_list,n_list)


# In[37]:


print("here")
No=2

n=No
t=0
a=0.5
dt=0.0001
K=200

maximum_time=20
number_of_times_to_repeat=int(maximum_time/dt)

n_list=[n]
t_list=[t]
for i in range(number_of_times_to_repeat):
    dn=(a*n*(1-n/K))*dt
    n=n+dn
    t=t+dt
    
    n_list.append(n)
    t_list.append(t)
    
plot(t_list,n_list)


# # Another system
# 
# $$
# \frac{dx}{dt} = v
# $$
# 
# $$
# \frac{dv}{dt} = r\cdot t
# $$

# In[38]:




# initial values of variables
t=0
x=0
v=0

# parameters
r=8

# deal with time
dt=0.0001
maximum_time=20
number_of_times_to_repeat=int(maximum_time/dt)

# initial lists for variables
x_list=[x]
v_list=[v]
t_list=[t]
for i in range(number_of_times_to_repeat):
    # how the variables change
    dx=v*dt
    dv=r*t*dt
    
    # update the variable values, and time
    x=x+dx
    v=v+dv
    t=t+dt
    
    # store the results in a list
    x_list.append(x)
    v_list.append(v)
    t_list.append(t)
    


# In[39]:


plot(t_list,x_list)


# In[40]:


plot(t_list,v_list)


# In[ ]:




