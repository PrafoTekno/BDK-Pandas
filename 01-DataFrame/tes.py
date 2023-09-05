
import pandas as pd
import numpy as np

a = np.array ([1,2,3])

data = pd.DataFrame (a)
print (data)

siswa = {"Nama":["Agus", "Udin", "Asep"],
         "Jurusan":["elektro", "sipil", "industri"],
         "Angkatan": [2020, 2021, 2022]}

data1 = pd.DataFrame (siswa)
print (f"\n{data1}")
