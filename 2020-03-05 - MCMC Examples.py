#!/usr/bin/env python
# coding: utf-8

# In[12]:


get_ipython().run_line_magic('pylab', 'inline')


# In[3]:


from sci378 import *


# In[4]:


from sie.mcmc import MCMCModel,Bernoulli,Uniform,Cauchy,Normal,Jeffreys,Beta
rcParams['figure.figsize']=(8,6)


# In[5]:


def P_data(data,θ):
    D,U=data
    N=D+U
    return D*log(θ)+ (N-D)*log(1-θ)


# In[7]:


D,U=data=3,9


# In[13]:


model=MCMCModel(data,P_data,
               θ=Uniform(0,1))


# In[14]:


model.run_mcmc(500)
model.plot_chains()


# In[15]:


model.plot_distributions()


# In[19]:


model.P("θ>0.9")


# ## Some other data

# In[22]:


data=pd.read_excel('data/Pennies.xlsx')
data.head()


# In[23]:


total_mass=array(data['Mass (g)'])
number_of_pennies=array(data['Number of Pennies'])
mass_per_penny=total_mass/number_of_pennies
year=array(data['Year'])


# In[24]:


plot(year,mass_per_penny,'-o')


# In[31]:


plot(year,mass_per_penny,'-o')
ylim([-10,10])


# In[26]:


plot(year,mass_per_penny,'-o')
xlim([1979,1984])


# In[27]:


m=mass_per_penny[year<1982]
y=year[year<1982]


# In[28]:


plot(y,m,'-o')


# In[32]:


def P_data(data,μ):
    x=data
    σ=0.1
    distribution=Normal(μ,σ)
    return sum(distribution(x))


# In[39]:


model=MCMCModel(m,P_data,
               μ=Normal(0,20))


# In[40]:


model.run_mcmc(500)
model.plot_chains()


# In[41]:


model.plot_distributions()


# In[42]:


def P_data(data,μ,σ):
    x=data
    distribution=Normal(μ,σ)
    return sum(distribution(x))


# In[43]:


model=MCMCModel(m,P_data,
               μ=Normal(0,20),
               σ=Uniform(0,10),
               )


# In[44]:


model.run_mcmc(500)
model.plot_chains()


# In[45]:


model.plot_distributions()


# In[49]:


model=MCMCModel(m,P_data,
               μ=Normal(0,20),
               σ=Jeffreys(),
               )


# In[50]:


model.run_mcmc(500)
model.plot_chains()

model.plot_distributions()


# In[51]:


model.run_mcmc(500)
model.plot_chains()

model.plot_distributions()


# In[52]:


model=MCMCModel(m,P_data,
               μ=Normal(0,20),
               σ=Jeffreys(),
               )

for i in range(2):
    model.run_mcmc(500)
    
    
model.plot_chains()
model.plot_distributions()


# In[ ]:




