import numpy as np
import os
import glob
import pandas as pd
import matplotlib.pyplot as plt


plt.figure(figsize=(10, 6))
all_files = glob.glob("*.txt")
print(all_files)
list_figs = ['k--', 'k-', 'k-.', 'k:', 'r-']
for i in range(len(all_files)):
    df_ref = pd.read_csv(all_files[4], sep=r"\s+", skiprows=5, names=["Frequency", "Value"], engine="python")
    max_value = df_ref["Value"].max()
    file_path = all_files[i]
    df = pd.read_csv(file_path, sep=r"\s+", skiprows=5, names=["Frequency", "Value"], engine="python")
    label = os.path.basename(file_path)
    label = os.path.splitext(label)[0]
    if i < 4:
        plt.plot(df["Frequency"], df["Value"]/max_value, list_figs[i], color = 'darkgray', label=label)
    else:
        plt.plot(df["Frequency"], df["Value"]/max_value, 'k-', label=label)
    
plt.xscale("log")
plt.xlabel("Frequence (Hz)")
plt.ylabel("Intensité relative")
plt.ylim(0, 1.1)
plt.xlim(80, 20000)
plt.legend()
plt.tight_layout()



plt.figure(figsize=(10, 6))
for i in range(len(all_files)):
    df_ref = pd.read_csv(all_files[4], sep=r"\s+", skiprows=5, names=["Frequency", "Value"], engine="python")
    file_path = all_files[i]
    df = pd.read_csv(file_path, sep=r"\s+", skiprows=5, names=["Frequency", "Value"], engine="python")
    label = os.path.basename(file_path)
    label = os.path.splitext(label)[0]
    if i < 4:
        plt.plot(df["Frequency"], (df_ref["Value"]-df['Value'])/max_value, list_figs[i], color = 'black', label=label)

        
plt.xscale("log")
plt.xlabel("Frequence (Hz)")
plt.ylabel("Absorption du signal")
plt.ylim(0, 1.1)
plt.xlim(80, 20000)
plt.legend()
plt.tight_layout()
plt.show()