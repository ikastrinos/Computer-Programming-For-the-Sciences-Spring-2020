#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# $$
# \frac{dy}{dt} = a+b\sin(c\cdot t)
# $$
# 
# $$
# dy  = \left(a+b\sin(c\cdot t) \right) \cdot dt
# $$
# 
# 
# Solution (https://www.wolframalpha.com/input/?i=integrate%28a%2Bb*sin%28c*t%29%2Ct%29):
# 
# $$
# y(t)=a t - \frac{b \cos(c\cdot t)}{c} + {\rm constant}
# $$

# In[2]:


y=0
t=0
a=0.5
b=1
c=2

dt=0.0001

maximum_time=20
number_of_times_to_repeat=int(maximum_time/dt)

y_list=[y]
t_list=[t]
for i in range(number_of_times_to_repeat):
    dy=(a+b*sin(c*t))*dt
    y=y+dy
    t=t+dt
    
    y_list.append(y)
    t_list.append(t)


# In[3]:


plot(t_list,y_list)
xlabel('time')
ylabel('y')


# In[5]:


plot(t_list,y_list)
xlabel('time [s]')
ylabel('position [m]')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# Things I don't like about this plot:
# 
# * fonts too small
# * figure too small
# * I like grids over no-grids

# In[6]:


from matplotlib import rcParams

fontsize=20

rcParams['font.size']=fontsize
rcParams['font.family']='sans-serif'

rcParams['axes.labelsize']=fontsize
rcParams['axes.titlesize']=fontsize
rcParams['xtick.labelsize']=fontsize
rcParams['ytick.labelsize']=fontsize
rcParams['legend.fontsize']=fontsize

rcParams['figure.figsize']=(12,8)

rcParams['axes.grid']=True


# In[7]:


plot(t_list,y_list)
xlabel('time [s]')
ylabel('position [m]')


# ## what is the effect of $a$

# In[14]:


y=0
t=0
a=0.5
b=1
c=2

dt=0.0001

maximum_time=20
number_of_times_to_repeat=int(maximum_time/dt)

y_list=[y]
t_list=[t]
for i in range(number_of_times_to_repeat):
    dy=(a+b*sin(c*t))*dt
    y=y+dy
    t=t+dt
    
    y_list.append(y)
    t_list.append(t)

    
plot(t_list,y_list,label=f'a={a}')
xlabel('time [s]')
ylabel('position [m]')

#=============================================


y=0
t=0
a=1.2
b=1
c=2

dt=0.0001

maximum_time=20
number_of_times_to_repeat=int(maximum_time/dt)

y_list=[y]
t_list=[t]
for i in range(number_of_times_to_repeat):
    dy=(a+b*sin(c*t))*dt
    y=y+dy
    t=t+dt
    
    y_list.append(y)
    t_list.append(t)

    
plot(t_list,y_list,label=f'a={a}')
xlabel('time [s]')
ylabel('position [m]')


#=============================================


y=0
t=0
a=2.3
b=1
c=2

dt=0.0001

maximum_time=20
number_of_times_to_repeat=int(maximum_time/dt)

y_list=[y]
t_list=[t]
for i in range(number_of_times_to_repeat):
    dy=(a+b*sin(c*t))*dt
    y=y+dy
    t=t+dt
    
    y_list.append(y)
    t_list.append(t)

    
plot(t_list,y_list,label=f'a={a}')
xlabel('time [s]')
ylabel('position [m]')


legend()


# In[27]:


len(y_list)


# In[ ]:





# In[11]:


a


# In[13]:


f'the value of a is {a}'


# In[15]:



for a in [0.5,1.2,2.3]:

    y=0
    t=0
    #a=2.3
    b=1
    c=2

    dt=0.0001

    maximum_time=20
    number_of_times_to_repeat=int(maximum_time/dt)

    y_list=[y]
    t_list=[t]
    for i in range(number_of_times_to_repeat):
        dy=(a+b*sin(c*t))*dt
        y=y+dy
        t=t+dt

        y_list.append(y)
        t_list.append(t)


    plot(t_list,y_list,label=f'a={a}')
    
xlabel('time [s]')
ylabel('position [m]')
legend()


# In[17]:


a_list=[]
last_point_list=[]

for a in [0,0.5,1,1.5,2,2.5,3,3.5,4]:

    y=0
    t=0
    #a=2.3
    b=1
    c=2

    dt=0.0001

    maximum_time=20
    number_of_times_to_repeat=int(maximum_time/dt)

    y_list=[y]
    t_list=[t]
    for i in range(number_of_times_to_repeat):
        dy=(a+b*sin(c*t))*dt
        y=y+dy
        t=t+dt

        y_list.append(y)
        t_list.append(t)


    plot(t_list,y_list,label=f'a={a}')
    
    a_list.append(a)
    last_point_list.append(y_list[-1])
    
xlabel('time [s]')
ylabel('position [m]')
legend()


# In[18]:


a_list


# In[19]:


last_point_list


# In[22]:


plot(a_list,last_point_list,'-o')
xlabel('a')
ylabel('last point')


# In[23]:


last_point_list


# In[24]:


last_point_list[2]


# In[25]:


last_point_list[-1]


# In[26]:


last_point_list[-2]


# ## don't need to save every single time step

# In[32]:



for a in [0.5,1.2,2.3]:

    y=0
    t=0
    #a=2.3
    b=1
    c=2

    dt=0.0001

    maximum_time=20
    number_of_times_to_repeat=int(maximum_time/dt)

    y_list=[y]
    t_list=[t]
    for i in range(number_of_times_to_repeat):
        dy=(a+b*sin(c*t))*dt
        y=y+dy
        t=t+dt

        if i%100 == 0 :
            y_list.append(y)
            t_list.append(t)


    plot(t_list,y_list,label=f'a={a}')
    
xlabel('time [s]')
ylabel('position [m]')
legend()


# In[33]:


len(y_list)


# ## loading data and plotting

# In[34]:


import pandas as pd


# In[38]:


data=pd.read_excel('data/ligo_L1.xlsx')
data.head()


# In[36]:


pwd


# In[37]:


x=data['time (seconds)']
y=data['strain (*1e21)']
plot(x,y,'o')


# ## format on plot

# In[39]:


plot(x,y,'o')  # just markers


# In[40]:


plot(x,y,'-')  # just lines


# In[41]:


plot(x,y,'--')  # dashed lines


# In[42]:


plot(x,y,'o-')  #  markers and lines


# In[43]:


plot(x,y,'ro-')  #  red markers and lines


# In[48]:


get_ipython().run_line_magic('pinfo', 'pd.read_excel')


# In[ ]:




