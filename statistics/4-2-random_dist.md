[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

The distribution of the CDF shows a straight line, with some noise from randomness. Going from 1000 random values to 10,000 random values reduces noise and improves the smoothness of the CDF.


Python code below:

import thinkstats2, thinkplot, random

random_values = []
for i in range(0, 1000):
    random_values.append(random.random())

random_pmf = thinkstats2.Pmf(random_values, label ='random')

thinkplot.PrePlot(2)
thinkplot.Pmfs([random_pmf])
thinkplot.Show()

random_cdf = thinkstats2.Cdf(random_values)
thinkplot.Cdfs([random_cdf])
thinkplot.Show()

t = [random.random() for _ in range(10000)]
cdf = thinkstats2.Cdf(t)
thinkplot.Cdfs([cdf])
thinkplot.Show()

