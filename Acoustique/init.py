import re
import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.interpolate import UnivariateSpline

base_folder = r"C:\Users\AlexisGiroux\OneDrive - Laserax inc\Documents\GitHub\TPA---Team-4" 
materiau = ["Rien", "Bois", "Carton", "Plexiglass", "Mousse"]
folder_path = r"Carton"
ref_file = os.path.join(folder_path, "Ref.txt")

df_ref = pd.read_csv(ref_file, sep=r"\s+", skiprows=5, names=["Frequency", "Value"], engine="python")
df_ref["Frequency"] = df_ref["Frequency"].str.replace(",", ".").astype(float)
df_ref["Value"] = df_ref["Value"].str.replace(",", ".").astype(float)
x_ref = df_ref["Frequency"]
y_ref = df_ref["Value"]

all_files = glob.glob(os.path.join(folder_path, "*.txt"))
data_files = [f for f in all_files if not f.endswith("Ref.txt")]

plt.figure(figsize=(10, 6))
max_curve_x = []
max_curve_y = []
for i, file_path in enumerate(data_files):
    df = pd.read_csv(file_path, sep=r"\s+", skiprows=5, names=["Frequency", "Value"], engine="python")
    df["Frequency"] = df["Frequency"].str.replace(",", ".").astype(float)
    df["Value"] = df["Value"].str.replace(",", ".").astype(float)
    
    x = df["Frequency"]
    y = df["Value"]

    match = re.search(r'(\d+)', file_path)
    target_frequency = int(match.group(1))
    idx_closest = (np.abs(x - target_frequency)).argmin()
    if target_frequency < 200:
        plt.plot(x, y-y_ref, 'k:', linewidth=1, label=f"Courbe à {target_frequency} Hz")
        plt.plot(x_ref, y_ref, 'k--', color = 'black', linewidth=1, label="Courbe de référence")
        plt.plot(x, y, 'k-', linewidth=1, label=f"100Hz - référence")
    


plt.xscale("log")
plt.xlabel("Frequence (Hz)")
plt.ylabel("Intensité (dB)")
plt.ylim(0, 90)
plt.xlim(10, 20000)
plt.legend()
plt.tight_layout()
plt.show()
