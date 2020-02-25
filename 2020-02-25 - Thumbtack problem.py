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


# In[6]:


fact(5)


# In[7]:


D=3
U=9
N=D+U


# In[10]:


p=fact(N)/fact(D)/fact(U)*θ**(D)*(1-θ)**(N-D)

p=fact(N)/(fact(D)*fact(U))*θ**(D)*(1-θ)**(N-D)


# In[11]:


p


# In[12]:


sum(p)


# In[13]:


K=sum(p)
p=p/K


# In[14]:


sum(p)


# In[17]:


figure(figsize=(8,4))
plot(θ,p,'-o')
xlabel('θ')


# In[19]:


D,U=0,0
N=D+U
p=fact(N)/fact(D)/fact(U)*θ**(D)*(1-θ)**(N-D)
p=p/sum(p)
figure(figsize=(8,4))
plot(θ,p,'-o')
xlabel('θ')


# In[24]:


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


# In[25]:


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


# In[26]:


p


# In[30]:


p[(θ>.1) & (θ<0.8)].sum()


# In[34]:


θ=linspace(0,1,53)
θ


# In[35]:


dθ=θ[1]-θ[0]
dθ


# In[36]:


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


# In[37]:


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


# In[38]:


(p[(θ<=.5)]*dθ).sum()


# In[39]:


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


# In[40]:


(p[(θ<=.5)]*dθ).sum()


# In[41]:


θ=linspace(0,1,101)
dθ=θ[1]-θ[0]
data=[(1,2),(300,900)]
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




