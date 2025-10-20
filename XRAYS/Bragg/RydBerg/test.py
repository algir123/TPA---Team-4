import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def linear_func(x, m, b):
    return m * x + b

# Données expérimentales
lamb = np.array([45.2, 50.1, 63.8, 70.7])
lamb = 1 / lamb
z = np.array([49, 47, 42, 40])

# Ajustement
popt, pcov = curve_fit(linear_func, z, np.sqrt(lamb))
m, b = popt
sigma_m, sigma_b = np.sqrt(np.diag(pcov))

# Constantes physiques
R = m**2*10**12
sigma_R = 2 * m * sigma_m*10**12

sigma = -b / m
sigma_sigma = np.sqrt((sigma_b / m)**2 + ((b * sigma_m) / (m**2))**2)

# Affichage
print(f"m = {m:.6f} ± {sigma_m:.6f}")
print(f"b = {b:.6f} ± {sigma_b:.6f}")
print(f"R = {R:.6e} ± {sigma_R:.6e}")
print(f"σ = {sigma:.3f} ± {sigma_sigma:.3f}")

# Tracé
x = np.linspace(0, 50, 200)
plt.figure(figsize=(7, 5))
plt.plot(z, np.sqrt(lamb), 'o', color = 'black')
plt.plot(x, linear_func(x, *popt), '--', color = 'gray',
         label=(f"Fit: y = {m:.4f}x + {b:.4f}\n"
                f"$R^2$ = {1 - np.sum((np.sqrt(lamb) - linear_func(z, *popt))**2) / np.sum((np.sqrt(lamb)-np.mean(np.sqrt(lamb)))**2):.3f}"))
plt.xlabel("Atomic number Z")
plt.ylabel(r"$\sqrt{\frac{pm}{\lambda}}$")
plt.legend()
plt.grid(alpha=0.3)
plt.show()