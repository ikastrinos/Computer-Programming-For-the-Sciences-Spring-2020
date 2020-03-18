#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# Drawing a 7 and a 9 with replacement, so the 55 stays the same...

# calculating the numerators

# In[2]:


P_H=(7/55 * 9/55)* (1/2)
P_L=(4/55 * 2/55)* (1/2)


# In[3]:


P_H,P_L


# adding up the numerators and then dividing

# In[4]:


K=P_H+P_L


# In[5]:


P_H=P_H/K
P_L=P_L/K


# In[6]:


P_H,P_L


# with replacement, say, drawing 4 7's and 2 9's

# In[9]:


P_H=(7/55 * 7/55 * 7/55 * 7/55 * 9/55* 9/55)* (1/2)
P_H


# In[10]:


P_H=(7/55)**4 * (9/55)**2 * (1/2)
P_H


# In[11]:


P_H=(7/55)**4000 * (9/55)**2000 * (1/2)
P_H


# In[14]:


log_P_H = 4000*log10(7/55) + 2000*log10(9/55)+log10(1/2)
log_P_H


# <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/5ae9303fffd60858ddcc5e697dec847dc49849ed">

# In[32]:


α=0.2
xm=3

x=linspace(-3,30,1000)


# In[33]:


dx=x[1]-x[0]
dx


# In[34]:


p=zeros(len(x))
p[x>=xm]=α*xm**α/x[x>=xm]**(α+1)


# In[35]:


plot(x,p)


# $$
# \int_{-\infty}^{+\infty} p(x) dx =1
# $$

# In[36]:


sum(p*dx)


# In[37]:


p=p/sum(p*dx)


# In[38]:


sum(p*dx)


# In[39]:


plot(x,p)


# In[ ]:





# In[ ]:




