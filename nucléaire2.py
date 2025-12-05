import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

angles = [-25, -15, -10, -4, 0, 5, 10, 15, 25]
comptes = [6, 191, 639, 1054, 982, 630, 197, 30, 8]
comptes = np.array(comptes)/240

def model(x, a, mu, sigma, c):
    return a * np.exp(-(x - mu) ** 2 / (2 * sigma**2)) + c

x = np.linspace(min(angles), max(angles), 200)


#Fit
popt, pcov = curve_fit(model, angles, comptes)
a_fit, mu_fit, sigma_fit, c_fit = popt

y_fit = model(x, a_fit, mu_fit, sigma_fit, c_fit)

y_pred = model(angles, a_fit, mu_fit, sigma_fit, c_fit)
ss_res = np.sum((comptes - y_pred) ** 2)
ss_tot = np.sum((comptes - np.mean(y_pred)) ** 2)
R2 = 1 - ss_res/ss_tot

print("a =", a_fit)
print("mu =", mu_fit)
print("sigma =", sigma_fit)
print("c =", c_fit)

peak = y_fit.max()
idx = np.where(y_fit == peak)
print(x[idx])



#Affichage
plt.scatter(angles, comptes, color="black")
plt.plot(x,  y_fit, "k--", label = f"Régression gaussienne" + "\n" + f"$\mu = $ {mu_fit:.2f}, $\sigma =$ {sigma_fit:.2f}" + "\n" + f"$R^2 = {R2:.3f}$")
plt.errorbar(angles, comptes, yerr = np.sqrt(np.array(comptes)), fmt = "o", capsize=5, color="black",label = "Données expérimentales")
plt.xlabel(r"Angle relatif entre les deux détecteurs[$^\circ$]", fontsize = 14)
plt.ylabel(r"Taux de coïncidences détectées [s$^{-1}$]", fontsize = 14)
plt.legend()
plt.show()