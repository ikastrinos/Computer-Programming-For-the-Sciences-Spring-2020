#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


θ=linspace(0,1,11)
θ


# In[4]:


def fact(N):
    val=1
    for i in range(1,N+1):
        val=val*i
        
    return val


# In[5]:


fact(5)


# In[6]:


D=3
U=9
N=D+U


# In[7]:


p=fact(N)/fact(D)/fact(U)*θ**(D)*(1-θ)**(N-D)

p=fact(N)/(fact(D)*fact(U))*θ**(D)*(1-θ)**(N-D)


# In[8]:


p


# In[9]:


sum(p)


# In[10]:


K=sum(p)
p=p/K


# In[11]:


sum(p)


# In[12]:


figure(figsize=(8,4))
plot(θ,p,'-o')
xlabel('θ')


# In[13]:


D,U=0,0
N=D+U
p=fact(N)/fact(D)/fact(U)*θ**(D)*(1-θ)**(N-D)
p=p/sum(p)
figure(figsize=(8,4))
plot(θ,p,'-o')
xlabel('θ')


# In[14]:


data=[(0,0),(0,1),(0,2),(1,2)]
figure(figsize=(8,4))

for D,U in data:
#D,U=0,1
    N=D+U
    p=fact(N)/fact(D)/fact(U)*θ**(D)*(1-θ)**(N-D)
    p=p/sum(p)
    plot(θ,p,'-o',label=str((D,U)))
    xlabel('θ')
legend()


# In[15]:


data=[(1,2)]
figure(figsize=(8,4))

for D,U in data:
#D,U=0,1
    N=D+U
    p=fact(N)/fact(D)/fact(U)*θ**(D)*(1-θ)**(N-D)
    p=p/sum(p)
    plot(θ,p,'-o',label=str((D,U)))
    xlabel('θ')
legend()


# In[16]:


p


# In[17]:


p[(θ>.1) & (θ<0.8)].sum()


# In[18]:


θ=linspace(0,1,53)
θ


# In[19]:


dθ=θ[1]-θ[0]
dθ


# In[20]:


data=[(1,2)]
figure(figsize=(8,4))

for D,U in data:
#D,U=0,1
    N=D+U
    p=fact(N)/fact(D)/fact(U)*θ**(D)*(1-θ)**(N-D)
    p=p/sum(p*dθ)
    print(sum(p*dθ))
    plot(θ,p,'-o',label=str((D,U)))
    xlabel('θ')
legend()


# In[21]:


θ=linspace(0,1,101)
dθ=θ[1]-θ[0]
data=[(1,2)]
figure(figsize=(8,4))

for D,U in data:
#D,U=0,1
    N=D+U
    p=fact(N)/fact(D)/fact(U)*θ**(D)*(1-θ)**(N-D)
    p=p/sum(p*dθ)
    print(sum(p*dθ))
    plot(θ,p,'-',label=str((D,U)))
    xlabel('θ')
legend()


# In[22]:


(p[(θ<=.5)]*dθ).sum()


# In[23]:


θ=linspace(0,1,101)
dθ=θ[1]-θ[0]
data=[(1,2),(3,9)]
figure(figsize=(8,4))

for D,U in data:
#D,U=0,1
    N=D+U
    p=fact(N)/fact(D)/fact(U)*θ**(D)*(1-θ)**(N-D)
    p=p/sum(p*dθ)
    print(sum(p*dθ))
    plot(θ,p,'-',label=str((D,U)))
    xlabel('θ')
legend()


# In[24]:


(p[(θ<=.5)]*dθ).sum()


# In[27]:


θ=linspace(0,1,101)
dθ=θ[1]-θ[0]
data=[(1,2),(60,180)]
figure(figsize=(8,4))

for D,U in data:
#D,U=0,1
    N=D+U
    p=fact(N)/fact(D)/fact(U)*θ**(D)*(1-θ)**(N-D)
    p=p/sum(p*dθ)
    print(sum(p*dθ))
    plot(θ,p,'-',label=str((D,U)))
    xlabel('θ')
legend()


# In[ ]:




