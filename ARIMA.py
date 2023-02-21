from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
from matplotlib import pyplot

series=pd.read_csv('shampoo_sales.csv',header=0,parse_dates=[0],index_col=0,squeeze=True)
model=ARIMA(series,order=(5,1,0))
model_fit=model.fit()
print(model_fit.summary())
residuals=pd.DataFrame(model_fit.resid)
residuals.plot()
pyplot.ylabel("Sales")
pyplot.show()
residuals.plot(kind='kde')
pyplot.show()
print(residuals.describe())
