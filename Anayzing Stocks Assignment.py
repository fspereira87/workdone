#!/usr/bin/env python
# coding: utf-8

# ##### Question 1 - Extracting Tesla Stock Data Using yfinance

# In[1]:


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


# In[16]:


#Using the yfinance Library to Extract Tesla Stock Data

ticker = 'TSLA'
tesla = yf.download(ticker, start='2020-01-01', end='2023-01-01')
tesla.head()


# ##### Question 2 - Extracting Tesla Revenue Data Using Webscraping

# In[4]:


url = "https://companiesmarketcap.com/tesla/revenue/"
data = requests.get(url).text
soup = BeautifulSoup(data, 'html5lib')

# Initialize an empty list to store data
data_list = []

# Find all rows in the table (excluding header row)
rows = soup.find_all('tr')

for row in rows[1:]:  # Start from index 1 to skip the header row
    col = row.find_all('td')
    if len(col) >= 3:  # Ensure there are at least 3 columns (Year, Revenue, Change)
        year = col[0].text.strip()
        revenue = col[1].text.strip()
        change = col[2].text.strip()

        # Append data as a dictionary to the list
        data_list.append({"Year": year, "Revenue": revenue, "Change": change})
    else:
        print(f"Skipping row with insufficient data: {col}")

# Create DataFrame from the list of dictionaries
tesla_data = pd.DataFrame(data_list)

print(tesla_data.head())


# ##### Question 3 - Extracting GameStop Stock Data Using yfinance

# In[15]:


#Using the yfinance Library to Extract GameStop Stock Data

ticker = 'GME'
gme = yf.download(ticker, start='2020-01-01', end='2023-01-01')
gme.head()


# ##### Question 4 - Extracting GameStop Revenue Data Using Webscraping

# In[6]:


url = "https://companiesmarketcap.com/gamestop/revenue/"
data = requests.get(url).text
soup = BeautifulSoup(data, 'html5lib')


data_list = []

# Find all rows in the table (excluding header row)
rows = soup.find_all('tr')

for row in rows[1:]:  # Start from index 1 to skip the header row
    col = row.find_all('td')
    if len(col) >= 3:  # Ensure there are at least 3 columns (Year, Revenue, Change)
        year = col[0].text.strip()
        revenue = col[1].text.strip()
        change = col[2].text.strip()

        
        data_list.append({"Year": year, "Revenue": revenue, "Change": change})
    else:
        print(f"Skipping row with insufficient data: {col}")


gme_data = pd.DataFrame(data_list)

print(gme_data.head())
    


# ##### Question 5 - Tesla Stock and Revenue Dashboard

# In[18]:


# Plotting Tesla stock prices

plt.figure(figsize=(7, 3))
plt.plot(tesla['Close'], label='Tesla Stock Price', color='blue')
plt.title('Tesla Stock Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()

#Showing Gamestop Revenue
tesla_data.head(10)


# ##### Question 6 - GameStop Stock and Revenue Dashboard

# In[17]:


# Plotting Gamestop stock prices
plt.figure(figsize=(8, 3))
plt.plot(gme['Close'], label='GameStop Stock Price', color='blue')
plt.title('GameStop Stock Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()

#Showing Gamestop Revenue
gme_data.head(10)


# In[19]:





# In[ ]:




