import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
import numpy as np
from scipy.optimize import curve_fit


def gaussian(x, a, mu, sigma):
    return a * np.exp(-(x - mu)**2 / (2 * sigma**2))

folder_path = r"SpectreFreq/Rien"
ref_file = os.path.join(folder_path, "Ref.txt")

df_ref = pd.read_csv(ref_file, sep=r"\s+", skiprows=5, names=["Frequency", "Value"], engine="python")
df_ref["Frequency"] = df_ref["Frequency"].str.replace(",", ".").astype(float)
df_ref["Value"] = df_ref["Value"].str.replace(",", ".").astype(float)

all_files = glob.glob(os.path.join(folder_path, "*.txt"))
data_files = [f for f in all_files if not f.endswith("Ref.txt")]

plt.figure(figsize=(10, 6))

for file_path in data_files:
    df = pd.read_csv(file_path, sep=r"\s+", skiprows=5, names=["Frequency", "Value"], engine="python")
    df["Frequency"] = df["Frequency"].str.replace(",", ".").astype(float)
    df["Value"] = df["Value"].str.replace(",", ".").astype(float)
    delta = df["Value"] - df_ref["Value"]
    label = os.path.basename(file_path)
    plt.plot(df["Frequency"], delta, linewidth=1, label=label)

plt.xscale("log")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Intensity (dB)")
plt.ylim(0, 120)
plt.xlim(0, 20000)
plt.legend()
plt.tight_layout()
plt.show()
