#!/usr/bin/env python
# coding: utf-8

# # Git For Windows

# https://git-scm.com/download/win

# # Course GitHub

# In[23]:


def get_course_github():
    import os,sys
    if not os.path.exists(name):
        get_ipython().system('git clone https://github.com/bblais/Computer-Programming-For-the-Sciences-Spring-2020 Computer-Programming-For-the-Sciences-Spring-2020')
    else:
        get_ipython().system('cd Computer-Programming-For-the-Sciences-Spring-2020; git pull https://github.com/bblais/Computer-Programming-For-the-Sciences-Spring-2020 ')
        


# In[22]:


get_course_github()


# # Pyndamics

# In[3]:


pip install "git+git://github.com/bblais/pyndamics" --upgrade


# # Emcee

# In[4]:


pip install -U emcee


# In[ ]:




