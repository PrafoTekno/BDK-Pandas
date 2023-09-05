
import pandas as pd
import numpy as np

makanan = {"nama": ["nasi goreng", "mie goreng", "seblak"],
           "jumlah": [8, 9, 7],
           "panas" : [True, False, True],
           "jenis" : ["nasi", "mie", "kuah"]}

data = pd.DataFrame (makanan)
print (f"Ini tabel makanan mula-mula\n\n {data}\n")

print (f"Hanya ambil kolom nama dan panas\n\n {data[['nama', 'panas']]}")

#Menggunakan loc [baris, kolom]

index = ["Row 1", "Row 2", "Row 3"]

data.index = index
print (f"\n\n{data}\n\n")

print (f"\n\n Ambil hanya nasi goreng: \n{data.loc['Row 1', 'nama']}\n\n")
print (f"Ambil nama dan jumlah saja: \n{data.loc[:, ['nama', 'jumlah']]}\n\n")

print (f"Dengan loc: \n{data.loc['Row 1':'Row 2']}\n\n")
print (f"Dengan iloc: \n{data.iloc[0:3]}\n\n")



