#!/usr/bin/env python
# coding: utf-8

# # Git For Windows

# https://git-scm.com/download/win

# # Course GitHub

# In[5]:


def get_course_github(name='Computer-Programming-For-the-Sciences-Spring-2020'):
    import os,sys
    if not os.path.exists(name):
        get_ipython().system('git clone https://github.com/bblais/Computer-Programming-For-the-Sciences-Spring-2020 Computer-Programming-For-the-Sciences-Spring-2020')
    else:
        get_ipython().system('cd Computer-Programming-For-the-Sciences-Spring-2020; git pull https://github.com/bblais/Computer-Programming-For-the-Sciences-Spring-2020 ')
        


# In[ ]:





# In[6]:


get_course_github()


# # Pyndamics

# In[7]:


pip install "git+git://github.com/bblais/pyndamics" --upgrade


# # Emcee

# In[4]:


pip install -U emcee


# # SIE

# In[1]:


pip install "git+git://github.com/bblais/Statistical-Inference-for-Everyone#egg=sie&subdirectory=python/sie" --upgrade


# In[ ]:




