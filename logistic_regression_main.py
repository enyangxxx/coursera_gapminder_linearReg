#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 03 07:41:03 2019

@author: enyang
"""

import pandas as pandas
import numpy as numpy
import seaborn
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%.2f'%x)

#call in data set
data = pandas.read_csv('gapminder.csv',sep=',',error_bad_lines=False)

# Convert argument to a numeric type
# errors : {'ignore', 'raise', 'coerce'}, default 'raise' for raising exception
# - If 'ignore', then invalid parsing will return the input 
# - If 'coerce', then invalid parsing will be set as NaN
data['incomeperperson'] = pandas.to_numeric(data['incomeperperson'], errors='coerce')
data['internetuserate'] = pandas.to_numeric(data['internetuserate'], errors='coerce')
data['lifeexpectancy'] = pandas.to_numeric(data['lifeexpectancy'], errors='coerce')
# check type(data['lifeexpectancy']) in Console if unsure

def binning(oldDF, dataSeries, binList, newColName, labelList, deleteOldColumn):
    columnForBins = pandas.cut(x = dataSeries, bins = binList, labels = labelList).to_frame()
    columnForBins.columns = [newColName]
    df_new = pandas.concat([oldDF,columnForBins],axis = 1)
    if deleteOldColumn is True:
        df_new = df_new.drop(dataSeries.name,axis=1)
    return df_new


dataForFrame = {'IPP': data['incomeperperson'], 'IUR': data['internetuserate'], 'LE': data['lifeexpectancy']}
df = pandas.DataFrame(data = dataForFrame).dropna()
df = binning(df, df['LE'], [0, 70, 100], 'BinnedLE', ['0-70','70-100'], True)
df = df.replace(to_replace={'BinnedLE' : {'0-70' : 0, '70-100' : 1}})

# logistic regression with Income per Person
lreg1 = smf.logit(formula = 'BinnedLE ~ IPP', data = df).fit()
print (lreg1.summary())

# odd ratios with 95% confidence intervals
params = lreg1.params
conf1 = lreg1.conf_int()
conf1['OR'] = params
conf1.columns = ['Lower CI', 'Upper CI', 'OR']
print (numpy.exp(conf1))

# logistic regression with IUR
lreg2 = smf.logit(formula = 'BinnedLE ~ IUR', data = df).fit()
print (lreg2.summary())

# odd ratios with 95% confidence intervals
params = lreg2.params
conf2 = lreg2.conf_int()
conf2['OR'] = params
conf2.columns = ['Lower CI', 'Upper CI', 'OR']
print (numpy.exp(conf2))

# logistic regression with IUR & IPP
lreg3 = smf.logit(formula = 'BinnedLE ~ IUR + IPP', data = df).fit()
print (lreg3.summary())

# odd ratios with 95% confidence intervals
params = lreg3.params
conf3 = lreg3.conf_int()
conf3['OR'] = params
conf3.columns = ['Lower CI', 'Upper CI', 'OR']
print (numpy.exp(conf3))

g = seaborn.regplot(x="IPP", y="BinnedLE", scatter=True, data=df, logistic=True)
