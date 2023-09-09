#!/usr/bin/env python
# coding: utf-8

# In[35]:


# Import Libraries
import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt


# In[5]:


#Importing and Preview datasets
data=pd.read_csv("Downloads/_world-data-2023.csv")


# In[6]:


data.shape


# In[7]:


data.info()


# In[8]:


data.head()


# In[9]:


data.Country.unique()


# In[12]:


data.Country=data.Country.str.replace('S�����������'," ")


# In[13]:


data.Country=data.Country.replace(" ",np.nan)


# In[14]:


data.Country.unique()


# In[15]:


data.dtypes


# In[18]:


comma_cols = []
percent_cols = []
dollar_cols = []

for col in data.columns:
    if data[col].dtype == "object":
        if data[col].str.contains(",").any():
            comma_cols.append(col)
        elif data[col].str.contains("%").any():
            percent_cols.append(col)
        elif data[col].str.contains("$").any():
            dollar_cols.append(col)


# In[19]:


for col in percent_cols:
    data[col] = data[col].str.replace("%", " ")


# In[20]:


for col in comma_cols:
    data[col] = data[col].str.replace(","," ")


# In[21]:


for col in dollar_cols:
    data[col] = data[col].replace("$"," ")


# In[22]:


data["GDP"] = data["GDP"].replace("$","",regex=True)


# In[42]:


for col in data.columns:
    if data[col].dtype == "object":
        if col in ['Density\n(P/Km2)', 'Land Area(Km2)', 'Armed Forces size', 'Co2-Emissions', 'CPI', 'GDP', 'Population', 'Urban_population', 'Agricultural Land( %)', 'CPI Change (%)', 'Forested Area (%)', 'Gross primary education enrollment (%)', 'Gross tertiary education enrollment (%)', 'Out of pocket health expenditure', 'Population: Labor force participation (%)', 'Tax revenue (%)', 'Total tax rate', 'Unemployment rate', 'Gasoline Price', 'Minimum wage']:
 # Remove non-numeric characters (dollar sign and spaces) and convert to float
            data[col] = data[col].str.replace('[$, ]', '', regex=True).astype("float64")


# In[32]:


data.dtypes


# In[34]:


data.head()


# # Data Analysis and Visualisation  

# In[39]:


# Sort the DataFrame by "Unemployment rate" column in descending order
sorted_data = data.sort_values(by="Unemployment rate", ascending=False)

# Top 10 countries with the highest unemployment rate
top_10_unemployment_countries = sorted_data.head(10)

# Extract the country names and their corresponding unemployment rates
countries = top_10_unemployment_countries["Country"]
unemployment_rate = top_10_unemployment_countries["Unemployment rate"]

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(countries, unemployment_rate, color="red")
plt.xlabel("Country")
plt.ylabel("Unemployment Rate")
plt.title("Top 10 Countries with the Highest Unemployment Rate")
plt.xticks(countries, rotation=45, ha="right")
plt.tight_layout()
plt.show()


# In[43]:


# Top 10 countries with the highest population
sorted_data = data.sort_values(by= "Population", ascending= False)
top_10_population_countries = sorted_data.head(10)
countries = top_10_population_countries["Country"]
population = top_10_population_countries["Population"]
plt.figure(figsize=(12,6))
plt.bar(countries,population, color= "Orange")
plt.xlabel("Country")
plt.ylabel("Population")
plt.title("Top 10 Countries with Highest Population")
plt.xticks(countries,rotation=45,ha="right")
plt.tight_layout()
plt.show()


# In[47]:


columns_of_interest = ["Agricultural Land( %)", "Co2-Emissions", "Forested Area (%)"]
subset_data = data[columns_of_interest]
correlation_matrix = subset_data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True)
plt.title('Correlation Heatmap: Forested Area (%), Agricultural Land (%), and CO2 Emissions')
plt.show()


# In[49]:


# Urbanization trends by country
subset_countries = 20  # To display the top 20 countries
urbanization_by_country = data.groupby("Country")["Urban_population"].mean().sort_values(ascending=False).head(subset_countries)

plt.figure(figsize=(10, 8))
ax = urbanization_by_country.plot(kind="barh", color="purple")
plt.title("Urbanization Trends by Country")
plt.xlabel("Average Urban Population")
plt.ylabel("Country")
plt.gca().invert_yaxis()  # Invert y-axis to have the highest value at the top

# Add data labels to the bars
for index, value in enumerate(urbanization_by_country):           #loop iterates through the values in urbanization_by_country and adds data labels to the bars. The enumerate function is used to access both the index and value of each item.
    ax.text(value + 2, index, f'{value:.2f}', va='center', color="black")  # Display values on a separate axis

plt.show()


# In[52]:


# Population density distribution
plt.figure(figsize=(9,6))
plt.hist(data["Density\n(P/Km2)"], bins=20, color="green", edgecolor= "black")
plt.title("Population Density Distribution")
plt.xlabel("Density\n(P/Km2)")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()


# In[56]:


# Economic indicator scatter matrix
economic_indicators = data[["GDP","Gross primary education enrollment (%)","Total tax rate","Unemployment rate"]]
sns.set(style="ticks")
g=sns.pairplot(economic_indicators)
g.fig.suptitle("Scatter Plot Matrix of Key Economic Indicators", y=1.02)
plt.show()


# In[62]:


# Distribution of Life Expectancy
plt.figure(figsize=(9, 6))
sns.histplot(data=data, x='Life expectancy', bins=20, kde=True, color='Brown')
plt.title('Distribution of Life Expectancy')
plt.xlabel('Life Expectancy')
plt.ylabel('Frequency')
plt.show()

