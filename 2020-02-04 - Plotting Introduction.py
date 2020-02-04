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


# In[ ]:




