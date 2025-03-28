#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


data=pd.read_csv("fake_news.csv")
data.head()


# In[5]:


data.shape


# In[6]:


data.info()


# In[7]:


data.isna().sum()


# In[8]:


data=data.drop(['id'],axis=1)


# In[9]:


data=data.fillna('')


# In[10]:


data['content']=data['author']+' '+data['title']+' '+data['text']


# In[12]:


data=data.drop(['title','author','text'],axis=1)


# In[13]:


data.head()


# In[14]:


data['content']=data['content'].apply(lambda x:" ".join(x.lower() for x in x.split()))


# In[15]:


data['content']=data['content'].str.replace('[\w\s]','')


# In[16]:


import nltk
nltk.download('stopwords')


# In[18]:


from nltk.corpus import stopwords
stop=stopwords.words('english')
data['content']=data['content'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))


# In[26]:


get_ipython().system('pip install textblob')


# In[27]:


from nltk.stem import WordNetLemmatizer
from textblob import Word
data['content']=data['content'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
data['content'].head()


# In[24]:


x=data['content']
y=data['label']


# In[28]:


from sklearn.model_selection import train_test_split


# In[32]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=45,stratify=y)


# In[34]:


print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)


# In[35]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[ ]:


tfidf_vect=TfidfVectorizer(analyzer='word',token_pattern=r'\w{1,}',max_features=5000)
tfidf_vect.fit(data['content'])
xtrain_tfidf=tfidf_vect.transform(x_train['content'])
xtest_tfidf=tfidf_vect.transform(x_test['content'])


# In[ ]:




