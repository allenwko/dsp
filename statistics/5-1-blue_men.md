[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

34.3% of men in the US are in the correct height range to qualify to join the Blue Men group. 


Python code below:

import brfss, scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc = mu, scale = sigma)

low_height = (5*12+10)*2.54
hi_height = (6*12+1)*2.54
bman = dist.cdf(hi_height) - dist.cdf(low_height)
print "The percent of men in this height range is:", bman*100, "%"
