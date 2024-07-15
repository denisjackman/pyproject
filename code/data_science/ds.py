'''
ds.py

This is a website traffic forcasting example.
It is based on
https://thecleverprogrammer.com/2022/06/28/website-traffic-forecasting-using-python/
'''

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.00 $"
__date__ = "$Date: 2022/07/04 12:03:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv(r"Z:/Resources/excel/Thecleverprogrammer.csv")
print(data.head())
data["Date"] = pd.to_datetime(data["Date"],
                              format="%d/%m/%Y")
print(data.info())
plt.style.use('fivethirtyeight')
plt.figure(figsize=(15, 10))
plt.plot(data["Date"], data["Views"])
plt.title("Daily Traffic of Thecleverprogrammer.com")
plt.show()


# result = seasonal_decompose(data["Views"],
#                             model='multiplicative',
#                            freq=30)
# fig = plt.figure()
# fig = result.plot()
# fig.set_size_inches(15, 10)
