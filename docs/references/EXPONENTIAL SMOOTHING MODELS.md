

## Exponential smoothing models



Source:

 https://otexts.com/fpp2/expsmooth.html 



**SUMMARY TABLES:**

|                       | Seasonal Component |              |                    |
| :-------------------- | :----------------- | :----------- | :----------------- |
| **Trend Component**   | N (None)           | A (Additive) | M (Multiplicative) |
| N (None)              | (N,N)              | (N,A)        | (N,M)              |
| A (Additive)          | (A,N)              | (A,A)        | (A,M)              |
| Add (Additive damped) | (Add,N)            | (Add,A)      | (Add,M)            |

| Short hand | Method                              |
| :--------- | :---------------------------------- |
| (N,N)      | Simple exponential smoothing        |
| (A,N)      | Holt’s linear method                |
| (Add,N)    | Additive damped trend method        |
| (A,A)      | Additive Holt-Winters’ method       |
| (A,M)      | Multiplicative Holt-Winters’ method |
| (Add,M)    | Holt-Winters’ damped method         |

 ![img](https://otexts.com/fpp2/pegelstable.png) 





**MULTIPLICATIVE OR ADITIVE ERRORS::**

ADITIVES					![image-20191102142847679](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191102142847679.png)

 MULTIPLICATIVES![image-20191102142628797](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191102142628797.png)



![img](https://otexts.com/fpp2/statespacemodels.png)



 **VARIANCE:**

![image-20191102144528872](C:\Users\Illan\AppData\Roaming\Typora\typora-user-images\image-20191102144528872.png)



 