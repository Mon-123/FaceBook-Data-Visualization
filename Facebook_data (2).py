#!/usr/bin/env python
# coding: utf-8

# ## Assignment - Facebook Data Analysis
# 
# The objective of the proposed framework is to study and analyse the differences in the way users
# are using Facebook based on their gender, age-group, etc. and Identify a pattern out of it.

# ### Loading important libraries

# In[1]:


import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


os.chdir('C:\\Users\\Monali\\OneDrive\\Desktop\\Case Study-DS\\Facebook')


# In[3]:


os.getcwd()


# ### Loading the Data

# In[4]:


FB = pd.read_excel('facebook user data.xlsx')


# In[5]:


FB.head()


# In[6]:


FB.shape


# In[7]:


FB.info()


# In[40]:


FB.describe()


# -Average age of facebook user is 37.
# -Users use web and mobile both to use facebook (Based on mobile_likes and web_likes Data)

# ### Missing Value analysis

# In[9]:


FB.isnull().sum()


# In[10]:


#Visualization of missing values with heatmap
sns.heatmap(FB.isnull(),yticklabels = False,cbar = True, cmap = "Blues",linecolor = "Black")


# ### Imputation of missing value
# 
# As the missing value is categorical, we will impute it with mode.

# In[11]:


FB['gender'].mode()


# In[13]:


FB['gender'] = FB['gender'].fillna(FB['gender'].mode()[0])


# Although for 'Tenure' mean or median can be used based on data distribution.
# If data is screwed median should be used else it can be imputed with mean.
# There are 2 missing values in 'Tenure', which can be dropped as it contributes only 0.001 of total data.

# In[14]:


FB.dropna(subset = ['tenure'], inplace = True)


# In[15]:


FB['gender'].isnull().sum()


# ### Data Visualization

# In[16]:


sns.pairplot(FB, hue = 'gender')


# In[17]:


plt.rcParams.update({'font.size': 12})
sns.set_style("whitegrid")
FB.hist(bins=40, figsize=(30, 30));


# In[18]:


FB['gender'].value_counts()


# In[19]:


plt.hist(FB['gender'])


# ### HeatMap/correlation

# In[20]:


f, ax = plt.subplots(figsize = (20,10))
sns.heatmap(FB.corr(),annot = True)


# There is high co-relation between Likes_recieved and www_likes_received and mobile_likes_received and www_likes_received,
# which dipicts these variables are carrying same information and maybe dropped while model creation.

# ## Analysis based on number of users

# #### Composition of male and female users

# In[21]:


plt.figure(figsize=(7,5))
g = sns.countplot(FB.gender, palette="pastel");
plt.title("Gender Distribution")
plt.xlabel("gender")
plt.ylabel("population count")
plt.show()


# In[22]:


plt.figure(figsize=(12,6))
plt.title("Gender distribution")
g = plt.pie(FB.gender.value_counts(), explode=(0.025,0.025), labels=FB.gender.value_counts().index, colors=['skyblue','navajowhite'],autopct='%1.1f%%', startangle=180);
plt.legend()
plt.show()


# The polpulation of male user is more than female users which singly constitues 59.3% of whole population.

# #### Friends Count based on gender

# In[23]:


#Females have more friends than males
sns.barplot(x=FB['gender'],y=FB['friend_count'])


# #### Friends_initiated based on gender

# In[24]:


#Females have inititaed more friendships than males
sns.barplot(x=FB['gender'],y=FB['friendships_initiated'])


# #### Distribution of tenure across different categories of gender 

# The tenure is converted in labels such as 1-2 years, 2-3 years.....
# The new column is added named 'Year_group'.

# In[25]:


tenlabel=['0-1','1-2','2-3','3-4','4-5','5-6','6-7','7-8','8-9']
FB['year_group']=pd.cut(FB.tenure,bins=np.arange(0,3300,365),labels=tenlabel,right=True)


# In[26]:


FB


# In[27]:


sns.barplot(x=FB['year_group'],y=FB['age'],hue = FB.gender)


# In[28]:


sns.barplot(x=FB['gender'],y=FB['tenure'])


# ## Analysis based on least active users on facebook

# #### Users having no friends

# In[29]:


fc=FB.friend_count==0
fc.value_counts()


# 1962 people have 0 friends.

# #### Users who didn't like any post

# In[30]:


Pc=FB.likes==0
Pc.value_counts()


# 22308 people didn't like any post

# #### Users who didn't received any likes

# In[31]:


No_likes_received=FB.likes_received==0
No_likes_received.value_counts()


# 24428 people didn't receive any likes from others.

# ## Analysis based on accessibility 

# #### Average number of post liked by user based on gender through web vs mobile devices

# In[32]:


FB[FB['gender']=='male']['mobile_likes'].mean()


# In[33]:


FB[FB['gender']=='female']['mobile_likes'].mean()


# In[34]:


FB[FB['gender']=='male']['www_likes'].mean()


# In[35]:


FB[FB['gender']=='female']['www_likes'].mean()


# #### Average number of likes received by user based on gender through web vs mobile devices

# In[36]:


FB[FB['gender']=='male']['mobile_likes_received'].mean()


# In[37]:


FB[FB['gender']=='female']['mobile_likes_received'].mean()


# In[38]:


FB[FB['gender']=='male']['www_likes_received'].mean()


# In[39]:


FB[FB['gender']=='female']['www_likes_received'].mean()


# In[ ]:




