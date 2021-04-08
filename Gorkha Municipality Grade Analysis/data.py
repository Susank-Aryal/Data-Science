#!/usr/bin/env python
# coding: utf-8

# In[23]:


from tabula import read_pdf
from tabula import convert_into
from tabulate import tabulate

get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np

import plotly.graph_objects as go
import plotly.express as px


# In[2]:


raw_data = read_pdf("2074.pdf",pages = 'all', lattice=True, multiple_tables = 'True')


# In[3]:


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# In[4]:


data = raw_data[:-1]
data = pd.concat(data, ignore_index = True)
data.columns = data.loc[0] 
data= data.drop([0])
data = data[['Symbol No','Name of Stundent', 'Nepali', 'English','Maths','Science','Sostd','Hpy','Moral','OBT','Lsub.','GPA']]


# In[5]:


del_index = (data[data['GPA']=='GPA'].index.values)
data['GPA'] = data['GPA'].fillna(0)
for d in del_index:
    data = data.drop([d])
data = data.reset_index(drop = True)
data


# In[6]:


d2 = raw_data[-1:] 
d2 = d2[0]
# d2.columns = d2.loc[0] 
d2= d2.drop([0])
list = ['Symbol No','Name of Stundent', 'Nepali', 'English','Maths','Science','Sostd','Hpy','Moral','OBT','Lsub.','GPA']
d2 = d2[:-1]
d2 = d2.dropna(axis = 1)
del d2[0]
d2.columns = list
d2


# In[7]:


data_df = data.append(d2, sort=False)
data_df.reset_index(drop = True)
# data = data[['Symbol No','Name of Stundent', 'Nepali', 'English','Maths','Science','Sostd','Hpy','Moral','OBT','Lsub.','GPA']]


# In[8]:


data_df['GPA'] = data_df['GPA'].astype('f') 
data_df[data_df['GPA']<=0] 


# In[9]:


school_code_df = read_pdf("2074 grade.pdf",pages = 'all', lattice=True, multiple_tables = 'True')
school_code_df = pd.concat(school_code_df,ignore_index = True)
school_code_df = school_code_df.drop([0])
school_code_df = school_code_df.fillna(0)


# In[10]:


school_code_df = school_code_df[[2,4]]
school_code_df = school_code_df[school_code_df[2]!= 0]
school_code_df['School Code'] = school_code_df[[2]]
school_code_df['Symbol No'] = school_code_df[[4]]


# In[11]:


del school_code_df[2]
del school_code_df[4]
school_code_df.reset_index(drop = True)


# In[12]:


data_df['Nepali'] = data_df['Nepali'].astype('f') 
data_df['English'] = data_df['English'].astype('f') 
data_df['Maths'] = data_df['Maths'].astype('f') 
data_df['Science'] = data_df['Science'].astype('f') 
data_df['Sostd'] = data_df['Sostd'].astype('f') 
data_df['Hpy'] = data_df['Hpy'].astype('f') 
data_df['Moral'] = data_df['Moral'].astype('f') 
data_df['OBT'] = data_df['OBT'].astype('f') 
data_df['Lsub.'] = data_df['Lsub.'].astype('f') 

data_df = pd.merge(data_df, school_code_df, on = 'Symbol No')
data_df


# In[17]:


# fig = px.histogram(data_df, x="GPA", nbins = 50)
# fig.show()


# In[22]:


# data_df['School Code'].unique()


# In[ ]:




