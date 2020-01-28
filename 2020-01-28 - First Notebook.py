#!/usr/bin/env python
# coding: utf-8

# In[2]:


pwd


# In[4]:


5*8


# In[5]:


6*3


# In[6]:


a=8*9


# In[7]:


a


# In[8]:


a+20


# In[31]:


from numpy import sin,pi,radians


# In[30]:


pi


# In[27]:


a=sin(30*3.1415926535897932/180)


# In[32]:


a=sin(radians(30))


# In[33]:


a


# In[34]:


type(a)


# In[35]:


b=5


# In[36]:


type(b)


# In[22]:


a=Sin(30)


# In[14]:


a


# In[15]:


a=92
a=a+8


# In[17]:


a


# In[18]:


b=a=a*2


# In[19]:


a


# In[20]:


b


# In[21]:


c


# In[23]:


bob=10
sally=20
bob+sally


# In[40]:


print("here")
for i in range(7):
    print(i)
    print("this")
    
print("there")


# In[41]:


print("here")
a=2
for i in range(7):
    print(i)
    print("this")
    a=a*2
    
print("there")
print(a)


# In[42]:


print("here")
a=5
for i in range(7):
    print(i)
    print("this")
    a=a+0.2
    
print("there")
print(a)


# In[44]:


print("here")
n=1000000
t=0
r=0.1
dt=0.2

for i in range(7):
    print(i)
    print("this")
    dn=r*n*dt
    n=n+dn
    t=t+dt
    print(t,n)
    
print("there")
print(t,n)


# In[58]:


number_of_times_to_repeat=int(20/dt)
number_of_times_to_repeat


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

# In[79]:


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


# In[80]:


t,n


# In[81]:


from numpy import exp


# In[82]:


No*exp(r*t),No*exp(r*t)-n


# In[52]:


number_of_times_to_repeat


# In[ ]:




