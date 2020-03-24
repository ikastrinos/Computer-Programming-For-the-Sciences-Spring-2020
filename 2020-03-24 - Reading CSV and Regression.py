#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# 1. went to https://data.giss.nasa.gov/gistemp/station_data_v4_globe/
# 2. Looked down at the bottom for the search, and searched for "berkeley"
# 3. then clicked the station name "Berkeley" hyperlink
# 4. at the bottom, downloaded the CSV
# 5. renamed the station.csv to berkeley.csv and put it in my data folder

# In[36]:


data=pd.read_csv('data/berkeley.csv')


# In[37]:


data


# In[39]:


x=array(data['YEAR'])
y=array(data['metANN'])
y[y==999.9]=nan


# In[40]:


x


# In[41]:


y


# In[42]:


station='BERKELEY'

plot(x,y,'-o')
ylabel('Temperature [C]')
title(station)


# In[43]:


model=ols('y ~ x', data={'y':y,'x':x})
results=model.fit()
results.summary()


# In[44]:


xx=linspace(min(x)-10,max(x)+10,20)
yy=results.predict({'x':xx})

m=results.params['x']
mσ=results.bse['x']

b=results.params['Intercept']

plot(x,y,'-o')
ylabel('Temperature [C]')
title(station+" : y=%.3g (+/- %.4g) x + %.3g" % (m,mσ,b))
plot(xx,yy,'b-')


# When uncertainty written like: 0.00481 +- 0.00125
# 
# * mean value of 0.00481
# * 1-$\sigma$ uncertainty is 0.00125
# * look at 95% range, then I look 2-$\sigma$ uncertainty

# In[46]:


v=0.00481
one_σ=0.00125
lower_bound=v - 2*one_σ
upper_bound=v + 2*one_σ

lower_bound,upper_bound


# In[47]:


0.00231*100 # per century


# ## Save the plot, but don't show it

# In[45]:


plot(x,y,'-o')
ylabel('Temperature [C]')
title(station+" : y=%.3g (+/- %.4g) x + %.3g" % (m,mσ,b))
plot(xx,yy,'b-')

fig=gcf()
fig.savefig(station+'.png')
close()


# In[ ]:




