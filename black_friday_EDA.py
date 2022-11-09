#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df_train=pd.read_csv('train.csv')
df_train.head()


# In[4]:


df_test=pd.read_csv('test.csv')
df_test.head()


# In[5]:


df=df_train.append(df_test)
df.head()


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


df.drop(['User_ID'],axis=1,inplace=True)


# In[9]:


df.head()


# In[10]:


df['Gender']=pd.get_dummies(df['Gender'],drop_first=1)


# In[11]:


df['Gender']=df['Gender'].map({'F':0,'M':1})
df.head()


# In[12]:


df['Age'].unique()


# In[13]:


df['Age']=df['Age'].map({'0-17':1,'18-25':2,'26-35':3,'36-45':4,'46-50':5,'51-55':6,'55+':7})


# In[14]:


df.head()


# In[15]:


df_city=pd.get_dummies(df['City_Category'],drop_first=True)


# In[16]:


df=pd.concat([df,df_city],axis=1)
df.head()


# In[17]:


df.drop('City_Category',axis=1,inplace=True)


# In[18]:


df.isnull().sum()


# In[19]:


df['Product_Category_2'].unique()


# In[20]:


df['Product_Category_2'].value_counts()


# In[21]:


df['Product_Category_2']=df['Product_Category_2'].fillna(df['Product_Category_2'].mode()[0])


# In[22]:


df['Product_Category_2'].isnull().sum()


# In[23]:


df['Product_Category_3'].unique()


# In[24]:


df['Product_Category_3'].value_counts()


# In[25]:


df['Product_Category_3']=df['Product_Category_3'].fillna(df['Product_Category_3'].mode()[0])


# In[26]:


df.head()


# In[27]:


df.shape


# In[28]:


df['Stay_In_Current_City_Years'].unique()


# In[29]:


df['Stay_In_Current_City_Years']=df['Stay_In_Current_City_Years'].str.replace('+','')


# In[30]:


df['Stay_In_Current_City_Years']=df['Stay_In_Current_City_Years'].astype(int)
df.info()


# In[31]:


df['B']=df['B'].astype(int)
df['C']=df['C'].astype(int)


# In[34]:


sns.barplot('Age','Purchase',hue='Gender',data=df)


# In[35]:


df


# In[ ]:




