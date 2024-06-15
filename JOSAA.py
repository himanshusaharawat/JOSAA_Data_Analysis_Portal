#!/usr/bin/env python
# coding: utf-8

# EDA for josaa data analysis portal

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("C:\\Users\hp\Downloads\data.csv")


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.dtypes


# In[6]:


df.isna().sum()


# In[7]:


df.dropna(subset=['Opening Rank','Closing Rank'], inplace=True)


# In[8]:


df.isna().sum()


# In[9]:


df['Opening Rank'] = df['Opening Rank'].astype(int)
df['Closing Rank'] = df['Closing Rank'].astype(int)


# In[10]:


df.dtypes


# In[11]:


df.head()


# In[12]:


df.drop(columns = ['Has_P' , 'Round'], inplace=True) 


# In[13]:


df['Gender'].unique()


# In[14]:


df = df[df['Gender']!='Female-only (including Supernumerary)']


# In[15]:


df.shape


# In[16]:


df.drop(columns=['Gender'], inplace = True)


# In[17]:


df.head()


# In[18]:


df['Seat Type'].unique()


# In[19]:


df['Academic Program Name'].unique()


# In[20]:


df = df[df['Academic Program Name'].isin(['Civil Engineering (4 Years, Bachelor of Technology)',
                                         'Computer Science and Engineering (4 Years, Bachelor of Technology)',
                                         'Electrical Engineering (4 Years, Bachelor of Technology)',
                                         'Electronics and Communication Engineering (4 Years, Bachelor of Technology)',
                                         'Mechanical Engineering (4 Years, Bachelor of Technology)',
                                         'Metallurgical and Materials Engineering (4 Years, Bachelor of Technology)',
                                         'Aerospace Engineering (4 Years, Bachelor of Technology)',
                                         'Chemical Engineering (4 Years, Bachelor of Technology)',
                                         'Chemistry (4 Years, Bachelor of Science)',
                                         'Engineering Physics (4 Years, Bachelor of Technology)',
                                         'Metallurgical Engineering and Materials Science (4 Years, Bachelor of Technology)',
                                         'Biotechnology and Biochemical Engineering (4 Years, Bachelor of Technology)',
                                         'Electrical Engineering (Power and Automation) (4 Years, Bachelor of Technology)',
                                         'Mathematics and Computing (4 Years, Bachelor of Technology)',
                                         'Production and Industrial Engineering (4 Years, Bachelor of Technology)',
                                         'Textile Technology (4 Years, Bachelor of Technology)',
                                         'Agricultural and Food Engineering (4 Years, Bachelor of Technology)',
                                         'Electronics and Electrical Communication Engineering (4 Years, Bachelor of Technology)',
                                         'Mining Engineering (4 Years, Bachelor of Technology)',
                                         'Economics (4 Years, Bachelor of Science)',
                                         'Materials Science and Engineering (4 Years, Bachelor of Technology)',
                                         'Bio Technology (4 Years, Bachelor of Technology)',
                                         'Chemical Science and Technology (4 Years, Bachelor of Technology)',
                                         'Electronics and Electrical Engineering (4 Years, Bachelor of Technology)', 
                                         'Data Science and Artificial Intelligence (4 Years, Bachelor of Technology)',
                                         ])]


# In[21]:


df['Institute'].unique()


# In[22]:


df.shape


# In[23]:


Institute_1 = df[(df['Institute'] == 'Indian Institute of Technology Bhubaneswar') & (df['Seat Type']=='OPEN')]


# In[24]:


Institute_2 = df[(df['Institute'] == 'Indian Institute of Technology Bombay') & (df['Seat Type']=='OPEN')]


# In[25]:


Institute_3 = df[(df['Institute'] == 'Indian Institute of Technology Mandi') & (df['Seat Type']=='OPEN')]


# In[26]:


Institute_4 = df[(df['Institute'] == 'Indian Institute of Technology Delhi') & (df['Seat Type']=='OPEN')]


# In[27]:


Institute_5 = df[(df['Institute'] == 'Indian Institute of Technology Indore') & (df['Seat Type']=='OPEN')]


# In[28]:


Institute_6 = df[(df['Institute'] == 'Indian Institute of Technology Kharagpur') & (df['Seat Type']=='OPEN')]


# In[29]:


Institute_7 = df[(df['Institute'] == 'Indian Institute of Technology Hyderabad') & (df['Seat Type']=='OPEN')]


# In[30]:


Institute_8 = df[(df['Institute'] == 'Indian Institute of Technology Jodhpur') & (df['Seat Type']=='OPEN')]


# In[31]:


Institute_9 = df[(df['Institute'] == 'Indian Institute of Technology Kanpur') & (df['Seat Type']=='OPEN')]


# In[32]:


Institute_10 = df[(df['Institute'] == 'Indian Institute of Technology Madras') & (df['Seat Type']=='OPEN')]


# In[33]:


Institute_11 = df[(df['Institute'] == 'Indian Institute of Technology Gandhinagar') & (df['Seat Type']=='OPEN')]


# In[34]:


Institute_12 = df[(df['Institute'] == 'Indian Institute of Technology Patna') & (df['Seat Type']=='OPEN')]


# In[35]:


Institute_13 = df[(df['Institute'] == 'Indian Institute of Technology Roorkee') & (df['Seat Type']=='OPEN')]


# In[36]:


Institute_14 = df[(df['Institute'] == 'Indian Institute of Technology (ISM) Dhanbad') & (df['Seat Type']=='OPEN')]


# In[37]:


Institute_15 = df[(df['Institute'] == 'Indian Institute of Technology Ropar') & (df['Seat Type']=='OPEN')]


# In[38]:


Institute_16 = df[(df['Institute'] == 'Indian Institute of Technology (BHU) Varanasi') & (df['Seat Type']=='OPEN')]


# In[39]:


Institute_17 = df[(df['Institute'] == 'Indian Institute of Technology Guwahati') & (df['Seat Type']=='OPEN')]


# In[40]:


Institute_18 = df[(df['Institute'] == 'Indian Institute of Technology Bhilai') & (df['Seat Type']=='OPEN')]


# In[41]:


Institute_19 = df[(df['Institute'] == 'Indian Institute of Technology Goa') & (df['Seat Type']=='OPEN')]


# In[42]:


Institute_20 = df[(df['Institute'] == 'Indian Institute of Technology Palakkad') & (df['Seat Type']=='OPEN')]


# In[43]:


Institute_21 = df[(df['Institute'] == 'Indian Institute of Technology Tirupati') & (df['Seat Type']=='OPEN')]


# In[44]:


Institute_22 = df[(df['Institute'] == 'Indian Institute of Technology Jammu') & (df['Seat Type']=='OPEN')]


# In[45]:


Institute_23 = df[(df['Institute'] == 'Indian Institute of Technology Dharwad') & (df['Seat Type']=='OPEN')]


# In[46]:


print(Institute_1)


# In[47]:


import plotly.express as px
import plotly.io as pio


# In[48]:


fig = px.line(Institute_1, x='Year',y='Closing Rank', color="Academic Program Name",labels={'x': 'Year', 'y': 'Closing Rank'}, title='IIT Bhubaneswar',markers =True)
fig.update_layout(
    width=1200, 
    height=600  
)
fig.show()


# In[49]:


fig = px.line(Institute_2, x='Year',y='Closing Rank', color="Academic Program Name",labels={'x': 'Year', 'y': 'Closing Rank'}, title='IIT Bombay',markers =True)
fig.update_layout(
    width=1200, 
    height=600  
)
fig.show()


# In[50]:


fig = px.line(Institute_3, x='Year',y='Closing Rank', color="Academic Program Name",labels={'x': 'Year', 'y': 'Closing Rank'}, title='IIT Mandi',markers =True)
fig.update_layout(
    width=1200, 
    height=600  
)
fig.show()


# In[51]:


fig = px.line(Institute_4, x='Year',y='Closing Rank', color="Academic Program Name",labels={'x': 'Year', 'y': 'Closing Rank'}, title='IIT Delhi',markers =True)
fig.update_layout(
    width=1200, 
    height=600  
)
fig.show()


# In[52]:


fig = px.line(Institute_5, x='Year',y='Closing Rank', color="Academic Program Name",labels={'x': 'Year', 'y': 'Closing Rank'}, title='IIT Indore',markers =True)
fig.update_layout(
    width=1200, 
    height=600  
)
fig.show()


# In[53]:


fig = px.line(Institute_6, x='Year',y='Closing Rank', color="Academic Program Name",labels={'x': 'Year', 'y': 'Closing Rank'}, title='IIT Kharagpur',markers =True)
fig.update_layout(
    width=1200, 
    height=600  
)
fig.show()


# In[54]:


fig = px.line(Institute_7, x='Year',y='Closing Rank', color="Academic Program Name",labels={'x': 'Year', 'y': 'Closing Rank'}, title='IIT Hyderabad',markers =True)
fig.update_layout(
    width=1200, 
    height=600  
)
fig.show()


# In[55]:


fig = px.line(Institute_8, x='Year',y='Closing Rank', color="Academic Program Name",labels={'x': 'Year', 'y': 'Closing Rank'}, title='IIT Jodhpur',markers =True)
fig.update_layout(
    width=1200, 
    height=600  
)
fig.show()


# In[56]:


fig = px.line(Institute_9, x='Year',y='Closing Rank', color="Academic Program Name",labels={'x': 'Year', 'y': 'Closing Rank'}, title='IIT Kanpur',markers =True)
fig.update_layout(
    width=1200, 
    height=600  
)
fig.show()


# In[57]:


fig = px.line(Institute_10, x='Year',y='Closing Rank', color="Academic Program Name",labels={'x': 'Year', 'y': 'Closing Rank'}, title='IIT Madras',markers =True)
fig.update_layout(
    width=1200, 
    height=600  
)
fig.show()


# In[58]:


fig = px.line(Institute_11, x='Year',y='Closing Rank', color="Academic Program Name",labels={'x': 'Year', 'y': 'Closing Rank'}, title='IIT Gandhinagar',markers =True)
fig.update_layout(
    width=1200, 
    height=600  
)
fig.show()


# In[59]:


fig = px.line(Institute_12, x='Year',y='Closing Rank', color="Academic Program Name",labels={'x': 'Year', 'y': 'Closing Rank'}, title='IIT Patna',markers =True)
fig.update_layout(
    width=1200, 
    height=600  
)
fig.show()


# In[60]:


fig = px.line(Institute_13, x='Year',y='Closing Rank', color="Academic Program Name",labels={'x': 'Year', 'y': 'Closing Rank'}, title='IIT Roorkee',markers =True)
fig.update_layout(
    width=1200, 
    height=600  
)
fig.show()


# In[61]:


fig = px.line(Institute_14, x='Year',y='Closing Rank', color="Academic Program Name",labels={'x': 'Year', 'y': 'Closing Rank'}, title='IIT(ISM) Dhanbad ',markers =True)
fig.update_layout(
    width=1200, 
    height=600  
)
fig.show()


# In[62]:


fig = px.line(Institute_15, x='Year',y='Closing Rank', color="Academic Program Name",labels={'x': 'Year', 'y': 'Closing Rank'}, title='IIT Ropar',markers =True)
fig.update_layout(
    width=1200, 
    height=600  
)
fig.show()


# In[63]:


fig = px.line(Institute_16, x='Year',y='Closing Rank', color="Academic Program Name",labels={'x': 'Year', 'y': 'Closing Rank'}, title='IIT(BHU) Varanasi',markers =True)
fig.update_layout(
    width=1200, 
    height=600  
)
fig.show()


# In[64]:


fig = px.line(Institute_17, x='Year',y='Closing Rank', color="Academic Program Name",labels={'x': 'Year', 'y': 'Closing Rank'}, title='IIT Guwahati',markers =True)
fig.update_layout(
    width=1200, 
    height=600  
)
fig.show()


# In[65]:


fig = px.line(Institute_18, x='Year',y='Closing Rank', color="Academic Program Name",labels={'x': 'Year', 'y': 'Closing Rank'}, title='IIT Bhilai',markers =True)
fig.update_layout(
    width=1200, 
    height=600  
)
fig.show()


# In[66]:


fig = px.line(Institute_19, x='Year',y='Closing Rank', color="Academic Program Name",labels={'x': 'Year', 'y': 'Closing Rank'}, title='IIT Goa',markers =True)
fig.update_layout(
    width=1200, 
    height=600  
)
fig.show()


# In[67]:


fig = px.line(Institute_20, x='Year',y='Closing Rank', color="Academic Program Name",labels={'x': 'Year', 'y': 'Closing Rank'}, title='IIT Palakkad',markers =True)
fig.update_layout(
    width=1200, 
    height=600  
)
fig.show()


# In[68]:


fig = px.line(Institute_21, x='Year',y='Closing Rank', color="Academic Program Name",labels={'x': 'Year', 'y': 'Closing Rank'}, title='IIT Tirupati',markers =True)
fig.update_layout(
    width=1200, 
    height=600  
)
fig.show()


# In[69]:


fig = px.line(Institute_22, x='Year',y='Closing Rank', color="Academic Program Name",labels={'x': 'Year', 'y': 'Closing Rank'}, title='IIT Jammu',markers =True)
fig.update_layout(
    width=1200, 
    height=600  
)
fig.show()


# In[70]:


fig = px.line(Institute_23, x='Year',y='Closing Rank', color="Academic Program Name",labels={'x': 'Year', 'y': 'Closing Rank'}, title='IIT Dharwad',markers =True)
fig.update_layout(
    width=1200, 
    height=600  
)
fig.show()


# In[ ]:




