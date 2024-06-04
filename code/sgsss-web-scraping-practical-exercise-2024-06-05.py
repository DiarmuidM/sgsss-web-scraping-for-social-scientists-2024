#!/usr/bin/env python
# coding: utf-8

# # Practical exercise

# ## Introduction
# 
# Computational methods for collecting, cleaning and analysing data are an increasingly important component of a social scientist’s toolkit. Central to engaging in these methods is the ability to write readable and effective code using a programming language.
# 
# In this practical you are tasked with conducting your own web scrape, addressing one of the challenges outlined [here](https://github.com/DiarmuidM/ncrm-web-scraping-for-social-scientists-2023/blob/main/code/ncrm-web-scraping-challenges-2023-06-06.md).

# ### Aims
# 
# This practical has one aim:
# 1. Collect data from a website of your choice using web scraping techniques.

# ## Guide to using this resource
# 
# This learning resource was built using <a href="https://jupyter.org/" target=_blank>Jupyter Notebook</a>, an open-source software application that allows you to mix code, results and narrative in a single document. As <a href="https://jupyter4edu.github.io/jupyter-edu-book/" target=_blank>Barba et al. (2019)</a> espouse:
# > In a world where every subject matter can have a data-supported treatment, where computational devices are omnipresent and pervasive, the union of natural language and computation creates compelling communication and learning opportunities.
# 
# If you are familiar with Jupyter notebooks then skip ahead to the main content (*What is the general approach for scraping data from a web page?*). Otherwise, the following is a quick guide to navigating and interacting with the notebook.

# ### Interaction
# 
# **You only need to execute the code that is contained in sections which are marked by `In []`.**
# 
# To execute a cell, click or double-click the cell and press the `Run` button on the top toolbar (you can also use the keyboard shortcut Shift + Enter).
# 
# Try it for yourself:

# In[1]:


print("Enter your name and press enter:")
name = input()
print("\r")
print("Hello {}, enjoy learning more about Python and web-scraping!".format(name))


# ### Learn more
# 
# Jupyter notebooks provide rich, flexible features for conducting and documenting your data analysis workflow. To learn more about additional notebook features, we recommend working through some of the <a href="https://github.com/darribas/gds19/blob/master/content/labs/lab_00.ipynb" target=_blank>materials</a> provided by Dani Arribas-Bel at the University of Liverpool. 

# ## What is the general approach for scraping data from a web page?
# 
# We begin by identifying a web page containing information we are interested in collecting. Then we need to **know** the following:
# 1. The location (i.e., web address) where the web page can be accessed. For example, the UK Data Service homepage can be accessed via <a href="https://ukdataservice.ac.uk/" target=_blank>https://ukdataservice.ac.uk/</a>.
# 2. The location of the information we are interested in within the structure of the web page. This involves visually inspecting a web page's underlying code using a web browser.

# And **do** the following:
# 1. Request the web page using its web address.
# 2. Parse the structure of the web page so your programming language can work with its contents.
# 3. Extract the information we are interested in.
# 4. Write this information to a file for future use.
# 
# For any programming task, it is useful to write out the steps needed to solve the problem: we call this *pseudo-code*, as it is captures the main tasks and the order in which they need to be executed.

# ## Details
# 
# Your task is to apply the framework above to a website/file of your choosing. The key steps are outlined as headings but no code is provided: I look forward to seeing your ideas come to fruition!

# ###  Identifying the web address

# INSERT COMMENTS HERE IF NECESSARY

# In[1]:


# INSERT CODE HERE IF NECESSARY


# ### Locating information
# 

# INSERT COMMENTS HERE IF NECESSARY

# In[ ]:


# INSERT CODE HERE


# #### Visually inspecting the underlying HTML code

# ### Requesting the web page

# In[2]:


# Import modules


# In[3]:


# Define the URL where the web page can be accessed


# ### Parsing the web page

# In[5]:


# Extract the contents of the webpage from the response



# ### Extracting information

# In[6]:


# INSERT CODE HERE


# ### Saving results from the scrape

# In[12]:


# Define a file to store the data



# Open the file and write (save) the data to it



# In[8]:


# Check presence of file in current folder



# In[7]:


# Open file and read (import) its contents



# And Voila, you have successfully scraped a web page!

# --END OF FILE--
