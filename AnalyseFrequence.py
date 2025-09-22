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
folder_path = r"Rien"
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
    y = df["Value"] - y_ref

    match = re.search(r'(\d+)', file_path)
    target_frequency = int(match.group(1))
    idx_closest = (np.abs(x - target_frequency)).argmin()
    
    window = 12
    if target_frequency <= 200:
        window = 3
    if target_frequency > 200 and target_frequency <= 1000:
        window = 5
    start_idx = max(idx_closest - window, 0)
    end_idx = min(idx_closest + window + 1, len(x))
    
    x_region = x.iloc[start_idx:end_idx].fillna(0)
    y_region = y.iloc[start_idx:end_idx].fillna(0)
    
    f_interp = interp1d(x_region, y_region, kind="cubic", fill_value="extrapolate")
    x_new = np.linspace(x_region.min(), x_region.max(), 5000)
    y_new = f_interp(x_new)
    
    max_y = np.max(y_new)
    x_at_max = x_new[np.argmax(y_new)]
    max_curve_x.append(x_at_max)
    max_curve_y.append(max_y)
    
    if i == len(data_files) - 1:
        plt.plot(x_new, y_new, color='darkgray', linewidth=1, label="Courbes des fréquences du système")
        plt.plot(x_at_max, max_y, 'o', markerfacecolor='none', markeredgecolor='black', label="Pics max", markersize=6)
        plt.legend()
    else:
        plt.plot(x_new, y_new, color='darkgray', linewidth=1)
        plt.plot(x_at_max, max_y, 'o', markerfacecolor='none', markeredgecolor='black', markersize=6)
        
x = np.array(max_curve_x)
y = np.array(max_curve_y)

sorted_idx = np.argsort(x)
x = x[sorted_idx]
y = y[sorted_idx]

x_log = np.logspace(np.log10(x.min()), np.log10(x.max()), 1000)

spline = UnivariateSpline(np.log10(x), y, s=100)
y_smooth = spline(np.log10(x_log))

plt.plot(x_log, y_smooth, 'k-', linewidth=2, label="Courbe de réponse du système")
plt.xscale("log")
plt.xlabel("Frequence (Hz)")
plt.ylabel("Intensité (dB)")
plt.ylim(0, 90)
plt.xlim(10, 20000)
plt.legend()
plt.tight_layout()
plt.show()
