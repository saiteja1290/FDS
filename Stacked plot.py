import matplotlib.pyplot as plt
import pandas as pd

df=pd.DataFrame({'Product A':[45,56,47],'Product B':[65,45,78],'Product C':[99,84,47]})
df.index=['Strategy 1','Strategy 2','Strategy 3']
df.plot(stacked=True,kind='bar')
plt.show()
