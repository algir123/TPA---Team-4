import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("CNDs/3.1.1 Mesure épaisseur/3.1.1 Épaisseur BigPLaque.csv",comment='%',skip_blank_lines=True)
df.rename(columns={df.columns[0]: 'Time', df.columns[1]: 'Voltage'}, inplace=True) 
df = df.iloc[400:800]

plt.plot(df['Time'], df['Voltage'])
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.show()