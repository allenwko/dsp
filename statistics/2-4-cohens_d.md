[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Cohen's d = -0.089 standard deviations. According to this statistic, the effect size of being born first is relatively minor. 

Python code below:

import nsfg
import thinkstats2 as ts

df = nsfg.ReadFemPreg()
firsts = df[df.birthord==1]
others = df[df.birthord>1]

d = ts.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)

print d
