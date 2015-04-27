import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

data = data.splitlines()

data = [i.split(', ') for i in data]

column_names = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

alcohol_mean = df['Alcohol'].mean()

alcohol_median = df['Alcohol'].median()

alcohol_mode = stats.mode(df['Alcohol'])


tobacco_mean = df['Tobacco'].mean()

tobacco_median = df['Tobacco'].median()

tobacco_mode = stats.mode(df['Tobacco'])


alcohol_range = max(df['Alcohol']) - min(df['Alcohol'])

alcohol_standard_deviation = df['Alcohol'].std()

alcohol_variance = df['Alcohol'].var()

tobacco_range = max(df['Tobacco']) - min(df['Tobacco'])

tobacco_standard_deviation = df['Tobacco'].std()

tobacco_variance = df['Tobacco'].var()

print "The mean for the Alcohol and Tobacco dataset is {} {}".format(alcohol_mean, tobacco_mean)
print "The median for the Alcohol and Tobacco dataset is {} {}".format(alcohol_median, tobacco_median)
print "The mode for the Alcohol and Tobacco dataset is {} {}".format(alcohol_mode, tobacco_mode)
print "The range for the Alcohol and Tobacco dataset is {} {}".format(alcohol_range, tobacco_range)
print "The standard deviation for the Alcohol and Tobacco dataset is {} {}".format(alcohol_standard_deviation, tobacco_standard_deviation)
print "The variance for the Alcohol and Tobacco dataset is {} {}".format(alcohol_variance, tobacco_variance)