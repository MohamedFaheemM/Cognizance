import pandas as pd
import numpy as np

series = pd.Series(['welcome', 'to', 'cognizance',
                    'python', 'task'])
print("Series:")

print("")

print(series)

CapSeries = series.str.title()
  
# Print the resulting series
print("\nResulting Series :")
CapSeries

print("")

X = np.array(CapSeries)
print(*X, sep= ' ')


