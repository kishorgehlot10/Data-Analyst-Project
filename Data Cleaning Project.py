#!/usr/bin/env python
# coding: utf-8

# # Data Cleaning Project

# In[1]:


# Import libraries

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
# Thanks to kaggle for dataset of house price prediction
# use pandas "pd.read_csv" function for importing csv file 

df = pd.read_csv("C://Users.//hp//desktop//DATA ANALYST//Dataset_for_data_cleaning_project.csv")

# This function give total number of rows and columns of our dataset.(rows,columns) format

df.shape

# This function give total column names in our dataset , so we can overview of our dataset.

df.columns

# This function give first 5 rows of our dataset.
# But, There is shows few columns and hide rest of them.
# we can show that ... after Utilities column.

df.head()

# This function give last 5 rows of our dataset.
# But, There is shows few columns and hide rest of them.
# we can show that ... after Utilities column.

df.tail()

# This function help to show all columns and rows of our dataset.
# This pandas function display maximum row & columns.

pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)

df.head()

df.tail()

"""This function give all information about dataset like  datatype pf columns,
    non-null value in columns,column name, column index etc.. """

df.info()

df.describe()

# This function give True value if value is null.

df.isnull()

# This function give sum of all null values which contain in each columns.

df.isnull().sum()

# we can't easily understand numerical data so, plotting heatmap by using seaborn library.
# white lines or marker in  our heat map is null value, so we need clear that columns.

plt.figure(figsize = (16,9)) # this function use for increase the plot size , so we can easily view it
sns.heatmap(df.isnull())
plt.show()

"""We calculate the total percentage of null values containing each column 
   as compare to total rows in each column and assign value to null_var variable """

null_var = df.isnull().sum()/df.shape[0]*100
null_var

# we observe that some columns containing more than 17% null value ,we separate out that columns.

drop_columns = null_var[null_var >17].keys()
drop_columns

# clean that null value containing columns for clean data.

clean_df = df.drop(columns = drop_columns)
clean_df

clean_df.shape

plt.figure(figsize = (16,9))
sns.heatmap(clean_df.isnull())
plt.show()

df_complete_clean  = clean_df.dropna()
df_complete_clean

df_complete_clean.shape

# we plot heatmap after removing all dirty data.

plt.figure(figsize = (16,9))
sns.heatmap(df_complete_clean.isnull())
plt.show()

# verify the data containing any null value or not ?

df_complete_clean.isnull().sum().sum()

# after cleaning data we need to know data distribution between old dirty dataset and clean dataset.

num_var = df_complete_clean.select_dtypes(include = ["int64","float64"]).columns
num_var

sns.histplot(df["YearBuilt"])

""" we use histogram to know conclusion about data distribution  between old dataset and
    new clean dataset or we lose important data. """

sns.histplot(df["YearBuilt"],color = "r")
sns.histplot(df_complete_clean["YearBuilt"],color ="y")

# At the end we extract our clean data into new csv file 

df_complete_clean.to_csv("C:/Users/hp/Desktop/DATA ANALYST/clean_dataset_after_cleaning.csv")

