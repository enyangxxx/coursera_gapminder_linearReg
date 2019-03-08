#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 00:46:03 2019

@author: enyang
"""

import pandas as pandas
import seaborn
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

#call in data set
data = pandas.read_csv('gapminder.csv',sep=',',error_bad_lines=False)

# Convert argument to a numeric type
# errors : {'ignore', 'raise', 'coerce'}, default 'raise' for raising exception
# - If 'ignore', then invalid parsing will return the input 
# - If 'coerce', then invalid parsing will be set as NaN
data['incomeperperson'] = pandas.to_numeric(data['incomeperperson'], errors='coerce')
data['internetuserate'] = pandas.to_numeric(data['internetuserate'], errors='coerce')

dataForFrame = {'IPP': data['incomeperperson'], 'IUR': data['internetuserate']}
df = pandas.DataFrame(data = dataForFrame)
df = df.dropna()

### mean is 8097.816446139661 ###
IPPmean = df['IPP'].mean()
df['IPPDeviationToMean'] = df['IPP'] - IPPmean

############################################################################################
# BASIC LINEAR REGRESSION
############################################################################################
scat1 = seaborn.regplot(x="IPPDeviationToMean", y="IUR", scatter=True, data=df)
plt.xlabel('Income per person deviation value to mean')
plt.ylabel('Internet Use Rate')
plt.title ('Scatterplot for the Association Between Income per person and Internet Use Rate')
print(scat1)

print ("OLS regression model for the association between income per person and internet use rate")
reg1 = smf.ols('IUR ~ IPPDeviationToMean', data=df).fit()
print (reg1.summary())