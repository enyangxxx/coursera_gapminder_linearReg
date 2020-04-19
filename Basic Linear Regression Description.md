## OLS Regression Summary
![OLS Regression](https://github.com/enyangxxx/coursera_gapminder_linearReg/blob/master/wikiFiles/week2/olsLinearRegSummary.png)

The depending variable is Internet use rate (IUP), the explanatory variable is Income per person (IPP). The linear regression model is: y = 35.1215 + x1 * IPPDeviationToMean. When using IPP instead of IPPDeviationToMean, the scatterplot in the section below reveals to be similar. 

"The p-value for each term tests the null hypothesis that the coefficient is equal to zero (no effect). A low p-value (< 0.05) indicates that you can reject the null hypothesis. In other words, a predictor that has a low p-value is likely to be a meaningful addition to your model because changes in the predictor's value are related to changes in the response variable." (Source: http://blog.minitab.com) The p-value for IPP is 0.000, which means it is statistically significant and can be used in the linear regression model. 

## Scatterplot for the association between Income per person (IPP) and Internet use rate (IUR)
![Scatterplot](https://github.com/enyangxxx/coursera_gapminder_linearReg/blob/master/wikiFiles/week2/scatterplot_IPP_IUR.png)

The scatterplot shows that a linear curve might not be the most capable solution to describe the given data. A polynomial regression might fit better here.

## Others
The mean of Income per person value, by considering all countries with given values is 8097.816446139661