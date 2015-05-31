import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

# load data
loansData = pd.read_csv('LoanStats_MR.csv')

loansData = loansData[['int_rate', 'annual_inc', 'home_ownership']]

# clean data
loansData.dropna(subset=['annual_inc'], inplace=True)

loansData['int_rate'] = loansData['int_rate'].map(lambda x: round(float(x.strip('%')) / 100, 4))

loansData['annual_inc'] = loansData['annual_inc'].map(lambda x: int(x))

loansData['log10_inc'] = loansData['annual_inc'].map(lambda x: np.log10(x))

# model data

intrate = loansData['int_rate']
annualincomelog = loansData['log10_inc']

y = np.matrix(intrate).transpose()
x = np.matrix(annualincomelog).transpose()

X = sm.add_constant(x)

# Linear model
est = sm.OLS(y, X).fit()

X_prime = np.linspace(annualincomelog.min(), annualincomelog.max(), 100)
plt.figure()
plt.scatter(x, y, alpha=0.3)
plt.xlabel("Log of Annual Income")
plt.ylabel("Interest Rate")
plt.plot(est.params[0] + est.params[1]*X_prime, 'r')
plt.draw()
plt.savefig('intrate_vs_income.png')

loansData['home_dummy'] = pd.Categorical(loansData.home_ownership).labels

est2 = smf.ols(formula="int_rate ~ home_dummy + log10_inc", data=loansData).fit()
print est2.summary()

loansData['home_dummy'] = pd.Categorical(loansData.home_ownership).labels

est3 = smf.ols(formula="int_rate ~ home_dummy*log10_inc", data=loansData).fit()
print est3.summary()
