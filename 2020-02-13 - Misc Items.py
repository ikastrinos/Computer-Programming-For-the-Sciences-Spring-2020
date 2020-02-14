#!/usr/bin/env python
# coding: utf-8

# ## An easy math problem Excel gets wrong

# In[1]:


-5**2


# In[20]:


get_ipython().run_line_magic('pylab', 'inline')
from defaults import *
import pandas as pd


# ## Make some random data with dates and names to select from

# In[56]:


data=pd.DataFrame() # an empty data set
# make up some date strings to deal with
month=1
day=1
year=1900
dates=[]
names=[]
values=[]
for name in ['bob','charlie']:
    for year in [1900,1901,1902]:
        for month in [1,2,3,4,5,6,7,8,9,10,11,12]:

            s='%d-%02d-%02d' % (year,month,day)

            dates.append(s)
            names.append(name)
            if name=='bob':
                values.append(randn())
            else:
                values.append(10*rand())
            
data['dates']=dates
data['values']=values
data['names']=names


# In[57]:


data


# ## selecting a subset

# In[58]:


data['names']=='bob'


# In[59]:


df_bob=data[data['names']=='bob']  # read it like: the data where the data['names'] is 'bob'
df_bob


# In[60]:


df_charlie=data[data['names']=='charlie']  # read it like: the data where the data['names'] is 'bob'
df_charlie


# In[61]:


df=df_bob


# ## Dates to floats

# ### this plot is broken, because dates are all strings

# In[62]:


x=df['dates']
y=df['values']
plot(x,y,'-o')


# In[63]:


def date_to_float(d):
    
    from dateutil import parser
    import datetime  
    from numpy import array
    
    try:
        dt=parser.parse(d)
        year=dt.year
        f=year+(dt-datetime.datetime(year, 1, 1, 0, 0))/(datetime.datetime(year+1, 1, 1, 0, 0)-datetime.datetime(year, 1, 1, 0, 0))

        return f
    except TypeError:
        f=[date_to_float(_) for _ in array(d)]
        return array(f)


# In[64]:


x=date_to_float(df['dates'])


# In[65]:


x[:5]


# In[66]:


plot(x,y,'-o')


# ## putting it together

# In[68]:


x=date_to_float(df_bob['dates'])
y=df_bob['values']
plot(x,y,'-o',label='bob')

x=date_to_float(df_charlie['dates'])
y=df_charlie['values']
plot(x,y,'-s',label='charlie')

legend()


# ## inverting the axis

# In[71]:


x=date_to_float(df_bob['dates'])
y=df_bob['values']
plot(x,y,'-o',label='bob')

x=date_to_float(df_charlie['dates'])
y=df_charlie['values']
plot(x,y,'-s',label='charlie')

legend()

gca().invert_yaxis()


# In[ ]:




