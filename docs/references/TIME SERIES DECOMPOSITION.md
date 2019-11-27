## Time series decomposition



Source:

 https://otexts.com/fpp2/decomposition.html 



## Time series components

If we assume an additive decomposition, then we can write

![image-20191103123817392](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191103123817392.png)

 is the data, St is the seasonal component, Tt is the trend-cycle component, and Rt is the remainder component, all at period t. Alternatively, a multiplicative decomposition would be written 

![image-20191103123825759](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191103123825759.png)

The additive decomposition is the most appropriate if the magnitude of the seasonal fluctuations, or the variation around the trend-cycle, does not vary with the level of the time series. When the variation in the seasonal pattern, or the variation around the trend-cycle, appears to be proportional to the level of the time series, then a multiplicative decomposition is more appropriate. Multiplicative decompositions are common with economic time series.

An alternative to using a multiplicative decomposition is to first transform the data until the variation in the series appears to be stable over time, then use an additive decomposition. When a log transformation has been used, this is equivalent to using a multiplicative decomposition because

![image-20191103123832014](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191103123832014.png)

is equivalent to

![image-20191103123838413](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191103123838413.png)

 ![The electrical equipment orders (top) and its three additive components.](https://otexts.com/fpp2/fpp_files/figure-html/elecequip-stl-1.png) 



## Moving averages



### Moving average smoothing

![image-20191103124043631](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191103124043631.png)

 where m=2k+1. That is, the estimate of the trend-cycle at time t is obtained by averaging values of the time series within k periods of t. Observations that are nearby in time are also likely to be close in value. Therefore, the average eliminates some of the randomness in the data, leaving a smooth trend-cycle component. We call this an **m-MA**, meaning a moving average of order m. 



 ![Different moving averages applied to the residential electricity sales data.](https://otexts.com/fpp2/fpp_files/figure-html/ressales3-1.png) 

### Moving averages of moving averages

It is possible to apply a moving average to a moving average. One reason for doing this is to make an even-order moving average symmetric.

For example, we might take a moving average of order 4, and then apply another moving average of order 2 to the results.

![image-20191103124156126](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191103124156126.png)

**This is the same as a the trapezoidal integration method.**



### Estimating the trend-cycle with seasonal data

The most common use of centred moving averages is for estimating the trend-cycle from seasonal data. Consider the 2×4-MA:

![image-20191103124431048](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191103124431048.png)



In general, a 2×m-MA is equivalent to a weighted moving average of order m+1 where all observations take the weight 1/m, except for the first and last terms which take weights 1/(2m). 

So, if the seasonal period is even and of order m, we use a 2×m-MA to estimate the trend-cycle. If the seasonal period is odd and of order m, we use a m-MA to estimate the trend-cycle. For example, a 2×12-MA can be used to estimate the trend-cycle of monthly data and a 7-MA can be used to estimate the trend-cycle of daily data with a weekly seasonality.

Other choices for the order of the MA will usually result in trend-cycle estimates being contaminated by the seasonality in the data.



### Decomposition of the series



### Additive decomposition

- Step 1

  If m is an even number, compute the trend-cycle component using a 2×m-MA. If mm is an odd number, compute the trend-cycle component  using an m-MA.

- Step 2

  Calculate the detrended series: ![image-20191103124601189](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191103124601189.png)

- Step 3

  To estimate the seasonal component for each season, simply average the detrended values for that season. For example, with monthly data, the seasonal component for March is the average of all the detrended March values in the data. These seasonal component values are then adjusted to ensure that they add to zero. The seasonal component is obtained by stringing together these monthly values, and then replicating the sequence for each year of data. This gives ^StS^t.

- Step 4

  The remainder component is calculated by subtracting the estimated seasonal and trend-cycle components: ![image-20191103124632922](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191103124632922.png)

  

### Multiplicative decomposition

A classical multiplicative decomposition is similar, except that the subtractions are replaced by divisions.

- Step 1

  If m is an even number, compute the trend-cycle component using a 2×m-MA. If mm is an odd number, compute the trend-cycle component using an m-MA.

- Step 2

  Calculate the detrended series:![image-20191103124727427](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191103124727427.png)

- Step 3

  To estimate the seasonal component for each season, simply average the detrended values for that season. For example, with monthly data, the seasonal index for March is the average of all the detrended March values in the data. These seasonal indexes are then adjusted to ensure that they add to mm. The seasonal component is obtained by stringing together these monthly indexes, and then replicating the sequence for each year of data. 

- Step 4

  The remainder component is calculated by dividing out the estimated seasonal and trend-cycle components:![image-20191103124736567](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191103124736567.png)