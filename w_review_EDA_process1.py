#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/17/18 5:01 PM
# @Author  : Yan Jia
# @Site    : 
# @File    : w_review_EDA_process1.py
# @Software: IntelliJ IDEA


import missingno as msno
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df1 = pd.read_csv('../wine_reviews/winemag-data-130k-v2.csv')

#1. check head()
df1.head()
#2. check type of each factor
df1.dtypes


#4. explore NA
#show numbers.
df1.isnull().sum()
#%matplotlib inline # plot the graph by using the Jupytor
# plot the count of NA in each factor column
#msno.bar(df1)


#5. delete duplicate
print("Total records: ", df1.shape[0])
print("Records with the same title and description: ", df1[df1.duplicated(['description','title'])].shape[0])
#drop duplicates
df1=df1.drop_duplicates(['description','title'])

#3. points/price statistics
df1 = df1.drop(['Unnamed: 0', 'description'],axis=1) # won't use
print df1.describe()

# deal NA
df1 =df1.dropna(subset=['price']) #let price as response variable, delete NA price


# extract year from title
#df1['year'] = df1['title'].str.extract(r'([\d]{4})', expand=True)

#visualizations
# how's points vary in different country,region,
#v2
fig, ax = plt.subplots(figsize = (20,7))
chart = sns.boxplot(x='country',y='points', data=df1, ax = ax).set_title('Points in Countries')
plt.xticks(rotation = 90)
plt.show()

#show top 20 countries with meds
df1.country.value_counts()[:20]

#only display the reviews with more than 100
country=df1.groupby('country').filter(lambda x: len(x) >100)
df2 = pd.DataFrame({col:vals['points'] for col,vals in country.groupby('country')})
meds = df2.median()
meds.sort_values(ascending=False, inplace=True)

fig, ax = plt.subplots(figsize = (20,7))
chart = sns.boxplot(x='country',y='points', data=country, order=meds.index, ax = ax).set_title('Points in Countries with Reviews more than 100')
plt.xticks(rotation = 90)
plt.show()
