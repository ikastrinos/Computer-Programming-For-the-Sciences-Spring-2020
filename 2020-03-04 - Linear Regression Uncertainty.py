#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# ## one example

# In[3]:


data=pd.read_csv('data/linear_data.csv')
data


# In[4]:


x=array(data['x'])
y=array(data['y'])
x,y


# In[5]:


plot(x,y,'o')


# In[6]:


from sie.mcmc import MCMCModel,Uniform,Normal,Jeffreys


# In[7]:


def P_data(data,m,b,σ):
    x,y=data
    μ=m*x+b
    distribution=Normal(μ,σ)
    return sum(distribution(y))


# In[8]:


data=x,y
model=MCMCModel(data,P_data,
                m=Normal(0,10),
                b=Uniform(-10,10),
                σ=Jeffreys(),
               )


# In[9]:


for i in range(2):
    model.run_mcmc(500)
model.plot_chains()


# In[17]:


model.plot_distributions()


# In[ ]:





# In[ ]:





# In[11]:


data=pd.read_csv('data/linear_data.csv')
model=ols('y ~ x', data=data)
results=model.fit()
results.summary()


# In[21]:


figure(figsize=(8,5))
plot(data['x'],data['y'],'o')

for result in ols_result_random_samples(results):
    xx=linspace(-5,5,20)
    yy=result.predict({'x':xx})
    plot(xx,yy,'b-',alpha=0.01)


# ## another example

# In[22]:


data=pd.read_csv('data/temperature.txt',delim_whitespace=True)
data


# In[23]:


offset=1900
data['Year_Offset']=data['Year']-offset
model=ols('Annual_Mean ~ Year_Offset', data=data)
results=model.fit()
results.summary()


# In[24]:


figure(figsize=(8,5))
plot(data['Year'],data['Annual_Mean'],'o')

xx=linspace(1880,2020,20)
yy=results.predict({'Year_Offset':xx-offset})
plot(xx,yy,'-')


# In[25]:


figure(figsize=(8,5))
plot(data['Year'],data['Annual_Mean'],'o')

for result in ols_result_random_samples(results):
    xx=linspace(1880,2020,20)
    yy=result.predict({'Year_Offset':xx-offset})
    plot(xx,yy,'b-',alpha=0.01)


# In[ ]:




