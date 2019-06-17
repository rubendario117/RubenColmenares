#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
from datetime import datetime
import requests
import os
import time


# # Scrap NASA News:

# In[2]:


url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
response = requests.get(url)


# In[3]:


#Beautiful Soup Object
soup = bs(response.text, 'html5')
type(soup)


# In[6]:


#Let's check the class and print to check if the scrape was succesful:
news_title = soup.find_all('div', class_='content_title')[0].find('a').text.strip()
#print(news_title)
news_p = news_p = soup.find_all('div', class_='rollover_description_inner')[0].text.strip()
print(news_p)


# # JPL Mars Space Images - Featured Image

# In[7]:


# We'll use Chromedriver
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[8]:


image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(image_url)


# In[10]:


#Now let's create a BS Object:
html = browser.html
soup_image = bs(html, 'html5')
type(soup_image)


# In[11]:


#We will obtain the image address
address = soup_image.find_all('a', class_='fancybox')[0].get('data-fancybox-href').strip()
print(address)


# In[13]:


#Now let's build the final image url:
featured_image_url = "https://www.jpl.nasa.gov" + address
print(featured_image_url)


# # Mars Weather

# In[15]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[16]:


#NASA Tweeter Account. Let's Scrape it
url_tweet = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url_tweet)


# In[17]:


#Let's get info 
html = browser.html
soup_tweet = bs(html, "html5")

mars_weather = soup_tweet.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')[0].text

#Tweet Check
print(mars_weather)


# # Mars Facts

# In[26]:


url_facts = 'https://space-facts.com/mars/'

mars_list = pd.read_html(url_facts)
mars_list


# In[27]:


mars_df = mars_list[0]
mars_df.columns=['description','value']

mars_df.head()


# In[28]:


#We will set the 'description' column as our Index:
mars_df.set_index('description', inplace=True)
mars_df.head()


# In[23]:


#Use Pandas to convert the data to a HTML table string.
mars_df.to_html('mars_facts.html')


# # Mars Hemispheres

# In[32]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

url_hem = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

browser.visit(url_hem)

html = browser.html
soup_hem = bs(html,"html5")

type(soup)


# In[38]:


#Create blank list and dictionary:
hemisphere_image_urls = []
dict = {}

#Now let's obtain all titles:
results = soup_hem.find_all('h3')
results


# In[37]:


#Loop for getting results:
for result in results:
    text_hem = result.text
    time.sleep(1)    
    browser.click_link_by_partial_text(text_hem)
    time.sleep(1)
    
    # Create a Beautiful Soup object
    html_loop = browser.html
    soup_loop = bs(html_loop,"html5")
    time.sleep(1)
    # Grab the image link
    url_loop = soup_loop.find_all('div', class_="downloads")[0].find_all('a')[0].get("href")
    # Pass title to Dict
    time.sleep(1)
    dict["title"]=text_hem
    # Pass url to Dict
    dict["img_url"]=url_loop
    # Append Dict to the list 
    hemisphere_image_urls.append(dict)
    # Clean Up Dict
    dict = {}
    browser.click_link_by_partial_text('Back')
    time.sleep(1)
    
hemisphere_image_urls


# In[ ]:




