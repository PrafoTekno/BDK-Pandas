
import pandas as pd
import numpy as np

makanan = {"nama": ["nasi goreng", "mie goreng", "seblak"],
           "jumlah": [8, 9, 7],
           "panas" : [True, False, True],
           "jenis" : ["nasi", "mie", "kuah"]}

data = pd.DataFrame (makanan)

print ("\n\n")

for i,j in data.iterrows():
    print (f"{i,j}\n\n")


kolom = list (data)

for i in kolom:
    print (data[i][0])



