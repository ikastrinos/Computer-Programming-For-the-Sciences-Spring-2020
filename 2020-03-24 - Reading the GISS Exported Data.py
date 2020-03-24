#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


data=pd.read_csv("data/station_temperature_data.csv.gz",index_col=False)


# In[4]:


info=pd.read_excel("data/station_info.xlsx")


# In[5]:


info.head()


# In[6]:


data.tail()


# In[33]:


station='SAVE'
x=data['time']
y=data[station]
plot(x,y,'-o')
title(station)


# In[35]:


x,y   # lots of nans!


# In[36]:


def get_xy(data,station):
    x,y=array(data[['time',station]].dropna()).T    
    return x,y


# In[37]:


x,y=get_xy(data,station)


# In[38]:


model=ols('y ~ x', data={'y':y,'x':x})
results=model.fit()
results.summary()


# In[46]:


xx=linspace(min(x)-10,max(x)+10,20)
yy=results.predict({'x':xx})

m=results.params['x']
mσ=results.bse['x']

b=results.params['Intercept']

plot(x,y,'-o')
title(station+" : y=%.3g (+/- %.4g) x + %.3g" % (m,mσ,b))
plot(xx,yy,'b-')


# In[45]:


results.bse


# In[ ]:




