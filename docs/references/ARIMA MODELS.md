## ARIMA MODELS



Source:

 https://otexts.com/fpp2/arima.html 



## Stationarity and differencing

A stationary time series is one whose properties do not depend on the time at which the series is observed.[14](https://otexts.com/fpp2/stationarity.html#fn14) Thus, time series with trends, or with seasonality, are not stationary — the trend and seasonality will affect the value of the time series at different times. On the other hand, a white noise series is stationary — it does not matter when you observe it, it should look much the same at any point in time.

Some cases can be confusing — a time series with cyclic behaviour (but with no trend or seasonality) is stationary. This is because the cycles are not of a fixed length, so before we observe the series we cannot be sure where the peaks and troughs of the cycles will be.

In general, a stationary time series will have no predictable patterns in the long-term. Time plots will show the series to be roughly horizontal (although some cyclic behaviour is possible), with constant variance.



### Differencing

Even when a series is not stationary, its differences could be stationary. This shows one way to make a non-stationary time series stationary — compute the differences between consecutive observations. This is known as **differencing**.

Transformations such as logarithms can help to stabilise the variance of a time series. Differencing can help stabilise the mean of a time series by removing changes in the level of a time series, and therefore eliminating (or reducing) trend and seasonality.

As well as looking at the time plot of the data, the ACF plot is also useful for identifying non-stationary time series. For a stationary time series, the ACF will drop to zero relatively quickly, while the ACF of non-stationary data decreases slowly. Also, for non-stationary data, the value of r1r1 is often large and positive.



### Seasonal differencing

Seasonality can be assessed with ARIMA models. To detect seasonality performing an ADF test is required.

A seasonal difference is the difference between an observation and the previous observation from the same season. 

![image-20191102201703588](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191102201703588.png)

where m=m= the number of seasons. These are also called “lag-m differences”, as we subtract the observation after a lag of m periods.



### Random walk model

The differenced series is the *change* between consecutive observations in the original series, and can be written as

![image-20191103132322977](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191103132322977.png)

The differenced series will have only T−1 values, since it is not possible to calculate a difference y′1 for the first observation.

When the differenced series is white noise, the model for the original series can be written as

![image-20191103125808687](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191103125808687.png)

 where εt denotes white noise. Rearranging this leads to the “random walk” model 

![image-20191103125813351](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191103125813351.png)

Random walk models are widely used for non-stationary data, particularly financial and economic data. Random walks typically have:

- long periods of apparent trends up or down
- sudden and unpredictable changes in direction.

The forecasts from a random walk model are equal to the last observation, as future movements are unpredictable, and are equally likely to be up or down. Thus, the random walk model underpins naïve forecasts, first introduced in Section [3.1](https://otexts.com/fpp2/simple-methods.html#simple-methods).

A closely related model allows the differences to have a non-zero mean. Then:

![image-20191103125818772](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191103125818772.png)

### Second-order differencing

Occasionally the differenced data will not appear to be stationary and it may be necessary to difference the data a second time to obtain a stationary series:

![image-20191103125855357](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191103125855357.png)

In this case, y′′t will have T−2 values. Then, we would model the “change in the changes” of the original data. In practice, it is almost never necessary to go beyond second-order differences.



### DIFFERENCING:

### Unit root tests:

**STATIONARITY:**

It is necessary to check the stationarity of the series.

One way to determine more objectively whether differencing is required is to use a *unit root test*. These are statistical hypothesis tests of stationarity that are designed for determining whether differencing is required.

A number of unit root tests are available, which are based on different assumptions and may lead to conflicting answers. In our analysis, we use the *Kwiatkowski-Phillips-Schmidt-Shin (KPSS) test* (Kwiatkowski, Phillips, Schmidt, & Shin, [1992](https://otexts.com/fpp2/stationarity.html#ref-KPSS92)). In this test, the null hypothesis is that the data are stationary, and we look for evidence that the null hypothesis is false. Consequently, small p-values (e.g., less than 0.05) suggest that differencing is required. The test can be computed using the `ur.kpss()` function from the [**urca** package](https://cran.r-project.org/package=urca).

**SEASONALITY:**

A similar function for determining whether seasonal differencing is required is `nsdiffs()`, which uses the measure of seasonal strength introduced in Section [6.7](https://otexts.com/fpp2/seasonal-strength.html#seasonal-strength) to determine the appropriate number of seasonal differences required. No seasonal differences are suggested if FS<0.64, otherwise one seasonal difference is suggested.

We can apply `nsdiffs()` to the logged US monthly electricity data.



## Autoregressive models

In a multiple regression model, we forecast the variable of interest using a linear combination of predictors. In an autoregression model, we forecast the variable of interest using a linear combination of *past values of the variable*. The term *auto*regression indicates that it is a regression of the variable against itself.

Thus, an autoregressive model of order pp can be written as

![image-20191103130015505](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191103130015505.png)

where εt is white noise. This is like a multiple regression but with *lagged values* of ytyt as predictors. We refer to this as an **AR(pp) model**, an autoregressive model of order pp.

Autoregressive models are remarkably flexible at handling a wide range of different time series patterns. The two series in Figure [8.5](https://otexts.com/fpp2/AR.html#fig:arp) show series from an AR(1) model and an AR(2) model. Changing the parameters ϕ1,…,ϕp results in different time series patterns. The variance of the error term εtεt will only change the scale of the series, not the patterns.

 ![Two examples of data from autoregressive models with different parameters. Left: AR(1) with $y_t = 18 -0.8y_{t-1} + \varepsilon_t$. Right: AR(2) with $y_t = 8 + 1.3y_{t-1}-0.7y_{t-2}+\varepsilon_t$. In both cases, $\varepsilon_t$ is normally distributed white noise with mean zero and variance one.](https://otexts.com/fpp2/fpp_files/figure-html/arp-1.png) 

For an AR(1) model:

- when ϕ1=0ϕ1=0, yt is equivalent to white noise;
- when ϕ1=1ϕ1=1 and c=0c=0, yt is equivalent to a random walk;
- when ϕ1=1ϕ1=1 and c≠0c≠0, yt is equivalent to a random walk with drift;
- when ϕ1<0ϕ1<0, yt tends to oscillate around the mean.

We normally restrict autoregressive models to stationary data, in which case some constraints on the values of the parameters are required.

- For an AR(1) model: −1<ϕ1<1.
- For an AR(2) model: −1<ϕ2<1, ϕ1+ϕ2<1, ϕ2−ϕ1<1.

When p≥3p≥3, the restrictions are much more complicated. R takes care of these restrictions when estimating a model.



## Moving average models

Rather than using past values of the forecast variable in a regression, a moving average model uses past forecast errors in a regression-like model.

![image-20191103130139588](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191103130139588.png)

where εtεt is white noise. We refer to this as an **MA(q) model**, a moving average model of order q. Of course, we do not *observe* the values of εtεt, so it is not really a regression in the usual sense.

Notice that each value of yt can be thought of as a weighted moving average of the past few forecast errors. However, moving average *models* should not be confused with the moving average *smoothing* we discussed in Chapter [6](https://otexts.com/fpp2/decomposition.html#decomposition). A moving average model is used for forecasting future values, while moving average smoothing is used for estimating the trend-cycle of past values.

 ![Two examples of data from moving average models with different parameters. Left: MA(1) with $y_t = 20 + \varepsilon_t + 0.8\varepsilon_{t-1}$. Right: MA(2) with $y_t = \varepsilon_t- \varepsilon_{t-1}+0.8\varepsilon_{t-2}$. In both cases, $\varepsilon_t$ is normally distributed white noise with mean zero and variance one.](https://otexts.com/fpp2/fpp_files/figure-html/maq-1.png) 

It is possible to write any stationary AR(p) model as an MA(∞) model. For example, using repeated substitution, we can demonstrate this for an AR(1) model: 

![image-20191103130218385](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191103130218385.png)



 Provided −1<ϕ1<1, the value of ϕ1k will get smaller as k gets larger. So eventually we obtain 

![image-20191103130224060](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191103130224060.png)

an MA(∞) process.

The reverse result holds if we impose some constraints on the MA parameters. Then the MA model is called **invertible**. That is, we can write any invertible MA(q) process as an AR(∞) process. Invertible models are not simply introduced to enable us to convert from MA models to AR models. They also have some desirable mathematical properties.

The invertibility constraints for other models are similar to the stationarity constraints.

- For an MA(1) model: −1<θ1<1.
- For an MA(2) model: −1<θ2<1,  θ2+θ1>−1, θ1−θ2<1.

More complicated conditions hold for q≥3q≥3. Again, R will take care of these constraints when estimating the models.



## Non-seasonal ARIMA models

If we combine differencing with autoregression and a moving average model, we obtain a non-seasonal ARIMA model. ARIMA is an acronym for AutoRegressive Integrated Moving Average (in this context, “integration” is the reverse of differencing). The full model can be written as:

![image-20191103130508521](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191103130508521.png)

where y'_t is the differenced series (it may have been differenced more than once). The “predictors” on the right hand side include both lagged values of yt and lagged errors. We call this an **ARIMA(p,d,q) model**, where

|      |                                        |
| ---: | :------------------------------------- |
|   p= | order of the autoregressive part;      |
|   d= | degree of first differencing involved; |
|   q= | order of the moving average part.      |

The same stationarity and invertibility conditions that are used for autoregressive and moving average models also apply to an ARIMA model.

| Model                  | Designation                   |
| ---------------------- | ----------------------------- |
| White noise            | ARIMA(0,0,0)                  |
| Random walk            | ARIMA(0,1,0) with no constant |
| Random walk with drift | ARIMA(0,1,0) with a constant  |
| Autoregression         | ARIMA(p,0,0)                  |
| Moving average         | ARIMA(0,0,q)                  |



### ACF and PACF plots

It is usually not possible to tell, simply from a time plot, what values of pp and qq are appropriate for the data. However, it is sometimes possible to use the ACF plot, and the closely related PACF plot, to determine appropriate values for pp and qq.

Recall that an ACF plot shows the autocorrelations which measure the relationship between ytyt and yt−kyt−k for different values of kk. Now if ytyt and yt−1yt−1 are correlated, then yt−1yt−1 and yt−2yt−2 must also be correlated. However, then ytyt and yt−2yt−2 might be correlated, simply because they are both connected to yt−1yt−1, rather than because of any new information contained in yt−2yt−2 that could be used in forecasting ytyt.

To overcome this problem, we can use **partial autocorrelations**. These measure the relationship between ytyt and yt−kyt−k after removing the effects of lags 1,2,3,…,k−11,2,3,…,k−1. So the first partial autocorrelation is identical to the first autocorrelation, because there is nothing between them to remove. Each partial autocorrelation can be estimated as the last coefficient in an autoregressive model. Specifically, αkαk, the kkth partial autocorrelation coefficient, is equal to the estimate of ϕkϕk in an AR(kk) model. In practice, there are more efficient algorithms for computing αkαk than fitting all of these autoregressions, but they give the same results.

Figures [8.9](https://otexts.com/fpp2/non-seasonal-arima.html#fig:usconsumptionacf) and [8.10](https://otexts.com/fpp2/non-seasonal-arima.html#fig:usconsumptionpacf) shows the ACF and PACF plots for the US consumption data shown in Figure [8.7](https://otexts.com/fpp2/non-seasonal-arima.html#fig:usconsumption). The partial autocorrelations have the same critical values of ±1.96/√T±1.96/T as for ordinary autocorrelations, and these are typically shown on the plot as in Figure [8.9](https://otexts.com/fpp2/non-seasonal-arima.html#fig:usconsumptionacf).

 ![ACF of quarterly percentage change in US consumption.](https://otexts.com/fpp2/fpp_files/figure-html/usconsumptionacf-1.png) 

 ![PACF of quarterly percentage change in US consumption.](https://otexts.com/fpp2/fpp_files/figure-html/usconsumptionpacf-1.png) 

If the data are from an ARIMA(pp,dd,0) or ARIMA(0,dd,qq) model, then the ACF and PACF plots can be helpful in determining the value of p or q. If p and q are both positive, then the plots do not help in finding suitable values of p and q.

The data may follow an ARIMA(p,d,0) model if the ACF and PACF plots of the differenced data show the following patterns:

- the ACF is exponentially decaying or sinusoidal;
- there is a significant spike at lag p in the PACF, but none beyond lag p.

The data may follow an ARIMA(0,d,q) model if the ACF and PACF plots of the differenced data show the following patterns:

- the PACF is exponentially decaying or sinusoidal;
- there is a significant spike at lag q in the ACF, but none beyond lag q.

In Figure [8.9](https://otexts.com/fpp2/non-seasonal-arima.html#fig:usconsumptionacf), we see that there are three spikes in the ACF, followed by an almost significant spike at lag 4. In the PACF, there are three significant spikes, and then no significant spikes thereafter (apart from one just outside the bounds at lag 22). We can ignore one significant spike in each plot if it is just outside the limits, and not in the first few lags. After all, the probability of a spike being significant by chance is about one in twenty, and we are plotting 22 spikes in each plot. The pattern in the first three spikes is what we would expect from an ARIMA(3,0,0), as the PACF tends to decrease. So in this case, the ACF and PACF lead us to think an ARIMA(3,0,0) model might be appropriate.