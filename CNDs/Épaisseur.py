import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import find_peaks


df = pd.read_csv("CNDs/3.1.1 Mesure épaisseur/3.1.1 Épaisseur BigPLaque.csv",comment='%',skip_blank_lines=True)
df.rename(columns={df.columns[0]: 'Time', df.columns[1]: 'Voltage'}, inplace=True) 
df = df.iloc[400:800]

df_out = df.iloc[0:200]
df_reflechi = df.iloc[200:400]
peaks_out, _ = find_peaks(df_out['Voltage'], height=-0.03)
peaks_reflechi, _ = find_peaks(df_reflechi['Voltage'], height=-0.02)

peak_times_out = df_out['Time'].iloc[peaks_out]
peak_times_reflechi = df_reflechi['Time'].iloc[peaks_reflechi]

print(peak_times_out)
print(peak_times_reflechi)

epaisseurs = []
for i, t_reflechi in enumerate(peak_times_reflechi.values):
    epaisseurs.append((t_reflechi - peak_times_out.values[i])*6300*1000)
epaisseur = np.mean(epaisseurs)/2
std_epaisseur = np.std(epaisseurs)/2

print("Épaisseur mesurée : ", epaisseur, '±', std_epaisseur, " mm")

plt.plot(df['Time']*1e6, df['Voltage'], 'k-', label="Signal mesuré")
for i, peak in enumerate(peaks_out):
    label = "Pics incidents" if i == 0 else None
    plt.plot(df['Time'].iloc[peak]*1e6, df['Voltage'].iloc[peak], "ko", markersize=4, label=label)
for i, peak in enumerate(peaks_reflechi):
    label = "Pics réfléchis" if i == 0 else None
    plt.plot(df['Time'].iloc[peak+200]*1e6, df['Voltage'].iloc[peak+200], "o", markerfacecolor='none', markeredgecolor='black', markersize=4, label=label)
    
plt.legend()
plt.xlabel("Temps (μs)")
plt.ylabel("Voltage (V)")
plt.show()
################## Nouveau code pour la petite plaque #####################

plt.cla()
df_ref = pd.read_csv("CNDs/3.1.1 Mesure épaisseur/3.1.1 mesure REF.csv",comment='%',skip_blank_lines=True)
df_ref.rename(columns={df_ref.columns[0]: 'Time', df_ref.columns[1]: 'Voltage'}, inplace=True) 
df_ref = df_ref.iloc[400:800]

df_little = pd.read_csv("CNDs/3.1.1 Mesure épaisseur/3.1.1 Épaisseur Little Plaque.csv",comment='%',skip_blank_lines=True)
df_little.rename(columns={df_little.columns[0]: 'Time', df_little.columns[1]: 'Voltage'}, inplace=True) 
df_little = df_little.iloc[400:800]



df_ref = df_ref.iloc[0:100]
df_little = df_little.iloc[0:100]
peaks_out, _ = find_peaks(df_ref['Voltage'], height=-0.03)
peaks_reflechi, _ = find_peaks(df_little['Voltage']-df_ref['Voltage'], height=-0.02)

print(peaks_reflechi)


peak_times_out = df_ref['Time'].iloc[peaks_out]
peak_times_reflechi = df_little['Time'].iloc[peaks_reflechi]
peak_times_reflechi = peak_times_reflechi[12:]




epaisseurs = []
n = min(len(peak_times_reflechi.values), len(peak_times_out.values))

for i in range(4):
    epaisseurs.append((peak_times_reflechi.values[i] - peak_times_out.values[i]) * 6300 * 1000)
    
epaisseur = np.mean(epaisseurs)/2
std_epaisseur = np.std(epaisseurs)/2

print("Épaisseur mesurée : ", epaisseur, '±', std_epaisseur, " mm")

plt.plot(df_ref['Time']*1e6, df_ref['Voltage'], 'k-', label="Signal de référence")
plt.plot(df_ref['Time']*1e6, df_little['Voltage'] - df_ref['Voltage'], 'k--', label="Signal de la plaque - Référence")
for i, peak in enumerate(peaks_out):
    label = "Pics incidents" if i == 0 else None
    if i < 4:
        plt.plot(df_ref['Time'].iloc[peak]*1e6, df_ref['Voltage'].iloc[peak], "ko", markersize=4, label=label)
for i, peak in enumerate(peak_times_reflechi.index-400):
    label = "Pics réfléchis" if i == 0 else None
    if i < 4:
        plt.plot(df_little['Time'].iloc[peak]*1e6, df_little['Voltage'].iloc[peak] - df_ref['Voltage'].iloc[peak], "o", markerfacecolor='none', markeredgecolor='black', markersize=4, label=label)
    
plt.legend()
plt.xlabel("Temps (μs)")
plt.ylabel("Voltage (V)")
plt.show()

liste_index = [1,2,3,4]
liste_epaisseurs = [1.8270477, 24.675, 13.251, 40.236]
liste_std = [0.1408722,0.134466, 0.134466, 0.059397]
