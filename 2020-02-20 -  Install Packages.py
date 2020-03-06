#!/usr/bin/env python
# coding: utf-8

# # Git For Windows

# https://git-scm.com/download/win

# # Course GitHub

# In[1]:


def get_course_github(name='Computer-Programming-For-the-Sciences-Spring-2020'):
    import os,sys,platform
    
    if not os.path.exists(name):
            get_ipython().system('git clone https://github.com/bblais/Computer-Programming-For-the-Sciences-Spring-2020 Computer-Programming-For-the-Sciences-Spring-2020            ')
    else:
        if platform.system()=="Windows":
            get_ipython().system('cd Computer-Programming-For-the-Sciences-Spring-2020 & git pull https://github.com/bblais/Computer-Programming-For-the-Sciences-Spring-2020 ')
        else:
            get_ipython().system('cd Computer-Programming-For-the-Sciences-Spring-2020; git pull https://github.com/bblais/Computer-Programming-For-the-Sciences-Spring-2020 ')
        


# In[2]:


get_course_github()


# # Pyndamics

# In[3]:


pip install "git+git://github.com/bblais/pyndamics" --upgrade


# # Emcee

# In[4]:


pip install -U emcee


# # SIE

# In[6]:


pip install "git+git://github.com/bblais/Statistical-Inference-for-Everyone#egg=sie&subdirectory=python/sie" --upgrade 


# In[4]:


import pyndamics


# In[5]:


pyndamics.__file__


# In[13]:


import sie


# In[ ]:




