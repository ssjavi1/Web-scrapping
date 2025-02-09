#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import liabraries beautifulsoup for scrapping and selenium for automation
from selenium import webdriver
from bs4 import BeautifulSoup
import time


# In[3]:


#open driver
driver=webdriver.Chrome()


# In[4]:


#get url in driver
driver.get('https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')


# In[5]:


#run soup
soup=BeautifulSoup(driver.page_source,'html.parser')


# In[6]:


soup


# In[24]:


#extract the class of the category for which we want to scrap data
names='KzDlHZ'
price='Nx9bqj _4b5DiR'
ratings='XQDdHH'
specification='G4BRas'


# In[25]:


# find the container in which the class is present
laptop_names=soup.find_all('div',class_=names)
laptop_price=soup.find_all('div',class_=price)
laptop_ratings=soup.find_all('div',class_=ratings)
laptop_specification=soup.find_all('ul',class_=specification)


# In[9]:


laptop_names


# In[10]:


#making the list of all such categories
laptop_names_list=[]
for i in laptop_names:
    laptop_names_list.append(i.text)


# In[11]:


laptop_names_list


# In[12]:


laptop_price_list=[]
for i in laptop_price:
    laptop_price_list.append(i.text)


# In[13]:


laptop_price_list


# In[14]:


laptop_ratings_list=[]
for i in laptop_ratings:
    laptop_ratings_list.append(i.text)


# In[15]:


laptop_ratings_list


# In[22]:


laptop_specifications_list=[]
for i in laptop_specification:
    laptop_specifications_list.append(i.text)


# In[27]:


laptop_specifications_list


# In[26]:


laptop_specification


# In[28]:


driver.quit()


# In[ ]:




