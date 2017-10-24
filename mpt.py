# from https://github.com/yhilpisch/py4fi/blob/master/ipython3/11_Statistics_a.ipynb

import numpy as np
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
%matplotlib inline

symbols = ['AAPL', 'MSFT', 'YHOO', 'DB', 'GLD']
noa = len(symbols)

data = pd.DataFrame()
for sym in symbols:
    data[sym] = web.DataReader(sym, data_source='google',
                               end='2014-09-12')['Close']
data.columns = symbols

(data / data.ix[0] * 100).plot(figsize=(8, 5), grid=True)
# tag: portfolio_1
# title: Stock prices over time
# size: 90

rets = np.log(data / data.shift(1))

rets.mean() * 252

rets.cov() * 252
