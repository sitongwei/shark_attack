#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv 
from datetime import datetime, timedelta

sharkfile = r'c:\data\GSAF5.csv' 
# In[5]:


sharkfile = r'c:\data\GSAF5.csv'  


# In[9]:


attack_dates = []
case = [] 
country = [] 
activity = [] 
age = [] 
gender = [] 
isfatal = []
with open(sharkfile) as f:      
    reader = csv.DictReader(f)
    for row in reader: 
        case.append(row['Case Number'])
        attack_dates.append(row['Date'])
        country.append(row['Country']) 
        activity.append(row['Activity'])
        age.append(row['Age']) 
        gender.append(row['Sex '])
        isfatal.append(row['Fatal (Y/N)'])


# In[12]:


data = zip(attack_dates, case, country, activity, age, gender, isfatal)


# In[21]:


cur.execute('truncate table swshark') 


# In[14]:


import pyodbc 
conn = pyodbc.connect('DSN=kubricksql;UID=de14;PWD=password')
cur = conn.cursor()
q = 'insert into swshark(attack_dates, case, country, activity, age, gender, isfatal) values (?, ?, ?, ?, ?, ?, ?)'


# In[20]:


for d in range(0, len(case)): 
    if len(list(data)[1]) > 0: 
        try: 
            cur.execute(q, list(data)[d]) 
            conn.commit() 
        except: 
            conn.rollback()


# In[15]:


for d in zip(attack_dates, case, country, activity, age, gender, isfatal): 
    print(d) 


# In[ ]:





# In[34]:


attack_dates[:10]


# In[ ]:


# 1. initialise an empty list 
# 2. iterate through attack_dates list 
# 3. replace str instance of 'Reported' with '' empty string 
# 4. append into new list a datetime.strptime() version of cleansed date 


# In[40]:


l1 = [] 


# In[41]:


l1 = [attack_dates]


# In[46]:


print(attack_dates.replace('Reported', '', 1))


# In[47]:


from datetime import datetime, timedelta
date_time = [] 
with open(sharkfile) as f:       
    for row in reader: 
        attack_dates.append(row['Date'], strptime) 
        if reported in item: 
            y = y


# In[49]:


clean_dates=[] 
for d in attack_dates: 
    try: 
        clean_dates.append(datetime.strptime(d.replace('Reported ', ''), '%d-%b-%Y')) 
    except: 
        pass 


# In[51]:


clean_dates


# In[52]:


attack_dates.strftime('%A %d %b %Y')


# In[36]:


datecount = () 
for d in attack_dates: 
    datecount[d] = datecount.get(d, 0) +1


# In[37]:


sorted(datecount.items(), key=lambda x: x[1], reverse=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[26]:


f.close()


# In[27]:


dialect.quotechar 


# In[ ]:




