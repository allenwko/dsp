[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

Actual mean: 1.02 children/household
Biased mean: 2.40 children/household

The data shows a very significant bias if the children were to report the data. This is in large part because households without children are unable to report themselves. Oversampling of high children households also adds to the effect.

Python code below:

import thinkstats2, chap01soln, thinkplot

def BiasPmf(pmf, label=''):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x,x)

    new_pmf.Normalize()
    return new_pmf

resp = chap01soln.ReadFemResp()

child_data = resp['numkdhh']
child_pmf = thinkstats2.Pmf(child_data, label = 'Actual')
biased_child_pmf = BiasPmf(child_pmf, label = 'Observed')

thinkplot.PrePlot(2)
thinkplot.Pmfs([child_pmf, biased_child_pmf])
thinkplot.Show(xlabel = 'Amount of Children', ylabel = 'PMF')

print 'Unbiased Mean:', child_pmf.Mean()
print 'Biased Mean:', biased_child_pmf.Mean()
