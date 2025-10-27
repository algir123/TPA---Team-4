import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


n_lambda = np.array([
25.6, 26.6, 27.6, 28.5, 29.5, 30.5, 31.5, 32.5, 33.4, 34.4,
35.4, 36.4, 37.4, 38.4, 39.3, 40.3, 41.3, 42.3, 43.3, 44.3,
45.2, 46.2, 47.2, 48.2, 49.2, 50.1, 51.1, 52.1, 53.1, 54.1,
55.0, 56.0, 57.0, 58.0, 59.0, 59.9, 60.9, 61.9, 62.9, 63.8
])

R0 = np.array([0.33,0.67,0.70,0.30,0.53,0.60,0.53,0.47,0.60,0.53,
               0.57,0.60,1.47,7.73,30.67,50.60,64.93,71.60,83.23,93.30,
               96.07,98.03,102.47,102.00,106.83,105.27,105.13,103.10,104.80,102.67,
               101.13,98.70,96.03,92.33,89.57,44.47,54.57,47.43,74.43,38.33])

R1 = np.array([0.53,0.43,0.23,0.37,0.40,0.63,0.47,0.27,0.73,0.73,
               0.43,0.80,0.63,1.23,5.33,22.47,39.63,55.20,64.00,73.57,
               77.27,84.07,91.03,91.03,90.30,97.53,93.57,94.30,95.50,94.27,
               93.07,88.23,90.23,86.60,85.33,37.40,39.97,27.90,39.17,26.40])

R2 = np.array([0.50,0.40,0.37,0.20,0.47,0.47,0.47,0.40,0.40,0.57,
               0.63,0.67,0.57,0.53,0.43,0.80,2.13,10.83,27.43,39.43,
               48.40,57.17,64.17,67.83,69.80,73.10,75.07,78.57,75.80,79.77,
               77.27,75.07,76.30,71.67,71.50,19.40,21.83,7.27,10.70,12.50])

R3 = np.array([np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.37,0.37,0.43,0.27,
               0.43,0.33,0.20,0.37,0.37,0.50,0.33,0.67,0.80,2.70,
               10.07,21.90,31.40,38.67,45.57,50.53,58.47,57.90,56.47,58.63,
               62.37,60.50,61.37,59.30,58.43,0.83,3.17,np.nan,np.nan,np.nan])

R4 = np.array([np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,np.nan,np.nan,np.nan,
               np.nan,np.nan,np.nan,np.nan,0.27,0.23,0.60,0.33,0.37,0.40,
               0.50,0.47,1.03,6.43,17.27,24.33,31.60,34.70,41.60,42.17,
               46.40,47.43,46.80,48.17,47.53,np.nan,np.nan,np.nan,np.nan,np.nan])

R5 = np.array([np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,np.nan,np.nan,np.nan,
               np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,
               np.nan,np.nan,np.nan,0.40,0.40,0.83,1.87,7.73,16.60,20.63,
               25.37,27.90,31.87,32.87,35.03,np.nan,np.nan,np.nan,np.nan,np.nan])

labels = ["V = 22 kV", "V = 24 kV", "V = 26 kV", "V = 28 kV", "V = 30 kV", "V = 32 kV", "V = 34 kV", "V = 35 kV"]


def fit_pente(x, y, fraction = 0.03):

    mask = ~np.isnan(y)
    x, y = x[mask], y[mask]
    if len(x) < 5:
        return np.nan, np.nan, np.nan, (x, y)

    # Dérivée locale
    dy = np.gradient(y, x)
    idx_max = np.argmax(dy)

    # Taille de la fenêtre en points (entier)
    n = len(x)
    window = int(fraction * n)
    if window < 2:
        window = 2

    i1, i2 = max(0, idx_max - window), min(n, idx_max + window)

    # Régression linéaire sur la zone abrupte
    slope, intercept, r, p, err = linregress(x[i1:i2], y[i1:i2])
    x_zero = -intercept / slope if slope != 0 else np.nan

    return slope, intercept, r, x_zero, err, (x[i1:i2], y[i1:i2])


R = [R0, R1, R2, R3, R4, R5]
lambdas = []
voltage = [22, 24,26, 28, 30, 32]

for i, Ri in enumerate(R):
    slope, intercept, r, x_zero, err, (xf, yf) = fit_pente(n_lambda, Ri)
    print(err)
    label_fit = f"R{i} (pente={slope:.2f}, x_zero = {x_zero}, R²={r**2:.3f})"
    lambdas.append(x_zero)

    plt.plot(n_lambda, Ri, 'o-', label=label_fit)
    plt.plot(xf, intercept + slope*xf, '--')
    plt.legend()









fig, ax = plt.subplots()

ax.plot(n_lambda, R0, label = labels[0])
ax.plot(n_lambda, R1, label = labels[1])
ax.plot(n_lambda, R2, label = labels[2])
ax.plot(n_lambda, R3, label = labels[3])
ax.plot(n_lambda, R4, label = labels[4])
ax.plot(n_lambda, R5, label= labels[5])

ax.set_xlim(30,58)
ax.set_xlabel(r"$\frac{n\lambda}{pm}$",fontsize=15)
ax.set_ylabel(r"$\frac{R}{1/s}$",fontsize=15)
ax.grid(alpha = 0.3)
plt.legend()

plt.show()

lambdas_2 = [37.97, 39.57, 42.25, 44.59, 47.20, 49.33]
result = linregress(voltage, lambdas_2)

lambdas_fit = result.intercept + result.slope * (np.array(voltage))

residuals = lambdas_2 - lambdas_fit
sigma2 = np.sum(residuals**2) / (len(voltage) - 2)
Sxx = np.sum((np.array(voltage)- np.mean(np.array(voltage)))**2)
cov_ab = -sigma2 * np.mean(np.array(voltage)) / Sxx


print(f"La covariance est de {result.stderr}")



plt.plot(np.array(voltage) / 1000, lambdas_fit, color = "k", linestyle = "--", label = f"Ajust. linéraire, A = {1000 * result.slope:.2f},  R^2 = {result.rvalue ** 2:.3f}.")
plt.scatter(np.array(voltage) / 1000, lambdas_2, color = "k", label = "Données expérimentales")
plt.xlabel("1/V 1/kV")
plt.ylabel(r"$\frac{\lambda_{min}}{pm}$", fontsize=15)
plt.legend()
plt.grid(alpha = 0.3)
plt.show()
