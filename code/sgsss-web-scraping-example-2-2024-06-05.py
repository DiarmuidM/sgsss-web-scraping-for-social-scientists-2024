#!/usr/bin/env python
# coding: utf-8

# # Web scraping for social scientists: Example 2

# ## Introduction
# 
# Computational methods for collecting, cleaning and analysing data are an increasingly important component of a social scientist’s toolkit. Central to engaging in these methods is the ability to write readable and effective code using a programming language.
# 
# In this lesson we apply the logic of web scraping to more sophisticated, genuine websites.

# ### Aims
# 
# This lesson has two aims:
# 1. Demonstrate how to use Python to collect data found on more complicated, realistic websites.
# 2. Cultivate your computational thinking skills through coding examples. In particular, how to define and solve a data collection problem using a computational method.

# ### Lesson details
# 
# * **Level**: Introductory
# * **Time**: 40-60 minutes
# * **Pre-requisites**: [Example 1](https://github.com/DiarmuidM/ncrm-web-scraping-for-social-scientists-2023/blob/main/code/ncrm-web-scraping-example-1-2023-06-06.ipynb)
# * **Audience**: Researchers and analysts from any disciplinary background
# * **Learning outcomes**:
#     1. Understand the key steps and requirements for collecting data from web pages using computational methods.
#     2. Be able to use Python for requesting, parsing, extracting and saving data stored on a web page.

# ## Guide to using this resource
# 
# This learning resource was built using <a href="https://jupyter.org/" target=_blank>Jupyter Notebook</a>, an open-source software application that allows you to mix code, results and narrative in a single document. As <a href="https://jupyter4edu.github.io/jupyter-edu-book/" target=_blank>Barba et al. (2019)</a> espouse:
# > In a world where every subject matter can have a data-supported treatment, where computational devices are omnipresent and pervasive, the union of natural language and computation creates compelling communication and learning opportunities.
# 
# If you are familiar with Jupyter notebooks then skip ahead to the main content (*What is web-scraping?*). Otherwise, the following is a quick guide to navigating and interacting with the notebook.

# ### Interaction
# 
# **You only need to execute the code that is contained in sections which are marked by `In []`.**
# 
# To execute a cell, click or double-click the cell and press the `Run` button on the top toolbar (you can also use the keyboard shortcut Shift + Enter).
# 
# Try it for yourself:

# In[ ]:


print("Enter your name and press enter:")
name = input()
print("\r")
print("Hello {}, enjoy learning more about Python and web-scraping!".format(name))


# ### Learn more
# 
# Jupyter notebooks provide rich, flexible features for conducting and documenting your data analysis workflow. To learn more about additional notebook features, we recommend working through some of the <a href="https://github.com/darribas/gds19/blob/master/content/labs/lab_00.ipynb" target=_blank>materials</a> provided by Dani Arribas-Bel at the University of Liverpool. 

# ## City of Edinburgh Council

# Python script for collecting, parsing and saving organisation data from: 
# * https://www.edinburgh.gov.uk/directory/10258/other-warm-and-welcoming-locations
# * https://www.edinburgh.gov.uk/directory/10199/library-locations-and-opening-hours
# * https://www.edinburgh.gov.uk/cost-living/food-bank-information

# ### Preliminaries

# In[ ]:


# Modules

import string # module for working with ASCII and other strings
import os # module for navigating your machine (e.g., file directories)
import requests # module for requesting urls
import json # module for working with JSON data structures
import csv # module for working with csv files
import pandas as pd  # module for working with dataframes
from datetime import datetime as dt # module for working with dates and time
from bs4 import BeautifulSoup as soup # module for parsing web pages


# In[ ]:


# Filepaths

other_data = "./data/"
la_data = "./data/local-authorities/"


# In[ ]:


# Create data folders

for folder in other_data, la_data:
    try:
        os.mkdir(folder)
    except:
        print("Unable to create {}: already exists".format(folder))


# In[ ]:


# Download date

ddate = dt.now().strftime("%Y-%m-%d")
ddate


# ### Libraries

# In[ ]:


header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
base = "https://www.edinburgh.gov.uk/directory/10199/a-to-z/"
abc = list(string.ascii_uppercase)

org_list = []
    
for l in abc:
    url = base + str(l)
    print(url)
    response = requests.get(url, headers=header) # request the web address
    
    if response.status_code==200:
        orgs = soup(response.text, "html.parser")
        try:
            results = orgs.find("ul", class_="list list--record").find_all("li")
            for el in results:
                name = el.find("a").text
                link = el.find("a").get("href")
                obs = {"org_name": name, "org_url": link}
                #print(obs)
                org_list.append(obs)
        except:
             print("Could not find list of organisations")
            
#print(response.text)


# #### Specific libraries

# In[ ]:


len(org_list)


# In[ ]:


org_list


# In[ ]:


org_details = []
base = "https://www.edinburgh.gov.uk"
for org in org_list:
    url = base + org["org_url"]
    
    response = requests.get(url, headers=header) # request the web address
    if response.status_code==200:
        soup_org = soup(response.text, "html.parser")
        results = soup_org.find("dl", class_="list list--definition definition")
        #print(results)
        
        dts = results.find_all("dt")
        dt_list = []
        for dt in dts:
            dt_list.append(dt.text.strip())
            
        dds = results.find_all("dd")
        dd_list = []
        for dd in dds:
            dd_list.append(dd.text.strip())
        
        obs = dict(zip(dt_list, dd_list))
        obs["org_name"] = org["org_name"]
        obs["org_url"] = url
        #print(obs)
        
        org_details.append(obs)
    else:
        print("Could not request webpage")


# In[ ]:


org_details[0:4]


# #### Save file

# In[ ]:


outfile = la_data + "coe-library-spaces-" + ddate + ".json"
with open(outfile, "w", encoding="utf-8") as f:
    json.dump(org_details, f)


# ### Warm Spaces

# In[ ]:


header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
base = "https://www.edinburgh.gov.uk/directory/10258/a-to-z/"
abc = list(string.ascii_uppercase)

org_list = []
    
for l in abc:
    url = base + str(l)
    response = requests.get(url, headers=header) # request the web address
    
    if response.status_code==200:
        orgs = soup(response.text, "html.parser")
        try:
            results = orgs.find("ul", class_="list list--record").find_all("li")
            for el in results:
                name = el.find("a").text
                link = el.find("a").get("href")
                obs = {"org_name": name, "org_url": link}
                #print(obs)
                org_list.append(obs)
        except:
             print("Could not find list of organisations")
            
#print(response.text)


# #### Specific organisations

# In[ ]:


len(org_list)


# In[ ]:


org_list[0:4]


# In[ ]:


org_details = []
base = "https://www.edinburgh.gov.uk"
for org in org_list:
    url = base + org["org_url"]
    
    response = requests.get(url, headers=header) # request the web address
    if response.status_code==200:
        soup_org = soup(response.text, "html.parser")
        results = soup_org.find("dl", class_="list list--definition definition")
        #print(results)
        
        dts = results.find_all("dt")
        dt_list = []
        for dt in dts:
            dt_list.append(dt.text.strip())
            
        dds = results.find_all("dd")
        dd_list = []
        for dd in dds:
            dd_list.append(dd.text.strip())
        
        obs = dict(zip(dt_list, dd_list))
        obs["org_name"] = org["org_name"]
        obs["org_url"] = url
        #print(obs)
        
        org_details.append(obs)
    else:
        print("Could not request webpage")


# In[ ]:


org_details[0:4]


# #### Save file

# In[ ]:


outfile = la_data + "coe-warm-spaces-" + ddate + ".json"
with open(outfile, "w", encoding="utf-8") as f:
    json.dump(org_details, f)

