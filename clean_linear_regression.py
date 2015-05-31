import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loansData['Interest.Rate'] = cleanInterestRate

cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip('months')))

loansData['Loan.Length'] = cleanLoanLength
 
cleanFICORange = loansData['FICO.Range'].map(lambda x: int(x.split('-')[0]))

loansData['FICO.Range'] = cleanFICORange

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Range']

y = np.matrix(intrate).transpose() #this is because python does multiplication in rows and not columns

x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y, X)
f = model.fit()

print f.summary()

loansData.to_csv('loansData_clean.csv', header=True, index=False)


