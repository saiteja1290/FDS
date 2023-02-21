import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_excel('marks.xlsx')
#df.plot.box()

plt.boxplot(df[['Maths','Telugu']])
plt.show()

