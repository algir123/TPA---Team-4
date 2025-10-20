import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

def f(x, a, b):
    return a * x + b

x = [105,169,310,320,409,460,579,630,756]  # mesure du plastique
y = [72,-42,-263,-275,-419,-495,-678,-752,-968] # mesure du plastique
epaisseur = [0.73, 0.76,0.80,0.835,0.89,0.93,0.955,0.995,1.03]
epaisseurs = [e - 0.73 for e in epaisseur]
mesure_x = [160,187,217,205,188,222,288,306,277,300,304,325,436,441,448,454,509,547,560,382,370,351,290,347]   # mesure de 10 à 250mm
mesure_y = [-66,-108,-155,-137,-111,-161,-262,-246,-280,-289,-323,-491,-497,-553,-542,-623,-679,-690,-428,-400,-371,-278,-271]  # mesure de 10 à 250mm
ref_x = 30
ref_y = 110

plt.plot(ref_x, ref_y, 'ko', label='Référence de la plaque')
plt.plot(160, -66, 'ko', marker='s', label='Première mesure (à 1cm sur la plaque)')
plt.plot(300, -289, 'ko', marker='*', label='Première mesure (à 10cm sur la plaque)')
plt.xlabel("Signal comparé réel moyenné V$\Delta_{R}$")
plt.ylabel("Signal comparé imaginaire moyenné V$\Delta_{L}$")
plt.legend()
plt.xlim(0, 350)
plt.ylim(-400, 200)


popt, pcov = curve_fit(f, x, epaisseurs)
a, b = popt
perr = np.sqrt(np.diag(pcov))

plt.figure(figsize=(10, 6))
plt.plot(x, f(np.array(x), *popt), 'k-', label='fit: a=%5.6f, b=%5.6f' % tuple(popt))
plt.plot(x, epaisseurs, 'ok', label='Données expérimentales')
plt.xlabel(r"Changement de résistance (mV)")
plt.ylabel("Épaisseur de la couche de plastique (mm)")
plt.legend()

plt.figure(figsize=(10, 6))
for i in range(len(mesure_x)):
    plt.plot(i, f(mesure_x[i],a,b), 'ko')


popt, pcov = curve_fit(f, y, epaisseurs)
a, b = popt
perr = np.sqrt(np.diag(pcov))
plt.figure(figsize=(10, 6))
print(perr)
plt.plot(y, f(np.array(y), *popt), 'k-', label='fit: a=%5.6f, b=%5.6f' % tuple(popt))
plt.xlabel(r"Changement de réactance  (mV)")
plt.ylabel("Épaisseur de la couche de plastique (mm)")
plt.plot(y, epaisseurs, 'ok', label='Données expérimentales')
plt.legend()

plt.figure(figsize=(10, 6))
for i in range(len(mesure_y)):
    plt.plot(i, f(mesure_y[i],a,b), 'ko') 
plt.xlabel("Distance sur la plaque métallique (cm)")
plt.ylabel("Hauteur du revêtement (mm)")
plt.legend()   

#Changement d'impédance pour les couches minces de plastique

z = np.sqrt(np.array(x)**2 + np.array(y)**2)
popt, pcov = curve_fit(f, z, epaisseurs)
a, b = popt
perr = np.sqrt(np.diag(pcov))
m_err, b_err = np.sqrt(np.diag(pcov))
y_new_err = np.sqrt((z * m_err)**2 + b_err**2)

plt.close('all')

y_pred = f(np.array(z), *popt)
r2 = r2_score(epaisseurs, y_pred)
plt.figure(figsize=(10, 6))
plt.plot(z, f(np.array(z), *popt), "k-", label="fit: a=%5.6f, b=%5.6f" % tuple(popt))
plt.xlabel(r"Changement de tension (mV)")
plt.ylabel("Épaisseur de la couche de plastique (mm)")
plt.plot(z, epaisseurs, 'ok', label='Données expérimentales')
plt.legend(title=f"R² = {r2:.4f}")


mesure_z = np.sqrt(abs(np.array(mesure_x[:-1]) * np.array(mesure_y)))
print(mesure_x[:-1])
print(mesure_y)
print(mesure_z)


plt.figure(figsize=(10, 6))
for i in range(len(mesure_z)):
    y_new_err = np.sqrt((i * m_err)**2 + b_err**2)
    #plt.plot(i, f(mesure_z[i], a, b), "ko-")
    plt.errorbar(i, f(mesure_z[i], a, b), yerr=y_new_err, fmt='o', color='black', elinewidth=1, capsize=2)
print(mesure_z[11:19])
mean_first_5 = sum(mesure_z[:6]) / 6
mean_next_5 = sum(mesure_z[6:11]) / 5
mean_next = sum(mesure_z[11:19]) / 8
mean_last = sum(mesure_z[19:]) / 4
plt.plot([0,5], [f(mean_first_5, a, b),f(mean_first_5, a, b)], 'k:', label='Moyenne estimée sur chaque section')
plt.plot([6,10], [f(mean_next_5, a, b),f(mean_next_5, a, b)], 'k:')
plt.plot([11,18], [f(mean_next, a, b),f(mean_next, a, b)], 'k:')
plt.plot([19,22], [f(mean_last, a, b),f(mean_last, a, b)], 'k:')
plt.xlabel("Distance sur la plaque métallique (cm)")
plt.ylabel("Hauteur du revêtement (mm)")

plt.show()



'''Épaisseur de la couche de plastique: 
76 * 10^-2 - 73 10^-2 mm +- 0.05 = 3 * 10^-2 mm pm 0.05

2 plastiques: 80 *10^-2 mm

3 plastiques: 83.5 *10^-2

4 plastique: 89 * 10^-2

5plastiques: 93

6 plasituqe: 95.5

7 plastique 99.5 *10^-2

8: 103 *10^-2 mm


À chaque 10mm
'''