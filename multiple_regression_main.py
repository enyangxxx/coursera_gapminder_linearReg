#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 03 07:41:03 2019

@author: enyang
"""

import pandas as pandas
import numpy as np
import seaborn
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%.2f'%x)

#call in data set
data = pandas.read_csv('gapminder.csv',sep=',',error_bad_lines=False)

# NEXT STEP: choose another variable

# Convert argument to a numeric type
# errors : {'ignore', 'raise', 'coerce'}, default 'raise' for raising exception
# - If 'ignore', then invalid parsing will return the input 
# - If 'coerce', then invalid parsing will be set as NaN
data['incomeperperson'] = pandas.to_numeric(data['incomeperperson'], errors='coerce')
data['internetuserate'] = pandas.to_numeric(data['internetuserate'], errors='coerce')
data['lifeexpectancy'] = pandas.to_numeric(data['lifeexpectancy'], errors='coerce')

dataForFrame = {'IPP': data['incomeperperson'], 'IUR': data['internetuserate'], 'LE': data['lifeexpectancy']}
df = pandas.DataFrame(data = dataForFrame).dropna()

### mean of IPP = 7462.046964195515 ###
### mean of IUR = 34.1106255490486 ###
df['IPP_c'] = df['IPP'] - df['IPP'].mean()
df['IUR_c'] = df['IUR'] - df['IUR'].mean()
df[["IPP", "IUR"]].describe()

############################################################################################
# POLYNOMIAL REGRESSION
############################################################################################

# first order (linear) scatterplot
scat1 = seaborn.regplot(x="IUR", y="LE", scatter=True, data=df)
plt.xlabel('Internet Use Rate')
plt.ylabel('Life Expectancy')
plt.title ('Scatterplot for the Association Between Internet Use Rate and Life Expectancy')

# fit second order polynomial
scat2 = seaborn.regplot(x="IUR", y="LE", scatter=True, order=2, data=df)
plt.xlabel('Internet Use Rate')
plt.ylabel('Life Expectancy')
plt.title ('Scatterplot for the Association Between Internet Use Rate and Life Expectancy')

# fit with enabled log function, estimate regression of the form y ~ log(x)
scat3 = seaborn.regplot(x="IUR", y="LE", scatter=True, logx=True, data=df)
plt.xlabel('Internet Use Rate')
plt.ylabel('Life Expectancy')
plt.title ('Scatterplot for the Association Between Internet Use Rate and Life Expectancy')

# linear regression analysis
reg1 = smf.ols('LE ~ IUR_c', data=df).fit()
print (reg1.summary())

# log function enabled without centering
reg2 = smf.ols('LE ~ np.log(IUR)', data=df).fit()
print (reg2.summary())

# run following line of code if getting PatsyError 'ImaginaryUnit' object is not callable
# del I

# quadratic (polynomial) regression analysis
reg3 = smf.ols('LE ~ IUR_c + I(IUR_c**2)', data=df).fit()
print (reg3.summary())

# adding internet use rate
reg4 = smf.ols('LE  ~ IUR_c + I(IUR_c**2) + IPP_c', 
               data=df).fit()
print (reg4.summary())

#Q-Q plot for normality
fig4=sm.qqplot(reg3.resid, line='r')

# simple plot of residuals
stdres=pandas.DataFrame(reg3.resid_pearson)
plt.plot(stdres, 'o', ls='None')
l = plt.axhline(y=0, color='r')
plt.ylabel('Standardized Residual')
plt.xlabel('Observation Number')

# additional regression diagnostic plots
fig2 = plt.figure(figsize=(9,6))
fig2 = sm.graphics.plot_regress_exog(reg3,  "IUR_c", fig=fig2)

# leverage plot
fig3=sm.graphics.influence_plot(reg3, size=8)
print(fig3)