# Otlier-Analysis
IQR vs. DFFITS: Complementary strategies for identifying outliers in Python

The presence of outliers in data sets can significantly compromise the quality of statistical analyses and predictive models. This code analyzes the detection of outliers using the Interquartile Range (IQR) method, the DFFITS (Difference in Fits) metric, and the combination of both.

The IQR method is applied in the preprocessing phase to identify and remove univariate extreme values, while DFFITS is used after the adjustment of linear regression models, with the aim of detecting observations with a disproportionate influence on the adjusted values.
