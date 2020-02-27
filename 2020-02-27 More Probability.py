#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[14]:


θ=0.3
U=8000
N=10000
D=N-U


# In[15]:


θ**D * (1-θ)**(N-D)


# In[16]:


log(10)


# In[17]:


log10(10)


# In[18]:


sin(90)


# In[19]:


log=log10


# In[20]:


logP=D*log(θ) + (N-D)*log(1-θ)
logP


# In[21]:


10**(logP)


# In[23]:


def fact(N):
    val=1
    for i in range(1,N+1):
        val=val*i
        
    return val


# In[25]:


θ=linspace(0,1,101)
dθ=θ[1]-θ[0]
data=[(60,180)]
figure(figsize=(8,4))

for D,U in data:
    N=D+U
    
    
    p=fact(N)/fact(D)/fact(U)*θ**(D)*(1-θ)**(N-D)

    
    
    
    
#     p=p/sum(p*dθ)
#     print(sum(p*dθ))
#     plot(θ,p,'-',label=str((D,U)))
#     xlabel('θ')
# legend()


# In[26]:


D,U,N


# In[37]:


θ=linspace(0,1,11)
θ


# In[38]:


dθ


# In[39]:


# p=fact(N)/fact(D)/fact(U)*θ**(D)*(1-θ)**(N-D)
log_p=D*log(θ) + (N-D)*log(1-θ)
log_p


# In[41]:


log_p=log_p-log_p.max()
log_p


# In[42]:


p=exp(log_p)
p=p/sum(p*dθ)


# In[43]:


p


# In[46]:


θ=linspace(0.00001,.999999,101)
dθ=θ[1]-θ[0]
data=[(1,2),(60,180),(200,800)]
figure(figsize=(8,4))

for D,U in data:
    N=D+U
    
    
    #p=fact(N)/fact(D)/fact(U)*θ**(D)*(1-θ)**(N-D)
    log_p=D*log(θ) + (N-D)*log(1-θ)
    log_p=log_p-log_p.max()
    p=exp(log_p)
    p=p/sum(p*dθ)
    print(sum(p*dθ))
    plot(θ,p,'-',label=str((D,U)))
    xlabel('θ')
legend()


# In[59]:


zero=0.000001
one=0.99999
θ=linspace(zero,one,1001)
dθ=θ[1]-θ[0]
data=[(1,2),(60,180),(200,800)]
figure(figsize=(8,4))

for D,U in data:
    N=D+U
    
    
    #p=fact(N)/fact(D)/fact(U)*θ**(D)*(1-θ)**(N-D)
    log_p=D*log(θ) + (N-D)*log(1-θ)
    log_p=log_p-log_p.max()
    p=exp(log_p)
    p=p/sum(p*dθ)
    print(sum(p*dθ))
    plot(θ,p,'-',label=str((D,U)))
    xlabel('θ')
legend()

xlim([0,.4])


# In[53]:


p[(θ>.1) & (θ<0.8)].sum()


# In[54]:


p[(θ>.5)].sum()*dθ


# In[ ]:




