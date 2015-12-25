import pandas as pd
import datetime
import pandas.io.data as web
import matplotlib.pyplot as plt
from matplotlib import style


start = datetime.datetime(2010,1,1)
end = datetime.datetime(2015,12,25)

df = web.DataReader("EMC", "yahoo", start, end)

print(df)
print(df.head())

df['High'].plot()
plt.legend()
plt.show()


