import numpy as np
import pandas as pd

file = '/home/makanu/ownCloud/UmsaetzeSpardaBank/umsaetze-77593-2021-12-01-21-44-31.csv'

'''with open(file, encoding="ISO-8859-1") as fp:

    skip = next(filter(
        lambda x: x[1].startswith('Buchungstag'),
        enumerate(fp)
    ))[0]'''

df = pd.read_csv(file, skiprows=11, encoding="ISO-8859-1")

print(df)