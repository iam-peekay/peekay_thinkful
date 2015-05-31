import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

loansData = pd.read_csv('loansData_clean.csv')

loansData['IR_TF'] = loansData['Interest.Rate'].map(lambda x: (1 if x >= .12 else 0))

loansData['Intercept'] = 1

ind_vars = ['Amount.Requested', 'FICO.Range', 'Intercept']

logit = sm.Logit(loansData['IR_TF'], loansData[ind_vars])

result = logit.fit()

coeff = result.params
print coeff 

ficoscore = int(raw_input('Enter a FICO score: '))
loanamount = int(raw_input('Enter amount of loan: '))

def logistic_function(ficoscore, loanamount, coeff):
	p = 1/(1 + np.exp(coeff[2] + coeff[1]*ficoscore + coeff[0]*loanamount))
	return p

def prediction(ficoscore, loanamount, coeff):
	p = logistic_function(ficoscore, loanamount, coeff)
	if p >= 0.7:
		print("Congrats! You will get the loan!")
	else:
		print("Sorry, your FICO score does not qualify you for this loan.")
		
prediction(ficoscore, loanamount, coeff)

x = np.arange(500,900,1)
y = 1/(1 + np.exp(coeff[2] + coeff[1]*ficoscore + coeff[0]*loanamount))
plt.figure()
plt.plot(x,y)
plt.draw()
plt.savefig('logistic_function.png')





