## Selecting predictors



Source:

 https://otexts.com/fpp2/selecting-predictors.html 



### Selecting predictors

When there are many possible predictors, we need some strategy for selecting the best predictors to use in a regression model.

A common approach that is *not recommended* is to plot the forecast variable against a particular predictor and if there is no noticeable relationship, drop that predictor from the model. This is invalid because it is not always possible to see the relationship from a scatterplot, especially when the effects of other predictors have not been accounted for.

Another common approach which is also invalid is to do a multiple linear regression on all the predictors and disregard all variables whose pp-values are greater than 0.05. To start with, statistical significance does not always indicate predictive value. Even if forecasting is not the goal, this is not a good strategy because the pp-values can be misleading when two or more predictors are correlated with each other.

Instead, we will use a measure of predictive accuracy. Five such measures are introduced in this section. They can be calculated using the `CV()` function, here applied to the model for US consumption:

CV(fit.consMR)
#>        CV       AIC      AICc       BIC     AdjR2 
#>    0.1163 -409.2980 -408.8314 -389.9114    0.7486

 We compare these values against the corresponding values from other models. For the CV, AIC, AICc and BIC measures, we want to find the model with the lowest value; for Adjusted R2R2, we seek the model with the highest value. 



### Adjusted R22

Computer output for a regression will always give the R2R2 value, discussed in Section [5.2](https://otexts.com/fpp2/least-squares.html#least-squares). However, it is not a good measure of the predictive ability of a model. Imagine a model which produces forecasts that are exactly 20% of the actual values. In that case, the R2R2 value would be 1 (indicating perfect correlation), but the forecasts are not close to the actual values.

In addition, R2R2 does not allow for “degrees of freedom”. Adding *any* variable tends to increase the value of R2R2, even if that variable is irrelevant. For these reasons, forecasters should not use R2R2 to determine whether a model will give good predictions, as it will lead to overfitting.

An equivalent idea is to select the model which gives the minimum sum of squared errors (SSE). Minimising the SSE is equivalent to maximising R2R2 and will always choose the model with the most variables, and so is not a valid way of selecting predictors.

An alternative which is designed to overcome these problems is the adjusted R2R2 (also called “R-bar-squared”):

![image-20191102180642266](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191102180642266.png)



### Cross-validation

Time series cross-validation was introduced in Section [3.4](https://otexts.com/fpp2/accuracy.html#accuracy) as a general tool for determining the predictive ability of a model. For regression models, it is also possible to use classical leave-one-out cross-validation to selection predictors (Bergmeir, Hyndman, & Koo, [2018](https://otexts.com/fpp2/selecting-predictors.html#ref-BHK15)). This is faster and makes more efficient use of the data. The procedure uses the following steps:

1. Remove observation tt from the data set, and fit the model using the remaining data. Then compute the error (e∗t=yt−^ytet∗=yt−y^t) for the omitted observation. (This is not the same as the residual because the ttth observation was not used in estimating the value of ^yty^t.)
2. Repeat step 1 for t=1,…,Tt=1,…,T.
3. Compute the MSE from e∗1,…,e∗Te1∗,…,eT∗. We shall call this the **CV**.

Although this looks like a time-consuming procedure, there are fast methods of calculating CV, so that it takes no longer than fitting one model to the full data set.

### Akaike’s Information Criterion

A closely-related method is Akaike’s Information Criterion, which we define 

![image-20191102181715092](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191102181715092.png)

where TT is the number of observations used for estimation and kk is the number of predictors in the model. Different computer packages use slightly different definitions for the AIC, although they should all lead to the same model being selected. The k+2k+2 part of the equation occurs because there are k+2k+2 parameters in the model: the kk coefficients for the predictors, the intercept and the variance of the residuals. The idea here is to penalise the fit of the model (SSE) with the number of parameters that need to be estimated.

The model with the minimum value of the AIC is often the best model for forecasting. For large values of TT, minimising the AIC is equivalent to minimising the CV value.



### Corrected Akaike’s Information Criterion

For small values of TT, the AIC tends to select too many predictors, and so a bias-corrected version of the AIC has been developed,

![image-20191102181826237](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191102181826237.png)

should be minimised.

### Schwarz’s Bayesian Information Criterion

A related measure is Schwarz’s Bayesian Information Criterion (usually abbreviated to BIC, SBIC or SC):

![image-20191102181914764](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191102181914764.png)

As with the AIC, minimising the BIC is intended to give the best model. The model chosen by the BIC is either the same as that chosen by the AIC, or one with fewer terms. This is because the BIC penalises the number of parameters more heavily than the AIC. For large values of TT, minimising BIC is similar to leave-vv-out cross-validation when v=T[1−1/(log(T)−1)]v=T[1−1/(log⁡(T)−1)].

### Which measure should we use?

While ¯R2R¯2 is widely used, and has been around longer than the other measures, its tendency to select too many predictor variables makes it less suitable for forecasting.

Many statisticians like to use the BIC because it has the feature that if there is a true underlying model, the BIC will select that model given enough data. However, in reality, there is rarely, if ever, a true underlying model, and even if there was a true underlying model, selecting that model will not necessarily give the best forecasts (because the parameter estimates may not be accurate).

Consequently, we recommend that one of the AICc, AIC, or CV statistics be used, each of which has forecasting as their objective. If the value of TT is large enough, they will all lead to the same model. In most of the examples in this book, we use the AICc value to select the forecasting model.