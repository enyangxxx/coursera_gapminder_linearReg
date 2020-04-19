## Preprocessing: Binning

For this week's exercise and topic (Logistic Regression), I decided to keep using the Gapminder dataset and the previously selected explanatory variables (Income per Person & Internet Use Rate) and response variable (Life Expectancy).

As the sense of Logistic Regression is to have categorical response variables, it was required to conduct binning / discretization before executing the statistical analysis. Therefore I defined a function called "binning", which looks like this:
```
def binning(oldDF, dataSeries, binList, newColName, labelList, deleteOldColumn):
    columnForBins = pandas.cut(x = dataSeries, bins = binList, labels = labelList).to_frame()
    columnForBins.columns = [newColName]
    df_new = pandas.concat([oldDF,columnForBins],axis = 1)
    if deleteOldColumn is True:
        df_new = df_new.drop(dataSeries.name,axis=1)
    return df_new
```
Then I called the function during data preprocessing:
```
df = binning(df, df['LE'], [0, 70, 100], 'BinnedLE', ['0-70','70-100'], True)
```
This allows me to put the observed values of Life Expectancy into 2 categories: '0-70' and '70-100', the selection of threshold 70 is based on a personal decision without any further meanings. 

## Statistical Result

The 2 explanatory variables we investigate are IPP (Income per Person) and IUR (Internet Use Rate). Let's start with IPP.

![Regression Summary for IPP](https://github.com/enyangxxx/coursera_gapminder_linearReg/blob/master/wikiFiles/week4/summary_IPP.png)

The p-value is 0,000 which means that it is likely to be a meaningful addition to the model. But the odd ratio, which we can find beneath the summary, is 1,00 which reveals that it is statistically insignificant, especially the 95% confidence intervals (lower & upper), which are both 1,00, support that statement as well.

![Logistic Regression Plot for IPP](https://github.com/enyangxxx/coursera_gapminder_linearReg/blob/master/wikiFiles/week4/regplot_IPP.png)

The plot above shows the distribution of observed data. The Y-axis shows the BinnedLE, where 0 stands for '0-70' and 1 stands for '70-100', depending on the IPP values on the X-axis. The distribution reveals that generally, small IPP values lead to smaller LE more likely, but the range of values from the observed data for the bin '70-100' are covering the range of value between 0-10000 for IPP as well. This makes it very hard to say that smaller LE is associated to small IPP values.

![Regression Summary for IUR](https://github.com/enyangxxx/coursera_gapminder_linearReg/blob/master/wikiFiles/week4/summary_IUR.png)

The p-value for IUR is 0,000 which means that it is likely to be a meaningful addition to the model. But the odd ratio, which we can find beneath the summary, is 1,13 which reveals that it is statistically more likely significant than IPP. The 95% confidence intervals, which are 1,09 (lower CI) and 1,18 (upper CI), support that statement as well.

![Logistic Regression Plot for IUR](https://github.com/enyangxxx/coursera_gapminder_linearReg/blob/master/wikiFiles/week4/regplot_IUR.png)

The plot above shows the distribution of observed data. Once again, the Y-axis shows the BinnedLE, where 0 stands for '0-70' and 1 stands for '70-100', depending on the IUR values on the X-axis. The distribution reveals that generally, small IUR values lead to smaller LE more likely, but the range of values from the observed data for the bin '70-100' are covering the range of value between 0-40 for IUR as well. This makes it very hard to say that smaller LE is associated to small IUR values.

![Regression Summary for IUR and IPP](https://github.com/enyangxxx/coursera_gapminder_linearReg/blob/master/wikiFiles/week4/summary_IUR_IPP.png)

After putting both explanatory variables into the model, we can confirm that our previous assumption by analyzing the odd ratio of them. They become smaller for IUR, but still fit to our assumption that they are statistically more significant than the IPP, as we can see that its odd ratio remains 1,00.