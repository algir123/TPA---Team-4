import numpy as np
import os
import glob
import pandas as pd
import matplotlib.pyplot as plt


plt.figure(figsize=(10, 6))
all_files = glob.glob("*.txt")
list_figs = ['k--', 'k-', 'k-.', 'k:', 'r-']
for i in range(len(all_files)):
    file_path = all_files[i]
    df = pd.read_csv(file_path, sep=r"\s+", skiprows=5, names=["Frequency", "Value"], engine="python")
    label = os.path.basename(file_path)
    label = os.path.splitext(label)[0]
    if i < 4:
        plt.plot(df["Frequency"], df["Value"], list_figs[i], color = 'darkgray', label=label)
    else:
        plt.plot(df["Frequency"], df["Value"], 'k-', label=label)
    
plt.xscale("log")
plt.xlabel("Frequence (Hz)")
plt.ylabel("Intensité (dB)")
plt.ylim(0, 90)
plt.xlim(80, 20000)
plt.legend()
plt.tight_layout()
plt.show()