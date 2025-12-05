import matplotlib.pyplot as plt
import numpy as np

courant = [5, 10, 15, 20, 25, 30, 35]

ratio_100 = [0.6, 1.2, 1.85, 2.2, 2.55, 2.8, 2.95]
ratio_75 = [0.5, 1, 1.35, 1.7, 1.95, 2.1, 2.25]
ratio_50 = [0.4, 0.8, 1.05, 1.3, 1.45, 1.5, 1.5]
ratio_25 = [0.3, 0.55, 0.7, 0.8, 0.85, 0.8, 0.75]

ratio_100 = list(map(lambda x: x * 3, ratio_100))
ratio_75 = list(map(lambda x: x * 3, ratio_75))
ratio_50 = list(map(lambda x: x * 3, ratio_50))
ratio_25 = list(map(lambda x: x * 3, ratio_25))

fig, ax = plt.subplots()
ax.scatter(courant, ratio_100, label="P = 27.5 mbar")
ax.scatter(courant, ratio_75, label="P = 18 mbar")
ax.scatter(courant, ratio_50, label = "P = 13 mbar")
ax.scatter(courant, ratio_25, label = "P = 11 mbar")
ax.set_xlabel("Courant [mA]")
ax.set_ylabel("Puissance émise [W]")
ax.grid(alpha=0.3)
plt.legend()
plt.show()

d_100 = [9.25, 8.78, 7.9, 7.53, 7.22, 6.98, 6.78]

d_75 = [6.83, 6.26, 5.99, 5.78, 5.6, 5.47, 5.34]

d_50 = [5.64, 5.37, 5.18, 5.04, 4.92, 4.82, 4.73]

d_25 = [4.83, 4.66, 4.53, 4.43, 4.34, 4.26, 4.19]

fig, ax = plt.subplots()

ax.scatter(courant, d_100,label="P = 27.5 mbar")
ax.scatter(courant, d_75, label="P = 18 mbar")
ax.scatter(courant, d_50, label="P = 13 mbar")
ax.scatter(courant, d_25, label="P = 11 mbar")
ax.set_xlabel("Courant [mA]")
ax.set_ylabel("Tension de décharge [kV]")
ax.grid(alpha=0.3)
plt.legend()
plt.show()