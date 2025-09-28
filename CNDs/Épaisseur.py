import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import find_peaks


df = pd.read_csv("CNDs/3.1.1 Mesure épaisseur/3.11 Mesure Little plaque.csv",comment='%',skip_blank_lines=True)
df.rename(columns={df.columns[0]: 'Time', df.columns[1]: 'Voltage'}, inplace=True) 
df = df.iloc[400:800]

df_out = df.iloc[0:100]
df_reflechi = df.iloc[100:200]
plt.plot(df_reflechi['Time'], df_reflechi['Voltage'], label="Signal direct")
plt.show()
peaks_out, _ = find_peaks(df_out['Voltage'], height=-0.03)
peaks_reflechi, _ = find_peaks(df_reflechi['Voltage'], height=-0.02)

peak_times_out = df_out['Time'].iloc[peaks_out]
peak_times_reflechi = df_reflechi['Time'].iloc[peaks_reflechi]

print(peak_times_out)
print(peak_times_reflechi)

epaisseurs = []
for i, t_reflechi in enumerate(peak_times_reflechi.values):
    epaisseurs.append((t_reflechi - peak_times_out.values[i])*6300*1000)
epaisseur = np.mean(epaisseurs)
std_epaisseur = np.std(epaisseurs)

print("Épaisseur mesurée : ", epaisseur, '±', std_epaisseur, " mm")

plt.plot(df['Time'], df['Voltage'], label="Original signal")
plt.legend()
plt.show()