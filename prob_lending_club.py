import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)

loansData.boxplot(column='Amount.Funded.By.Investors')
plt.title('Lending Data Boxplot')
plt.savefig('lending-box.png')

loansData.hist(column='Amount.Funded.By.Investors')
plt.title('Lending Data Historgram')
plt.savefig('lending-hist.png')

plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.title('Lending Data QQ-plot')
plt.savefig('lending-qq.png')

