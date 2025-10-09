import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import find_peaks


df = pd.read_csv("CNDs/3.1.4 Atténuation/3.1.4 ptit acrylique.csv",comment='%', skip_blank_lines=True)
df.rename(columns={df.columns[0]: 'Time', df.columns[1]: 'Voltage'}, inplace=True) 
df = df.iloc[0:800]
df_out = df.iloc[0:400]
df_reflechi = df.iloc[400:800]
peaks_out, _ = find_peaks(df_out["Voltage"], height=-0.03)
peaks_reflechi, _ = find_peaks(df_reflechi["Voltage"], height=-0.02)
print(df_out)

peak_times_out = df_out["Time"].iloc[peaks_out]
peak_times_reflechi = df_reflechi["Time"].iloc[peaks_reflechi]


epaisseurs = []
if len(peaks_out) < len(peaks_reflechi):
    peak_times_reflechi = peak_times_reflechi[:len(peak_times_out)]
for j, t_reflechi in enumerate(peak_times_reflechi.values):
        epaisseurs.append((t_reflechi - peak_times_out.values[j]) * 6300*1000)

        
epaisseur = np.mean(epaisseurs)/2
std_epaisseur = np.std(epaisseurs)/2

print("Épaisseur mesurée : ", epaisseur, '±', std_epaisseur, " mm")
#Afficher les graphiques et leurs points:
plt.plot(df["Time"]*1e6, df["Voltage"])
# Ligne verticale pour démarcation entre df_out et df_reflechi
time_sep = df["Time"].iloc[400] * 1e6
plt.axvline(x=time_sep, color='gray', linestyle='--', label='Séparation out/réfléchi')
print(f"L'amplitude envoyée est de {df["Voltage"].iloc[peaks_out[0]]}V.")
print(f"L'amplitude réfléchie est de {np.abs(df["Voltage"].iloc[peaks_reflechi[0]])}V.")

coeff = (20/epaisseur) * np.log10(df["Voltage"].iloc[peaks_out[0]]/np.abs(df["Voltage"].iloc[peaks_reflechi[0]]))

print(coeff)
#plt.axvline(df_ou}")
plt.show()