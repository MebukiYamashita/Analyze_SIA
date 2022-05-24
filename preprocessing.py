import pandas as pd
import numpy as np
import seaborn as sb

df = pd.read_csv('./starbucks.csv', encoding = 'cp949')
df["주소"] = df["주소"].str.replace(pat=r'[^\w]', repl=r'', regex=True)
df["지역"] = df["주소"].str.split(" ".str[0])
