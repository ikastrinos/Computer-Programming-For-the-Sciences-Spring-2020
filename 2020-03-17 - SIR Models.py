#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from pyndamics import Simulation


# $$
# \frac{dS}{dt} = -\beta S\cdot I
# $$
# 
# $$
# \frac{dI}{dt} = +\beta S\cdot I - \gamma I
# $$
# 
# $$
# \frac{dR}{dt} = +\gamma I
# $$

# In[6]:


sim=Simulation()
sim.add(" N  = S + I + R")
sim.add(" S' = -β*S/N*I",1000,plot=True)
sim.add(" I' = +β*S/N*I - γ*I",1,plot=True)
sim.add(" R' = + γ*I",0,plot=True)

sim.params(β=10,γ=0.1)
sim.run(0,10)


# In[ ]:




