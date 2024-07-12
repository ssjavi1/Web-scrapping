#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import liabraries beautifulsoup for scrapping and selenium for automation
from selenium import webdriver
from bs4 import BeautifulSoup
import time


# In[2]:


#open driver
driver=webdriver.Chrome()


# In[3]:


#get url in driver
driver.get('https://www.naukri.com/data-analyst-jobs-in-pune?k=data%20analyst&l=pune&experience=0&nignbevent_src=jobsearchDeskGNB')


# In[4]:


#run soup
soup=BeautifulSoup(driver.page_source,'html.parser')


# In[5]:


soup


# In[22]:


#extract the class of the category for which we want to scrap data
job_title='row1'


# In[23]:


# find the container in which the class is present
job_titles=soup.find_all('div',class_=job_title)


# In[24]:


job_titles


# In[26]:


#making the list of all such categories
job_titles_list=[]
for i in job_titles:
    job_titles_list.append(i.text)


# In[27]:


job_titles_list


# In[34]:


company_name='comp-name mw-25'


# In[37]:


company_names=soup.find_all('a',class_=company_name)


# In[38]:


company_names


# In[39]:


company_names_list=[]
for i in company_names:
    company_names_list.append(i.text)


# In[40]:


company_names_list


# In[41]:


rating='rating'


# In[42]:


ratings=soup.find_all('a',class_=rating)


# In[43]:


ratings


# In[44]:


ratings_list=[]
for i in ratings:
    ratings_list.append(i.text)


# In[45]:


ratings_list


# In[46]:


location='locWdth'


# In[49]:


locations=soup.find_all('span',class_=location)


# In[50]:


locations


# In[51]:


locations_list=[]
for i in locations:
    locations_list.append(i.text)


# In[52]:


locations_list


# In[53]:


job_desc='job-desc ni-job-tuple-icon ni-job-tuple-icon-srp-description'


# In[54]:


job_description=soup.find_all('span',class_=job_desc)


# In[55]:


job_description


# In[56]:


JD_list=[]
for i in job_description:
    JD_list.append(i.text)


# In[57]:


JD_list


# In[58]:


driver.quit()


# In[ ]:




