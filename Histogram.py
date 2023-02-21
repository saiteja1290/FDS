import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_excel('marks.xlsx')

#of a sigle attribute
plt.hist(df['Maths'])
plt.show()

#complete
df.hist()
plt.show()
