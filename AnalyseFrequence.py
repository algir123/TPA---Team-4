import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
import numpy as np
from scipy.optimize import curve_fit
import re



def gaussian(x, a, mu, sigma):
    return a * np.exp(-(x - mu)**2 / (2 * sigma**2))


folder_path = r"Plexiglass"
ref_file = os.path.join(folder_path, "Ref.txt")

df_ref = pd.read_csv(ref_file, sep=r"\s+", skiprows=5, names=["Frequency", "Value"], engine="python")
df_ref["Frequency"] = df_ref["Frequency"].str.replace(",", ".").astype(float)
df_ref["Value"] = df_ref["Value"].str.replace(",", ".").astype(float)
x_ref = df_ref["Frequency"]
y_ref = df_ref["Value"]

all_files = glob.glob(os.path.join(folder_path, "*.txt"))
data_files = [f for f in all_files if not f.endswith("Ref.txt")]

plt.figure(figsize=(10, 6))

for file_path in data_files:
    df = pd.read_csv(file_path, sep=r"\s+", skiprows=5, names=["Frequency", "Value"], engine="python")
    df["Frequency"] = df["Frequency"].str.replace(",", ".").astype(float)
    df["Value"] = df["Value"].str.replace(",", ".").astype(float)
    delta = df["Value"] - df_ref["Value"]
    label = os.path.basename(file_path)
    x = df["Frequency"]
    y = df["Value"] - y_ref
    match = re.search(r'(\d+)', file_path)
    target_frequency = int(match.group(1))
    print(target_frequency)
    idx_closest = (np.abs(x - target_frequency)).argmin()
    window = 10
    if target_frequency <= 200:
        window = 3
    start_idx = max(idx_closest - window, 0)
    end_idx = min(idx_closest + window + 1, len(x))
    x_region = x.iloc[start_idx:end_idx]
    y_region = y.iloc[start_idx:end_idx]
    x_region = x_region.fillna(0)
    y_region = y_region.fillna(0)
    print(x_region)
    print(y_region)
    #initial_guess = [np.max(y_region), target_frequency, 20]
    #popt, _ = curve_fit(gaussian, x_region, y_region, p0=initial_guess)
    #x_fit = np.linspace(x_region.min(), x_region.max(), 100)
    #plt.plot(x_fit, gaussian(x_fit, *popt), 'r--', label="Gaussian Fit")
    plt.plot(x_region, y_region, linewidth=1, label=label)

plt.xscale("log")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Intensity (dB)")
plt.ylim(0, 120)
plt.xlim(0, 20000)
plt.legend()
plt.tight_layout()
plt.show()
