## Introduction & Preprocessing

For this week's exercise, I chose 2 explanatory variables (Internet Use Rate & Income per Person) and 1 response variable (Life Expectancy). For the preprocessing part, I put all the relevant variables into a new dataframe called 'df', then conducted the centering of Income per Person & Internet Use Rate values and also put them into 'df'. 

After that, I called ```df[["IPP", "IUR"]].describe()``` to get important values for measures of central tendency and measures of variation.

![Explanatory variable description](https://github.com/enyangxxx/coursera_gapminder_linearReg/blob/master/wikiFiles/week3/IPP_IUR_describe.png)

## Seaborn Regression Plots

For the regression plots, I tried 3 different variations. Let's start with the first one, a simple linear scatterplot (Order = 1 by default):

![Linear Regression Plot](https://github.com/enyangxxx/coursera_gapminder_linearReg/blob/master/wikiFiles/week3/regplot_1order.png)

Here we can see a linear plot to describe the association between Internet Use Rate and Life Expectancy, obviously not the best way to describe the given data, because a linear regression in this manner would exceed reasonable limit of life expectancy. Also the existing data shows a curve, which the lineare regression plot does not fit very well, which brings us to the second approach, a polynomial plot with order = 2:

![Polynomial Regression Plot](https://github.com/enyangxxx/coursera_gapminder_linearReg/blob/master/wikiFiles/week3/regplo_2order.png)

Unlike the linear plot, the polynomial regression plot is describing the data in a better manner by using the quadratic function. For 0 < x < 100, the polynomial plot shows a graph where the slope is descending when x is converging 80 and then the curve falls. That is an arguable aspect whether y should follow the graph of quadratic function and fall again or better converge a certain maximum of y-value. For the later case, we have the last regression plot:

![Log Regression Plot](https://github.com/enyangxxx/coursera_gapminder_linearReg/blob/master/wikiFiles/week3/regplot_logx.png)

The graph here looks very similar to the second plot, but the difference to that is the usage of logarithm function. By resetting the order to 1 again and enabling the log for x, the graph starts with a strong slope, which weakens more and more till the graph converges the maximum of ca. 80. That would mean that the graph will not fall again unlike the graph of quadratic function. In my opinion, this is probably the more realistic plot to describe the association between the two variables.

## OLS Regression Summary

For the regression model fit, 4 different formulas are set, each of them lead to a different result. While the first model is based on linear regression for centered Internet Use Rate, the second model includes logarithm of non-centered Internet Use Rate values. The last two models are for polynomial regressions, especially the last model is considering multiple (2) explanatory variables.

### Linear Regression Model fit:
```
reg1 = smf.ols('LE ~ IUR_c', data=df).fit()
```
![Linear Regression Model fit](https://github.com/enyangxxx/coursera_gapminder_linearReg/blob/master/wikiFiles/week3/linear_fit.png)

### Logarithm Regression Model fit:
```
reg2 = smf.ols('LE ~ np.log(IUR)', data=df).fit()
```
![Logarithm Regression Model fit](https://github.com/enyangxxx/coursera_gapminder_linearReg/blob/master/wikiFiles/week3/log_fit.png)

### Polynomial Regression Model fit with 1 variable:
```
reg3 = smf.ols('LE ~ IUR_c + I(IUR_c**2)', data=df).fit()
```
![Polynomial Regression Model fit with One Variable](https://github.com/enyangxxx/coursera_gapminder_linearReg/blob/master/wikiFiles/week3/polynomial_fit_one_variable.png)

### Polynomial Regression Model fit with 2 variables:
```
reg4 = smf.ols('LE  ~ IUR_c + I(IUR_c**2) + IPP_c', 
               data=df).fit()
```
![Polynomial Regression Model fit with two variables](https://github.com/enyangxxx/coursera_gapminder_linearReg/blob/master/wikiFiles/week3/polynomial_fit_two_variables.png)

By comparisons of the 4 summaries, you can see that the R-squared value is greater in polynomial regression model than in linear regression models, which confirms my previous assumption in the Seaborn Regression Plot section. The greatest R-squared value is shown in the polynomial regression model with 2 variables (0.653). 

If you have a more detailed look on the last model: The coefficients for the explanatory variables are not big values, but the intercept (73,62). It is the life expectancy value when Internet Use Rate and Income per Person are at their means. As we know that p-value < 0.05 is likely to be a meaningful addition to the model, all explanatory variables seem to be statistically significant enough to be considered.

Furthermore, we can see that the coefficient of centered Income per person is 0,0003, which indicates a very small positive association in this model. The 95% confidence interval shows that coefficient value for centered Income per person is most likely ca. 0. The standard deviation/error is also a very small number (8.79e-05). It does not mean at all that this variable is useless or even a confounding variable, otherwise the p-value would show value greater than 0,05.

## QQ-Plot
![QQ-Plot](https://github.com/enyangxxx/coursera_gapminder_linearReg/blob/master/wikiFiles/week3/qqplot.png)

"As we know that the easiest way to evaluate the residuals is to graph them, we can use a qq-plot to evaluate the assumption that the residuals from our regression model are normally distributed." (Source: Python Lesson 4) In the plot above, we can see the regression line in red and also recognize that the residuals of our model are generally follow the red line, but are not perfectly normally distributed due to obvious deviations. That means that other variables could be considered to improve our model and the observed curvilinearity.

## Standardized residuals for all observations
![Residual Pearson Plot](https://github.com/enyangxxx/coursera_gapminder_linearReg/blob/master/wikiFiles/week3/resid_pearson_plot.png)

In a standard normal distribution, 95% of the observations should be covered by 2 standard deviations of the mean. In the plot above, we can see that the most observations have a standardized residual between 2 und -2, but also 10 absolute values > 2 are existing. We have 1 extrem outlier which has an absolute value > 2.5 . 

"If more than 1% of our observations has standardized residuals with an absolute value greater than 2.5, or more than 5% have an absolute value of greater than or equal to 2, then there is evidence that the level of error within our model is unacceptable." (Source: Python Lesson 5) According to these rules, since we have 165 observations, we can calculate for these rules:
1 / 165 = 0,6%
10 / 165 = 6,06%
This shows us that the level of error within our model needs improvement and the fit can be optimized. 

## Leverage plot
![Leverage Plot](https://github.com/enyangxxx/coursera_gapminder_linearReg/blob/master/wikiFiles/week3/leverage_plot.png)

The most points have a leverage level under 0,03 and a small influence on the estimation. Observation no. 106 has a big influence on the estimation of the predicted value for life expectancy, but is also not an outlier, as it is within 2 standard deviations of the mean. We don't have any observations which are also outliers. The outliers which can be observed, have < 0.025 leverage values, that means although they are outlying observations, they do not have a huge influence on the estimation of the regression model overall. 

## Additional Regression Diagnostic Plots
![Regression Diagnostic Plots](https://github.com/enyangxxx/coursera_gapminder_linearReg/blob/master/wikiFiles/week3/plot_regress_exog.png)

These plots help us to determine how specific explanatory variables contribute to the fit of our model. The plot on the right top shows the residuals versus centered Internet Use Rate. The greatest absolute value of residual is ca. 20 and seems to be an outlier, while the other absolute residuals greater than 10 are mostly versus small values of centered Internet Use Rate. 

The partial regression plot shows the relationship between the response variable (Life Expectancy) and specific explanatory variable (in my case: centered Internet Use Rate), after controlling for the other explanatory variables. We can see if the centered Internet Use Rate residuals show a linear or non-linear pattern. "If the Internet use variable shows a linear relationship to the response variable after adjusting for the variables already in the model, it meets the linearity assumption in the multiple regression. If there is an obvious non-linear pattern, this would be additional support for adding a polynomial term for Internet use rate to the model." (Source: Python Lesson 5) We can see in our partial regression plot that there is a curvilinearity which indicates a slight non-linear association. The residuals are spread out in a random pattern around the partial regression line and a lot of them are pretty far from this line, indicating a great deal of life expectancy prediction error, which can be confirmed by the plot on the right top.