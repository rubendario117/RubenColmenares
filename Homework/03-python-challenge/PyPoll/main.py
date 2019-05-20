#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sys


# In[2]:


#Defino path del archivo
csv_path = "C:/Users/Ruben D. Colmenares/Documents/TEC/Data Bootcamp/Github Repository/RubenColmenares/python-challenge/PyPoll/election_data.csv"


# In[3]:


#Abro el archivo con Pandas
election_pd = pd.read_csv(csv_path)
election_pd.head()


# In[4]:


election_pd.describe()


# In[5]:


#count votes
votes = election_pd["Voter ID"].size
votes


# In[6]:


candidates = election_pd["Candidate"].value_counts()
candidates


# In[7]:


candidates
results_table = pd.DataFrame(candidates)

results_table


# In[8]:


#Format into %
percentages = results_table["Candidate"]/votes*100
results_table["Votes(%)"] = percentages

results_table.style.format({
    'Candidate': '{:,.2f}'.format,
    'Votes(%)': '{:,.2%}'.format,
})


results_table


# In[9]:


winner = max(results_table["Candidate"])
winner


# In[10]:


results_table["Candidate"]==winner


# In[11]:


results_table.loc[results_table["Candidate"]==winner,:]


# In[12]:


results_table.index[results_table["Candidate"]==winner]


# In[13]:


winner_candidate = list(results_table.index[results_table["Candidate"]==winner])
winner_candidate


# In[14]:


#Final Print

#sys.stdout=open("main_output.txt","w")
print("Election Results: \n")
print("--------------------------- \n")
print("Total Votes: " + str(votes))
print("--------------------------- \n")
print(results_table)
print("--------------------------- \n")
print("Winner" + str(winner_candidate))
#sys.stdout.close()


# In[ ]:


sys.stdout=open("main_output.txt","w")
print("Election Results: \n")
print("--------------------------- \n")
print("Total Votes: " + str(votes))
print("--------------------------- \n")
print(results_table)
print("--------------------------- \n")
print("Winner" + str(winner_candidate))
sys.stdout.close()


# In[ ]:




