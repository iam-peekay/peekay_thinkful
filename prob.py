import collections
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

#data in this lesson
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9] 

#frequency
c = collections.Counter(x)

print c

count_sum = sum(c.values())

for k,v in c.iteritems():
	print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)

#boxplot
plt.boxplot(x)
plt.title('BoxPlot')
plt.savefig('prob-boxplot.png')

#histogram
plt.hist(x)
plt.title('Histogram')
plt.savefig('prob-hist.png')

#QQ plot
stats.probplot(x, dist="norm", plot=plt)
plt.savefig('prob-qq.png')