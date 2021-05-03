import pandas as pd

df = pd.read_csv('detail.csv', parse_dates=["Absolute Time"], index_col="Absolute Time")

df = df.resample('T').mean()

df.to_csv('detailDownsampled.csv')
print(df.info())



df = pd.read_csv('detailVol.csv', parse_dates=["Realtime"], index_col="Realtime")

df = df.resample('T').mean()

df.to_csv('detailVolDownsampled.csv')
print(df.info())



df = pd.read_csv('detailTemp.csv', parse_dates=["Realtime"], index_col="Realtime")

df = df.resample('T').mean()

df.to_csv('detailTempDownsampled.csv')
print(df.info())
