''' NOTE: data is regular stock data, 'date' is in first column
date,open,high,low,close,adj_close,volume
2006-05-01,36.520000,39.720001,35.869999,38.849998,35.961147,3002800
2006-06-01,37.200001,40.270000,31.820000,38.700001,35.822296,13361400
'''

# How to handle dates in a CSV file

# 'date' will be read as 'object' (string)
data = pd.read_csv("test.csv", encoding='utf-8')

# 'date' is read as pandas datetime (datetime64[ns])
data = pd.read_csv("test.csv", parse_dates=['date'], encoding='utf-8')

# 'date' becomes index, but as 'object' (string)
data = pd.read_csv("test.csv", index_col='date', encoding='utf-8')

# 'date' becomes index, as DatetimeIndex (datetime64[ns])
data = pd.read_csv("test.csv", index_col='date', parse_dates=True, encoding='utf-8')
