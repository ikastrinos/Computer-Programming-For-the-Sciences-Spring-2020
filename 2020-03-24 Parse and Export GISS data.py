#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from science import *


# In[3]:


import gzip


# In[4]:


timeit(reset=True)


# In[5]:


timeit()


# # Parsing the GISS Data
# 
# https://data.giss.nasa.gov/gistemp/station_data_v4_globe/
# 
# In our analysis, we can only use stations with reasonably long, consistently measured time records. This is a subset of the full list of stations (v4.temperature.inv.txt). That subset of list of stations (station_list.txt) that contribute to the final products may slightly change with each update, as the number of stations that get dropped due to the shortness of their temperature record may decrease when new data are added. Notice that as part of the homogenization, all stations with less than 20 years of data are discarded (as seen in part (a) of the figure below).
# 
# 
# The Brightness Index (BI) is used to categorize stations as rural or suburban. A station with a BI value equal to or less than ten is rural while greater than 10 is suburban.

# In[6]:


subset_station_lines=station_lines=open('data/station_list.txt').readlines()
all_station_lines=open('data/v4.temperature.inv.txt').readlines()


# In[7]:


with gzip.open('data/v4.mean_GISS_homogenized.txt.gz','rt') as fid:
    GISS_lines=fid.readlines()


# In[8]:


station_lines[:10]  # first 10 lines


# In[9]:


all_station_lines[:10]


# In[10]:


GISS_lines[:80]  # what are these numbers?


# First one is year, next ones are temperatures for the months, probably multiplied by 100

# Fixed length strings on station list  :-(

# In[11]:


header=station_lines[0].split('\t')
header


# In[12]:


header=GISS_lines[0].split()
header


# In[13]:


GISS_lines[-10:]


# In[ ]:





# In[14]:


data=[]
station_data=None
earliest_year=2019

count=0
print("Starting...",end="")
for line in GISS_lines:
    
    # do all the IDs start with A?
    if not line[0] in '12': # this is a header line, not starting with a 1 or a 2
        
        if not station_data is None:   #save the old station
            station_data.time=array(station_data.time)
            station_data.temperature=array(station_data.temperature)
            data.append(station_data)
            count+=1
            if count%100==0:
                print(".",end="")
            if count%1000==0:
                print("O",end="")
        
        station_data=Struct()

        header=line.split()
        #print(header)
        station_data.ID=header[0]
        station_data.lat=float(header[1])
        station_data.long=float(header[2])
        station_data.elev=float(header[3])
        station_data.station=header[4]
        
        if header[5]=='*':
            station_data.brightness=header[6]
        else:
            station_data.brightness=header[5]
            
        station_data.time=[]
        station_data.temperature=[]
        
        assert (len(header)==6) or ((len(header)==7) and (header[5]=='*'))
    else:  # this is a line of data
        parts=line.split()
        year=int(parts[0])
        
        if year<earliest_year:
            earliest_year=year
            
        raw_temp=[int(part) for part in parts[1:]]
        
        for i,raw_T in enumerate(raw_temp):
            time=year+i/12  # change the month into a real number
            T=raw_T/100
            
            
            station_data.time.append(time)
            
            if raw_T==-9999:
                station_data.temperature.append(nan)
            else:
                station_data.temperature.append(T)
            
            
            
data.append(station_data)
print("done.")


# In[15]:


earliest_year


# ## Can I make it into a single data frame or perhaps two?  average over a year

# In[16]:


len(station_lines)


# In[17]:


import pandas as pd


# In[18]:


time_arr=arange(1880,2021)
temperature_arr=nan*ones(len(time_arr))

data={'time':time_arr}
info=Struct({'ID':[],
      'Station':[],
      'Latitude':[],
      'Longitude':[],
      'Brightness':[],
      'Elevation':[],
     })


station_data=None

count=0
print("Starting...",end="")
for line in GISS_lines:
    
    # do all the IDs start with A?
    if not line[0] in '12': # this is a header line, not starting with a 1 or a 2
        
        if not station_data is None:   #save the old station
            data[station_data.station]=temperature_arr
            temperature_arr=nan*ones(len(time_arr))

            info.ID.append(station_data.ID)
            info.Station.append(station_data.station)
            info.Latitude.append(station_data.lat)
            info.Longitude.append(station_data.long)
            info.Elevation.append(station_data.elev)
            info.Brightness.append(station_data.brightness)

            count+=1
            if count%100==0:
                print(".",end="")
            if count%1000==0:
                print("O",end="")
        
        station_data=Struct()

        header=line.split()
        #print(header)
        station_data.ID=header[0]
        station_data.lat=float(header[1])
        station_data.long=float(header[2])
        station_data.elev=float(header[3])
        
        if station_data.elev==9999.0:
            station_data.elev=nan

        
        station_data.station=header[4]
        
        if header[5]=='*':
            station_data.brightness=nan
        else:
            station_data.brightness=int(header[5])
            
        assert (len(header)==6) or ((len(header)==7) and (header[5]=='*'))
    else:  # this is a line of data
        parts=line.split()
        year=int(parts[0])
        
        raw_temp=[int(part) for part in parts[1:]]
        
        T=[]
        for i,raw_T in enumerate(raw_temp):
            time=year+i/12  # change the month into a real number
            
            if raw_T==-9999:
                T.append(nan)
            else:
                T.append(raw_T/100)
            
            
            
            
        idx=where(time_arr==year)[0][0]
        temperature_arr[idx]=nanmean(T)
            
            
data[station_data.station]=temperature_arr

info.ID.append(station_data.ID)
info.Station.append(station_data.station)
info.Latitude.append(station_data.lat)
info.Longitude.append(station_data.long)
info.Elevation.append(station_data.elev)
info.Brightness.append(station_data.brightness)



print("done.")


# In[19]:


info=pd.DataFrame(info)
data=pd.DataFrame(data)


# In[20]:


info.head()


# In[21]:


data.tail()


# In[22]:


info.to_excel("data/station_info.xlsx")


# In[23]:


data.to_excel("data/station_temperature_data.xlsx")


# In[24]:


data.to_csv("data/station_temperature_data.csv.gz", compression='gzip')


# In[ ]:





# In[ ]:


data2=pd.read_csv("station_temperature_data.csv.gz",index_col=False)


# In[ ]:


data2.head()


# In[ ]:





# In[ ]:





# In[ ]:


plot(data2['time'],data2['SAVE'],'-o')


# In[ ]:




