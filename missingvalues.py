import pandas as pd
import ftfy
import numpy as np
import json

# df = pd.read_csv"./allocations_2018615.csv"(, sep=',', delimiter=None, header='infer',  encoding = 'utf-8')
df = pd.read_json("./organization.json", encoding = 'utf-8')
print(df.head())
print(len(df.index))
print( df.isnull().sum())