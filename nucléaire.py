import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

courant = [1, 0.69, 0.42, 0.2, 0.05, 0.014, 0, 0.12, 0.25, 0.52, 0.88]
distance = [5, 8 ,13, 18, 25, 29, 34, 21, 16, 11, 6.5]
incert = [0.02, 0.02, 0.03, 0.02, 0.01, 0.02, 0, 0.01, 0.01, 0.02, 0.02]

def model(x, a, b):
    return a /(x) + b

params, cov = curve_fit(model, distance, courant)
a, b = params

x_fit = np.linspace(min(distance), max(distance), 500)
y_fit = model(x_fit, a, b)


y_pred = model(distance, a, b)
ss_res = np.sum((courant - y_pred)**2)
ss_tot = np.sum((courant - np.mean(y_pred))**2)
R2 = 1 - ss_res/ss_tot


plt.scatter(distance, courant, color="black")
plt.plot(x_fit, y_fit, "k--", label = f"$y = a/x + b$ (a ={a:.2f}, b = {b:.2f}, $R^2$ = {R2:.2f})")
plt.xlabel("Distance [mm]")
plt.ylabel("Courant mesuré [nA]")
plt.errorbar(distance, courant, yerr=incert, fmt = "o", capsize=5, color="black", label="Données expérimentales")
plt.legend()
plt.show()