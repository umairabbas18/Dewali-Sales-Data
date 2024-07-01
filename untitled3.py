# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lFuJ_i7VanT-AWCxl0e87rDA0BLLSoex
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # visulazation data
# %matplotlib inline
import seaborn as sns

df = pd.read_csv('Diwali Sales Data.csv' , encoding = 'unicode_escape')

df.shape

df.head(10)

df.info()

#drop unrelated/blank columns
df.drop(['Status' , 'unnamed1'] , axis =1, inplace = True)

pd.isnull(df)

#check for null values
pd.isnull(df).sum()

df.shape

#drop null values
df.dropna(inplace = True)

#change data type
df['Amount'] = df['Amount'].astype('int')

df['Amount'].dtypes

df.columns

#rename column
df.rename(columns = {'Marital_Status' : 'Shaadi'})

#describe() methd return description of the data in the DataFrame ( i.e. count, mean, std, etc)
df.describe()

ax = sns.countplot(x = 'Gender' , data = df)

for bars in ax.containers:
    ax.bar_label(bars)

sales_gen = df.groupby(['Gender'] , as_index = False)['Amount'].sum().sort_values(by = 'Amount' , ascending = False)
sns.barplot(x = 'Gender' , y = 'Amount' , data = sales_gen)

"""From the graph above, it is evident that females made more purchases than males."""

ax = sns.countplot(data = df , x = 'Age Group' , hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)

sales_age = df.groupby(['Age Group'] , as_index = False)['Amount'].sum().sort_values(by = 'Amount' , ascending = False)
sns.barplot(x = 'Age Group' , y = 'Amount' , data = sales_age)

"""Predominantly, women aged 26-35 constitute the majority of buyers."""

#Totle number of orders from top 10 stores

sales_state = df.groupby(['State'] , as_index = False)['Orders'].sum().sort_values(by = 'Orders' , ascending = False).head(10)

sns.set(rc = {'figure.figsize' : (15 , 5)})
sns.barplot(x = 'State' , y = 'Orders' , data = sales_state)

#Totle amount/sales from 10 states
sales_state = df.groupby(['State'] , as_index = False)['Amount'].sum().sort_values(by = 'Amount' , ascending = False).head(10)

sns.set(rc = {'figure.figsize' : (15 , 5)})
sns.barplot( x = 'State' , y = 'Amount' , data = sales_state)

"""# **MARITAL STATUS**"""

!pip install seaborn
import seaborn as sns

#Assuming 'df' is your DataFrame with 'Marital_Status', 'Amount', and 'Gender' cplumns

sns.set(rc = {'figure.figsize' : (6 , 5)})

#Use boxplot to visualize distribution of 'Amount' across 'Marital_state' and 'Gender'
ax = sns.barplot(x = 'Marital_Status' , y = 'Amount' , hue = 'Gender' , data = df)

sns.set(rc = {'figure.figsize' : (20 , 10)})

"""Purchasing power is geared towards married women.

# **OCCUPATION**
"""

sns.set(rc = {'figure.figsize' : (20 , 5)})
ax = sns.countplot(data = df , x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)

sales_state = df.groupby(['Occupation'] , as_index = False)['Amount'].sum().sort_values(by = 'Amount' , ascending = False)

sns.set(rc = {'figure.figsize' : (20 , 5)})
sns.barplot(x = 'Occupation' , y = 'Amount' , data = sales_state)

"""From the graph above, it is evident that the majority of buyers come from the IT, Healthcare, and Aviation departments."""

#Verify the column names in DataFrame
print(df.columns)

"""# **Product Category**

"""

sns.set(rc = {'figure.figsize' : (20 , 7)})
ax = sns.countplot(data = df , x = 'Product_Category')

ax.set_xticklabels(ax.get_xticklabels() , rotation = 90 , ha = 'right')

for bars in ax.containers:
    ax.bar_label(bars)

sales_state = df.groupby(['Product_Category'] , as_index = False)['Amount'].sum().sort_values(by = 'Amount' , ascending = False).head(10)

sns.set(rc = {'figure.figsize' : (20 , 10)})
sns.barplot(x = 'Product_Category' , y = 'Amount' , data = sales_state)

"""From the graph above, we can observe that the majority of products sold fall under categories such as food, clothing, and electronics."""

sales_state = df.groupby(['Product_ID'] , as_index = False)['Orders'].sum().sort_values(by = 'Orders' , ascending = False).head(10)

sns.set(rc = {'figure.figsize' : (20 , 10)})
sns.barplot(x = 'Product_ID' , y = 'Orders' , data = sales_state)

#Top 10 sold products

fig1 , ax1 = plt.subplots(figsize = (12 , 7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending = False).plot(kind = 'bar')

"""# **CONCLUSION**

Married women aged 26-35 from Uttar Pradesh, Maharashtra, and Karnataka working in IT, Healthcare, and Aviation are more likely to buy products from the Food, Clothing, and Electronics categories.
"""