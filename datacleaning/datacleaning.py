import pandas as pd
import numpy as np

#importing the csv
df=pd.read_csv('dirty.csv')
print(df.head())
#%%
#checking the null values
print(df.isnull())

#%%
#checking how many values are there in each col
print(df.describe())
print(df.isnull().sum())
#%%
#this lets you drop all the rows from your table
dfdropp=df.dropna()
print(dfdropp.isnull().sum())
#%%
# Here we are going to use imputs to handle null values

#In this there are 2 types of imputing types they are * Univariate imputation and * Mulitvariate imputations

# In univariate imputations there 5 methods now we are going see each of them

#Mean Imputation
# where should we be using this
'''
we can use the mean Use it when you have missing numerical data
that you want to fill with 
the average value to maintain overall statistical consistency
'''
df['Age_mean'] = df['age'].fillna(df['age'].mean())
print(df.isnull().sum())
#df.to_csv('cleaned.csv')
#%%

'''Median imputation: Use it when you want to handle missing numerical data by r
eplacing it with the middle value, which is useful
 for datasets with outliers.
'''
df['income']=df['annual_income'].fillna(df['annual_income'].median())
df['median_monthly_income']=df['monthly_income'].fillna(df['monthly_income'].median())
df['cleaned_tax']=df['tax'].fillna(df['tax'].median())


#%%
'''
Mode imputation: Use it for categorical data to fill missing values with the most
frequent category, ensuring 
that the imputation reflects the most common occurrence.
'''

df['statemode']=df['states'].fillna(df['states'].mode()[0])
#%%
# Constant value imputation
df['CreditScore_constant'] = df['CreditScore'].fillna(-1)

# Indicator for missingness
df['CreditScore_missing'] = df['CreditScore'].isna().astype(int)

df['LoanAmount_end_of_tail'] = df['LoanAmount'].fillna(df['LoanAmount'].mean() + 3 * df['LoanAmount'].std())

#%%
df= df.dropna(axis=1, how='any')
df.to_csv('cleaned.csv')
#%%
