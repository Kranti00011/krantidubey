import pandas as pd
data = pd.read_csv("rd.dat")
print(data.head(5))
export_csv  = data.to_csv(r'testout1.csv')
