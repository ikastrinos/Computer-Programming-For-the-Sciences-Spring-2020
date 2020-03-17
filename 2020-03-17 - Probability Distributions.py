#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# $$
# p(x) = (x-2)^2
# $$
# 
# with $x$ between 0 and 10.

# In[4]:


x=linspace(0,10,100)
p=(x-2)**2
plot(x,p)


# $$
# \int_0^{10} p(x)dx = 1
# $$

# if I want, say, $p(x>6)$:
# 
# $$
# \int_6^{10} p(x)dx 
# $$

# In[8]:


x=linspace(0,10,2000)
dx=x[1]-x[0]
dx


# In[9]:


p=(x-2)**2


# In[10]:


sum(p*dx)


# In[11]:


p=p/sum(p*dx)  # normalizing


# In[12]:


sum(p*dx)


# In[13]:


sum(p[x>6]*dx)


# In[14]:


plot(x,p)


# In[ ]:




