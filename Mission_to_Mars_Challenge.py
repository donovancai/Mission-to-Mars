#!/usr/bin/env python
# coding: utf-8

# In[35]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[16]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[17]:


url = "https://redplanetscience.com"
browser.visit(url)
#optional delay
browser.is_element_present_by_css('div.list_txt', wait_time=1)


# In[18]:


html = browser.html
news_soup = soup(html,'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[24]:


news_title = slide_elem.find('div',class_='content_title').get_text()
news_title


# In[25]:


news_p = slide_elem.find('div',class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[26]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[28]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[31]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[33]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[34]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[36]:


df = pd.read_html('https://galaxyfacts-mars.com/')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[37]:


df.to_html()


# In[39]:


browser.quit()


# In[ ]:





# # Starter Code

# In[54]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[59]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[4]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[ ]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[ ]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[ ]:


slide_elem.find('div', class_='content_title')


# In[ ]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[ ]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[ ]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[ ]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[ ]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[ ]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[ ]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[ ]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[ ]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[ ]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[71]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[72]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)


# In[73]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[74]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

# click on thumbnail
for i in range(0,4):
    # hemispheres dictionary
    hemispheres = {}
        
    browser.find_by_tag('h3')[i].click()

    # find the image text
    anchor = browser.find_by_text('Sample')
    
    # get title
    title = browser.find_by_tag('h2').text

    # update dictionary
    hemispheres["img_url"] = anchor['href']
    hemispheres["title"] = title

    # append to list
    hemisphere_image_urls.append(hemispheres)

    browser.back()
    


# In[75]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[76]:


# 5. Quit the browser
browser.quit()


# In[ ]:




