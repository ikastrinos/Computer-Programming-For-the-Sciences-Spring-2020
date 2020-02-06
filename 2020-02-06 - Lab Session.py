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


# In[26]:


list(range(1,4))


# In[27]:


t=3
exp(t/2)


# In[28]:


e**(t/2)


# ## Comparing to an analytical solution
# 
# Taken from 2020-01-30 Simulation notebook
# 
# $$
# \frac{dx}{dt} = v
# $$
# 
# $$
# \frac{dv}{dt} = r\cdot t
# $$
# 

# In[29]:


# initial values of variables
t=0
x=0
v=0

# parameters
r=8

# deal with time
dt=0.0001
maximum_time=20
number_of_times_to_repeat=int(maximum_time/dt)

# initial lists for variables
x_list=[x]
v_list=[v]
t_list=[t]
for i in range(number_of_times_to_repeat):
    # how the variables change
    dx=v*dt
    dv=r*t*dt
    
    # update the variable values, and time
    x=x+dx
    v=v+dv
    t=t+dt
    
    # store the results in a list
    x_list.append(x)
    v_list.append(v)
    t_list.append(t)
    


# In[30]:


x=array(x_list)
v=array(v_list)
t=array(t_list)


# In[42]:


y_soln=t*sin(t)


# In[ ]:





# In[33]:


plot(t,x)

x_soln=1/6*r*t**3
plot(t,x_soln,'--')


# In[34]:


x=12


# In[35]:


x%2


# In[36]:


x%7


# In[45]:


x=2
count=0

if x%2==0:
    print("divisible by two!")
    print("another")
    count+=1
else:
    print("not.")


# In[39]:


a=array([2,3,5,7,12,17])


# In[40]:


a


# In[41]:


a%2


# In[ ]:




