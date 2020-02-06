#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from defaults import *


# In[4]:



for a in [0.5,1.2,2.3]:

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

        if i%100 == 0 :
            y_list.append(y)
            t_list.append(t)


    plot(t_list,y_list,label=f'a={a}')
    
xlabel('time [s]')
ylabel('position [m]')
legend()


# In[6]:


[1,2,3]*2


# In[7]:


a=[1,2,3]
2*a


# In[9]:


a=[1,'bob',50]
a


# In[10]:


2*a


# In[11]:


a=[1,2,3]


# In[12]:


array(a)


# In[13]:


b=array(a)


# In[14]:


b


# In[15]:


a


# In[16]:


2*a


# In[17]:


2*b


# In[19]:



for a in [0.5,1.2,2.3]:

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

        if i%100 == 0 :
            y_list.append(y)
            t_list.append(t)

    t_arr=array(t_list)
    y_arr=array(y_list)
    plot(t_arr,y_arr+rand(),label=f'a={a}')
    
xlabel('time [s]')
ylabel('position [m]')
legend()


# In[20]:


y_arr


# In[22]:


plot(t_arr,y_arr)
plot(t_arr,2*y_arr)


# In[23]:


plot(t_arr,2*t_arr+sin(t_arr))


# In[24]:


t=linspace(5,10,20)
t


# In[25]:


plot(t,5*t+3)


# In[ ]:




