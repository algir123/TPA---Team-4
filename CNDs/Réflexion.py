import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import find_peaks

liste_fichier = [ _ for _ in range(1, 8)]

for i in liste_fichier:
    df = pd.read_csv("CNDs/3.1.2 rÉFLEXION/3.1.2 " + f"{i}.csv",comment='%', skip_blank_lines=True)
    df.rename(columns={df.columns[0]: 'Time', df.columns[1]: 'Voltage'}, inplace=True) 
    df = df.iloc[000:800]
    df_out = df.iloc[0:400]
    df_reflechi = df.iloc[400:800]
    peaks_out, _ = find_peaks(df_out["Voltage"], height=-0.03)
    peaks_reflechi, _ = find_peaks(df_reflechi["Voltage"], height=0.00005)

    peak_times_out = df_out["Time"].iloc[peaks_out]
    peak_times_reflechi = df_reflechi["Time"].iloc[peaks_reflechi]
    print(f"point: {i - 0}")
    print(peak_times_out)
    print(peak_times_reflechi)


    epaisseurs = []
    for j, t_reflechi in enumerate(peak_times_reflechi.values):
        epaisseurs.append((t_reflechi - peak_times_out.values[j]) * 6300*1000)
    epaisseur = np.mean(epaisseurs)/2
    std_epaisseur = np.std(epaisseurs)/2

    print("Épaisseur mesurée : ", epaisseur, '±', std_epaisseur, " mm")
    #Afficher les graphiques et leurs points:
    plt.plot(df["Time"]*1e6, df["Voltage"], "k")
    plt.xlabel(r"Temps ($\rm \mu$s)")
    plt.ylabel(r"Voltage (V)")
    plt.xlim(-1, 10)
    plt.show()
