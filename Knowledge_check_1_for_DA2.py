# Knowledge check 1 for DA2 
import pandas as pd
import _json
import requests
import numpy
r = requests.get('https://api.publicapis.org/entries')
data = r.json()
entries = data
df = pd.DataFrame(entries)
df.head (10)
df.describe()
df.count()
df.iloc[4:10]