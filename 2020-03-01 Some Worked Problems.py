#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *
import pandas as pd


# In[7]:


from sie.mcmc import MCMCModel,Bernoulli,Uniform,Cauchy,Normal,Jeffreys,Beta
rcParams['figure.figsize']=(8,6)


# ## Coin Flip Model

# In[12]:


D=3
U=9
N=D+U


# In[13]:


def P_data(data,θ):
    D,U=data
    N=D+U
    
    return D*log(θ) + (N-D)*log(1-θ)


# In[19]:


def P_data(data,θ):
    D,U=data
    N=D+U
    
    distribution=Beta(D,N)
    return distribution(θ)


# In[20]:


data=D,U
model=MCMCModel(data,P_data,
                θ=Uniform(0,1))


# In[21]:


model.run_mcmc(500)
model.plot_chains()


# In[22]:


model.plot_distributions()


# In[23]:


model.P("θ<=0.5")


# In[ ]:





# In[ ]:





# ## Pennies

# In[4]:


year,m=(array([1960., 1961., 1962., 1963., 1964., 1965., 1966., 1967., 1968., 1969., 1970., 1971., 1972., 1973., 1974.]),
        array([3.133, 3.083, 3.175, 3.12 , 3.1  , 3.06 , 3.1  , 3.1  , 3.073,
        3.076, 3.1  , 3.11 , 3.08 , 3.1  , 3.093]))


# In[23]:


figure(figsize=(12,6))
plot(year,m,'-o')
ylabel('Mass [g]')
title('Pennies')
xticks(arange(1960,1974+1,2));


# ## Known  deviation, $\sigma$
# 
# \begin{align}
# \mu &\sim {\rm Uniform}(-\infty,+\infty) \\
# x_i &\sim {\rm Normal}(\mu,\sigma=0.1) \sim P(x_i|\mu,\sigma) = \frac{1}{2\pi\sigma^2}\cdot e^{-(x_i-\mu)^2/2/\sigma^2}
# \end{align}

# In[6]:


def P_data(data,μ):
    x=data
    σ=0.1
    distribution=Normal(μ,σ)
    return sum(distribution(data))


# In[7]:


data=m
model=MCMCModel(data,P_data,
                μ=Uniform(0,10))


# In[8]:


model.run_mcmc(500)
model.plot_chains()


# In[9]:


model.plot_distributions()


# ## Unknown $\sigma$
# 
# \begin{align}
# \sigma &\sim {\rm Jeffreys}()\sim P(\sigma) = 1/\sigma \\
# \mu &\sim {\rm Uniform}(-\infty,+\infty) \\
# x_i &\sim {\rm Normal}(\mu,\sigma=0.1) \sim P(x_i|\mu,\sigma) = \frac{1}{2\pi\sigma^2}\cdot e^{-(x_i-\mu)^2/2/\sigma^2}
# \end{align}

# In[10]:


def P_data(data,μ,σ):
    x=data
    distribution=Normal(μ,σ)
    return sum(distribution(data))


# In[12]:


data=m
model=MCMCModel(data,P_data,
                μ=Uniform(0,10),
                σ=Jeffreys(),
               )


# In[13]:


model.run_mcmc(500)
model.plot_chains()


# In[14]:


model.plot_distributions()


# In[15]:


model.P("μ>3.1")


# ## Lighthouse problem
# 
# \begin{align}
# \alpha &\sim {\rm Uniform}(-\infty,+\infty) \\
# x_i &\sim {\rm Cauchy}(\alpha,\beta=1)
# \end{align}

# In[6]:


def P_data(data,α):
    x=data
    β=1
    distribution=Cauchy(α,scale=β)
    return sum(distribution(data))


# In[7]:


data=array([ -4.88670033,   1.02727087,   1.64012807,   1.16570506,
         0.74137098,   1.45785143,   0.75576402,  -7.16204611,
         0.30565497,   2.48463354,   0.98340414,   1.69667592,
         0.50776928, -26.27862631,   2.55648882,   0.85903135,
        -0.72341857,   0.40990678,   1.25050285,   1.61812728])


# In[8]:


model=MCMCModel(data,P_data,
                α=Uniform(-10,10))


# In[9]:


model.run_mcmc(500)
model.plot_chains()


# In[10]:


model.plot_distributions()


# In[11]:


model.P("α>0.5")


# ### the t-test doesn't work

# In[12]:


N=len(data)
S=std(data,ddof=1)
K=1-20/N**2

mean(data),K*S/sqrt(N)


# ## Regression

# In[21]:


data=pd.read_excel('data/Pennies.xlsx')
data.head()


# In[47]:


x=array(data['Year'])
M=array(data['Mass (g)'])
N=array(data['Number of Pennies'])
y=M/N


figure(figsize=(12,6))
plot(x,y,'-o')
ylabel('Mass [g]')
title('Pennies')


# In[25]:


y=y[x<=1981]
x=x[x<=1981]

figure(figsize=(12,6))
plot(x,y,'-o')
ylabel('Mass [g]')
title('Pennies')


# \begin{align}
# \sigma &\sim {\rm Jeffreys}()\sim P(\sigma) = 1/\sigma \\
# m &\sim {\rm Normal}(0,10)\\
# b &\sim {\rm Uniform}(-\infty,+\infty)\\
# \mu_i &= m x_i + b\\
# y_i &\sim {\rm Normal}(\mu_i,\sigma) \sim P(x_i|\mu,\sigma) = \frac{1}{2\pi\sigma^2}\cdot e^{-(y_i-\mu_i)^2/2/\sigma^2}
# \end{align}

# In[26]:


def P_data(data,m,b,σ):
    x,y=data
    μ=m*x+b
    distribution=Normal(μ,σ)
    return sum(distribution(y))


# In[31]:


data=x-1960,y
model=MCMCModel(data,P_data,
                m=Normal(0,10),
                b=Uniform(-10,10),
                σ=Jeffreys(),
               )


# In[34]:


model.run_mcmc(500)
model.plot_chains()


# In[35]:


model.plot_distributions()


# ## Two-part model

# In[75]:


data=pd.read_excel('data/Pennies.xlsx')
x=array(data['Year'])
M=array(data['Mass (g)'])
N=array(data['Number of Pennies'])
y=M/N


# remove the outliers, for now
idx=where( (x<1982) | ((x>1982) & (y<2.6) & (y>2.4)))
x=x[idx]
y=y[idx]



figure(figsize=(12,6))
plot(x,y,'-o')
ylabel('Mass [g]')
title('Pennies')


# In[76]:


def P_data(data,m1,b1,m2,b2,σ):
    x,y=data
    μ=m1*x+b1
    
    idx=where(x>=23)[0]
    μ[idx]=m2*x[idx]+b2
    
    distribution=Normal(μ,σ)
    return sum(distribution(y))


# In[77]:


data=x-1960,y
model=MCMCModel(data,P_data,
                m1=Normal(0,10),
                b1=Uniform(-10,10),
                m2=Normal(0,10),
                b2=Uniform(-10,10),
                σ=Jeffreys(),
               )


# In[80]:


model.run_mcmc(500)
model.plot_chains()


# In[81]:


model.plot_distributions()


# In[ ]:





# # Pyndamics

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from pyndamics import Simulation
from pyndamics.emcee import *


# ## Growth of a sunflower
# 
# Data from [http://www.seattlecentral.edu/qelp/sets/009/009.html](http://www.seattlecentral.edu/qelp/sets/009/009.html)

# In[3]:


t=array([7,14,21,28,35,42,49,56,63,70,77,84],float)
h=array([17.93,36.36,67.76,98.10,131,169.5,205.5,228.3,247.1,250.5,253.8,254.5])

plot(t,h,'-o')
xlabel('Days')
ylabel('Height [cm]')


# In[4]:


sim=Simulation()
sim.add("h'=a",1,plot=True)
sim.add_data(t=t,h=h,plot=True)
sim.params(a=1)
sim.run(0,90)


# In[5]:


model=MCMCModel(sim,a=Uniform(-10,10))


# In[6]:


model.run_mcmc(500)
model.plot_chains()


# In[7]:


model.best_estimates()


# In[8]:


sim.run(0,90)


# In[9]:


model.plot_distributions()


# In[10]:


model=MCMCModel(sim,
                a=Uniform(-10,10),
                initial_h=Uniform(0,180),
                )


# In[11]:


model.run_mcmc(500)
model.plot_chains()


# In[12]:


sim.run(0,90)
model.plot_distributions()


# In[13]:


model.plot_many(0,90,'h')


# In[14]:


model.triangle_plot()


# ## Logistic growth

# In[15]:


sim=Simulation()
sim.add("h'=a*h*(1-h/K)",1,plot=True)
sim.add_data(t=t,h=h,plot=True)
sim.params(a=1,K=500)
sim.run(0,90)


# In[18]:


model=MCMCModel(sim,
                a=Uniform(.001,5),
                K=Uniform(100,500),
                initial_h=Uniform(0,10),
                )


# In[19]:


model.run_mcmc(500)
model.plot_chains()


# In[20]:


for i in range(2):
    model.set_initial_values('samples')  # reset using the 16-84 percentile values from the samples
    model.run_mcmc(500)
model.plot_chains()


# In[21]:


model.best_estimates()


# In[22]:


model.plot_distributions()


# In[23]:


model.plot_many(0,90,'h')


# In[ ]:




