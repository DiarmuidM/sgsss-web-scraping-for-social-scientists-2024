#!/usr/bin/env python
# coding: utf-8

# # Web scraping for social scientists: Example 1

# ## Introduction
# 
# Computational methods for collecting, cleaning and analysing data are an increasingly important component of a social scientist’s toolkit. Central to engaging in these methods is the ability to write readable and effective code using a programming language.
# 
# In this lesson we apply the logic of web scraping to some a simple, genuine website.

# ### Aims
# 
# This lesson has two aims:
# 1. Demonstrate how to use Python to collect data found on simple websites.
# 2. Cultivate your computational thinking skills through coding examples. In particular, how to define and solve a data collection problem using a computational method.

# ### Lesson details
# 
# * **Level**: Introductory
# * **Time**: 40-60 minutes
# * **Pre-requisites**: None
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

# ## What is the general approach for scraping data from a web page?

# We begin by identifying a web page containing information we are interested in collecting. Then we need to **know** the following:
# * The location (i.e., web address) where the web page can be accessed. For example, the NCRM homepage can be accessed via <a href="https://www.ncrm.ac.uk/" target=_blank>https://www.ncrm.ac.uk/</a>.
# * The location of the information we are interested in within the structure of the web page. This involves visually inspecting a web page's underlying code using a web browser.

# And **do** the following:
# * Request the web page using its web address.
# * Parse the structure of the web page so your programming language can work with its contents.
# * Extract the information we are interested in.
# * Write this information to a file for future use.
# 
# For any programming task, it is useful to write out the steps needed to solve the problem: we call this *pseudo-code*, as it is captures the main tasks and the order in which they need to be executed.

# ## A simple web scraping example: extracting text
# 
# Let's work through the steps in our general approach using a real web page, one that is designed for practicing web scraping.

# ###  Identifying the web address
# 
# The web page we are interested in can be found at the following web address: <a href="https://httpbin.org/html" target=_blank>https://httpbin.org/html</a>.
# 
# You can click on the link to open the web page in your browser, though we could just use Python to view it in this notebook:

# In[ ]:


from IPython.display import IFrame

IFrame("https://httpbin.org/html", width="1000", height="650")


# We can see that the web page contains some text - this is an abstract from Herman Melville's classic novel *Moby Dick*.

# ### Locating information
# 
# Our task is to extract the text on this web page. In order to do so, we need to understand where the text is located within the underlying *source code* of the web page. Web pages are written in a langauge called HyperText Markup Language (HTML). HTML describes the structure of a web page, and consists of a number of elements (e.g., paragraphs, tables, headers), with each element represented by a tag (e.g., `<p>`, `<table>`, `<h1>`). Browsers do not display the HTML tags, but use them to render the content of the page.
# 
# See <a href="https://www.w3schools.com/html/html_intro.asp" target=_blank>https://www.w3schools.com/html/html_intro.asp</a> for more information on HTML.

# #### Visually inspecting the underlying HTML code
# 
# Therefore, what we need are the tags that identify the section of the web page where the text is stored. We can discover the tags by examining the *source code* (HTML) of the web page. This can be done using your web browser: for example, if you use use Firefox you can right-click on the web page and select *View Page Source* from the list of options. (Chrome: *View page source*; Safari: follow <a href="https://www.lifewire.com/view-html-source-in-safari-3469315" target=_blank>these instructions</a>).
# 
# The cell below shows the full HTML code for the web page.
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
       

      <div>
        <p>
          Availing himself of the mild, summer-cool weather that now reigned in these latitudes, and in preparation for the peculiarly active pursuits shortly to be anticipated, Perth, the begrimed, blistered old blacksmith, had not removed his portable forge to the hold again, after concluding his contributory work for Ahab's leg, but still retained it on deck, fast lashed to ringbolts by the foremast; being now almost incessantly invoked by the headsmen, and harpooneers, and bowsmen to do some little job for them; altering, or repairing, or new shaping their various weapons and boat furniture. Often he would be surrounded by an eager circle, all waiting to be served; holding boat-spades, pike-heads, harpoons, and lances, and jealously watching his every sooty movement, as he toiled. Nevertheless, this old man's was a patient hammer wielded by a patient arm. No murmur, no impatience, no petulance did come from him. Silent, slow, and solemn; bowing over still further his chronically broken back, he toiled away, as if toil were life itself, and the heavy beating of his hammer the heavy beating of his heart. And so it was.—Most miserable! A peculiar walk in this old man, a certain slight but painful appearing yawing in his gait, had at an early period of the voyage excited the curiosity of the mariners. And to the importunity of their persisted questionings he had finally given in; and so it came to pass that every one now knew the shameful story of his wretched fate. Belated, and not innocently, one bitter winter's midnight, on the road running between two country towns, the blacksmith half-stupidly felt the deadly numbness stealing over him, and sought refuge in a leaning, dilapidated barn. The issue was, the loss of the extremities of both feet. Out of this revelation, part by part, at last came out the four acts of the gladness, and the one long, and as yet uncatastrophied fifth act of the grief of his life's drama. He was an old man, who, at the age of nearly sixty, had postponedly encountered that thing in sorrow's technicals called ruin. He had been an artisan of famed excellence, and with plenty to do; owned a house and garden; embraced a youthful, daughter-like, loving wife, and three blithe, ruddy children; every Sunday went to a cheerful-looking church, planted in a grove. But one night, under cover of darkness, and further concealed in a most cunning disguisement, a desperate burglar slid into his happy home, and robbed them all of everything. And darker yet to tell, the blacksmith himself did ignorantly conduct this burglar into his family's heart. It was the Bottle Conjuror! Upon the opening of that fatal cork, forth flew the fiend, and shrivelled up his home. Now, for prudent, most wise, and economic reasons, the blacksmith's shop was in the basement of his dwelling, but with a separate entrance to it; so that always had the young and loving healthy wife listened with no unhappy nervousness, but with vigorous pleasure, to the stout ringing of her young-armed old husband's hammer; whose reverberations, muffled by passing through the floors and walls, came up to her, not unsweetly, in her nursery; and so, to stout Labor's iron lullaby, the blacksmith's infants were rocked to slumber. Oh, woe on woe! Oh, Death, why canst thou not sometimes be timely? Hadst thou taken this old blacksmith to thyself ere his full ruin came upon him, then had the young widow had a delicious grief, and her orphans a truly venerable, legendary sire to dream of in their after years; and all of them a care-killing competency.
        </p>
      </div>
  </body>
</html>
# In the HTML code above, we can see multiple tags identifying different elements on the web page: there is a set of `<h1></h1>` tags representing the page title, a set of `<div></div>` tags representing a section, and a set of `<p></p>` tags representing the paragraph containing the text we are interested. (There are also some metadata tags outwith the `<body></body>` tags that we do not need to concern ourselves with).

# ### Requesting the web page
# 
# Now that we possess the necessary information, let's begin the process of scraping the web page. There is a preliminary step, which is setting up Python with the modules it needs to perform the web-scrape.

# In[ ]:


# Import modules

import os # module for navigating your machine (e.g., file directories)
import requests # module for requesting urls
from bs4 import BeautifulSoup as soup # module for parsing web pages

print("Succesfully imported necessary modules")


# Modules are additional techniques or functions that are not present when you launch Python. Some do not even come with Python when you download it and must be installed on your machine separately - think of using `ssc install <package>` in Stata, or `install.packages(<package>)` in R. For now just understand that many useful modules need to be imported every time you start a new Python session.

# Now, let's implement the process of scraping the page. First, we need to request the web page using Python; this is analogous to opening a web browser and entering the web address manually. We refer to a page's location on the internet as its web address or Uniform Resource Locator (URL).

# In[ ]:


# Define the URL where the web page can be accessed

link = "https://httpbin.org/html"

# Request the web page

response = requests.get(link) # request the url
response.status_code # check if url was requested successfully


# In[ ]:


response


# In[ ]:


response.status_code


# Good, we get a status code of *200*, which means the request was successful. A status code in *400s* or *500s* represent an unsuccessful attempt at requesting a web page (see <a href="https://www.w3schools.com/tags/ref_httpmessages.asp" target=_blank>here</a> for a comprehensive description of different types of response status codes).
# 
# Let's unpack the code a bit. First, we define a variable (also known as an 'object' in Python) called `url` that contains the web address of the page we want to request. Next, we use the `get()` method of the `requests` module to request the web page, and in the same line of code, we store the results of the request in a variable called `response`. Finally, we check whether the request was successful by calling on the `status_code` attribute of the `response` variable.

# We can also view the metadata associated with our request:

# In[ ]:


response.headers


# You may be wondering exactly what it is we requested: if you were to type the URL (https://httpbin.org/html) into your browser and hit `enter`, the web page should appear on your screen. This is not the case when we request the URL through Python but rest assured, we have successfully requested the web page. To see the content of our request, we can examine the `text` attribute of the `response` variable:

# In[ ]:


date = response.headers['Date']
date


# In[ ]:


response.text


# This shows us the underlying code (HTML) of the web page we requested. It should be obvious that in its current form, the result of this request will be difficult to work with. This is where the `BeautifulSoup` module comes in handy.

# ### Parsing the web page
# 
# Now it's time to identify and understand the structure of the web page we requested. We do this by converting the content contained in the `response.text` attribute into a `BeautifulSoup` variable. `BeautifulSoup` is a Python module that provides a systematic way of navigating the elements of a web page and extracting its contents. Let's see how it works in practice:

# In[ ]:


# Extract the contents of the webpage from the response

soup_response = soup(response.text, "html.parser") # Parse the text as a Beautiful Soup object
soup_response


# Notice how the hierarchical structure of the web page is now recognised by Python? Not only that, `BeautifulSoup` provides some methods for accessing the tags contained in the web page.

# ### Extracting information
# 
# Now that we have parsed the web page, we can use Python to navigate and extract the information of interest.

# In[ ]:


paragraph = soup_response.find("p")
paragraph


# We used the `find()` method on the `soup_response` variable to capture the set of `<p></p>` tags on the page. Remember, we used our visual inspection of the source code to identify that the text we needed was contained within a set of `<p></p>` tags, and that there was only one set.

# We're near the end of the scrape: we just need to extract the text from within the tags like so:

# In[ ]:


data = paragraph.text
print(data)


# ### Saving results from the scrape
# 
# Let's conclude by saving the scraped data to a file for future use.

# In[ ]:


# Create a downloads folder

try:
    os.mkdir("./downloads")
except:
    print("Unable to create folder: already exists")


# In[ ]:


# Define a file to store the data

outfile = "./downloads/moby-dick-scraped-data.txt" # location and name of file


# In[ ]:


# Open the file and write (save) the data to it

with open(outfile, "w") as f:
    f.write(data)


# How do we know this worked? The simplest way is to check whether a) the file was created, and b) the results were written to it.

# In[ ]:


# Check presence of file in current folder

os.listdir("./downloads")


# In[ ]:


# Open file and read (import) its contents

with open(outfile, "r") as f:
    ptext = f.read()
    
print(ptext)  


# And Voila, we have successfully scraped a web page!

# ## A simple web scraping example: downloading files

# Another useful application of web scraping is to download files from websites. The process is much the same, except this time we are requesting a url that leads to a file instead of a web page. Once requested we then need to save the file somewhere on our machine.
# 
# Using code to request files may seem unnecessary depending on the file in question &mdash; especially for files that are rarely updated &mdash;, however there are instances where a programmatic/automated approach is preferable e.g., when there are dozens/hundreds of files to download, datasets that are updated on a daily/weekly basis and thus overwrite old records.

# ###  Identifying the web address
# 
# The file we are interested in can be found on the following web page: <a href="https://register-of-charities.charitycommission.gov.uk/register/full-register-download" target=_blank>https://register-of-charities.charitycommission.gov.uk/register/full-register-download</a>. The file in question is the latest copy of the Register of Charities in England and Wales (think of this as a census of charities registered in those countries).

# ### Locating information
# 
# Our task is to download the Register of Charities on this web page , which is named **charity**. There are two versions of this file: a *json* and *txt* version. The former is a common data structure used to store and share data over the web, the latter is the familiar plain text format.
# 
# If we hover the pointer/curser over **download txt** link we can see the web address where this file is located: <a href="https://ccewuksprdoneregsadata1.blob.core.windows.net/data/txt/publicextract.charity.zip" target=_blank>https://ccewuksprdoneregsadata1.blob.core.windows.net/data/txt/publicextract.charity.zip</a>.

# ### Requesting the web page
# 
# Now that we possess the necessary information, let's begin the process of downloading the file. There is a preliminary step, which is setting up Python with the modules it needs to perform the web-scrape.

# In[ ]:


import os # module for navigating your machine (e.g., file directories)
import requests # module for requesting urls

print("Succesfully imported necessary modules")


# In[ ]:


# Define the URL where the web page can be accessed

url = "https://ccewuksprdoneregsadata1.blob.core.windows.net/data/txt/publicextract.charity.zip"

# Request the web page

response = requests.get(url) # request the url
response.status_code # check if url was requested successfully


# In[ ]:


response.headers


# Good, the request was successful. Here is where the process is slightly different compared to requesting a web page: we do not need to parse the file in order to extract information within it; we do not need to examine the contents of the file at this stage at all. All we need to do is save it somewhere on our machine. (Think of requesting a file as picking a box of cereal from a shelf and placing it in your shopping basket - you do not (I repeat, not) need to look inside the cereal at any point during this process).

# In[ ]:


download = "./downloads/ccew-register-of-charities.zip" # specify the name you want the file to have on your machine

with open(download, "wb") as f:
    f.write(response.content)


# In[ ]:


# Check presence of file in current folder

os.listdir()


# Great, the file has been downloaded, all that needs to be done is to extract ('unzip') the file from the its compressed folder. Python can handle this task:

# In[ ]:


import zipfile # module for compressing/decompressing files

with zipfile.ZipFile(download, "r") as download_zip:
    download_zip.extractall("./downloads/")


# In[ ]:


os.listdir("./downloads/")


# Now we have the file we wanted all along *publicextract.charity.txt*. To end this tutorial, let's take a quick peek at the dataset itself.

# In[ ]:


import pandas as pd

df = pd.read_csv("./downloads/publicextract.charity.txt", delimiter = "\t", on_bad_lines="skip")
df.sample(5)


# ## What have we learned?
# 
# Let's recap what key skills and techniques we've learned:
# * **How to import modules**. You will usually need to import modules into Python to support your work. Python does come with some methods and functions that are ready to use straight away, but for computational social science tasks you'll almost certainly need to import some additional modules.
# * **How to request and parse web pages**. You can use Python to request a web page, and the `BeautifulSoup` module to parse its contents.
# * **How to read and write data**. You can save the results of your scrape to a file for future use.
# * **How to do all of the above in an efficient, clear and effective manner**.

# ## Conclusion
# 
# While the above examples demonstrate the basics of web scraping well, collecting research-relevant data from a web page is a little more difficult:
# * Data may be spread throughout a web page (or across multiple pages).
# * There may be many tags with similar data that need to be filtered in order to get to the information you need.
# * And many other potential issues.
# 
# Thankfully the process/logic is the same even for more complicated examples - we'll explore these in the next lesson.

# ## Bibliography
# 
# Barba, Lorena A. et al. (2019). *Teaching and Learning with Jupyter*. <a href="https://jupyter4edu.github.io/jupyter-edu-book/" target=_blank>https://jupyter4edu.github.io/jupyter-edu-book/</a>.

# ### Exercise

# Returning to our example from one of the lectures, see if you can scrape the paragraphs under *Assessing our impact* section, as well as download at least one of the charity's reports:
# * https://www.marysmeals.org/what-we-do/our-impact

# In[ ]:


# INSERT CODE HERE


# In[ ]:


# INSERT CODE HERE


# The solution is provided at the end of this notebook.

# ## Appendix A

# ### Requesting URLs

# In Python we've made use of the excellent `requests` module. By calling the `requests.get()` method, we mimic the manual process of launching a web browser and visiting a website. The `requests` module achieves this by placing a _request_ to the server hosting the website (e.g., show me the contents of the website), and handling the _response_ that is returned (e.g., the contents of the website and some metadata about the request). This _request-response_ protocol is known as HTTP (HyperText Transfer Protocol); HTTP allows computers to communicate with each other over the internet - you can learn more about it at <a href="https://www.w3schools.com/whatis/whatis_http.asp" target=_blank>W3 Schools</a>.
# 
# Run the code below to learn more about the data and metadata returned by `requests.get()`.

# In[ ]:


import requests

url = "https://httpbin.org/html"
response = requests.get(url)

print("1. {}".format(response)) # returns the object type (i.e. a response) and status code
print("\r")

print("2. {}".format(response.headers)) # returns a dictionary of response headers
print("\r")

print("3. {}".format(response.headers["Date"])) # return a particular header
print("\r")

print("4. {}".format(response.request)) # returns the request object that requested this response
print("\r")

print("5. {}".format(response.url)) # returns the URL of the response
print("\r")

#print(response.text) # returns the text contained in the response (i.e. the paragraphs, headers etc of the web page)
#print(response.content) # returns the content of the response (i.e. the HTML contents of the web page)

# Visit https://www.w3schools.com/python/ref_requests_response.asp for a full list of what is returned by the server
# in response to a request.


# ### Exercise Solution

# #### Scraping the content under *Assessing our impact* heading

# In[ ]:


import os # module for navigating your machine (e.g., file directories)
import requests # module for requesting urls
from bs4 import BeautifulSoup as soup # module for parsing web pages

print("Succesfully imported necessary modules")

# Request web page

#headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}
url = "https://www.marysmeals.org/what-we-do/our-impact"
response = requests.get(url) # request the url
response.status_code # check if url was requested successfully

# Parse web page

soup_response = soup(response.text, "html.parser") # Parse the text as a Beautiful Soup object
#print(soup_response)

# Extract relevant content

paragraphs = soup_response.find("div", {"class": "coh-wysiwyg ssa-component coh-component ssa-component-instance-b659e133-d541-41a7-8fdc-a10d2a24b61a coh-component-instance-b659e133-d541-41a7-8fdc-a10d2a24b61a"}).find_all("p")
#print(paragraphs)

# Extract text

text = [p.text for p in paragraphs]
print(text)


# #### Download an annual report

# In[ ]:


from IPython.display import IFrame

url = "https://www.marysmeals.org/sites/mmi/files/2022-05/Our_Impact_Story_Marys_Meals_Impact_Assessment_Report.pdf"

response = requests.get(url)

outfile = "./downloads/marys-meals-impact-report.pdf"

with open(outfile, "wb") as f:
    f.write(response.content)
    
IFrame(outfile, width=600, height=300)


# --END OF FILE--
