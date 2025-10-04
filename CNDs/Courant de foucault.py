import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

def f(x, a, b):
    return a * x + b

x = [105,169,310,320,409,460,579,630,756]  # mesure du plastique
y = [72,-42,-263,-275,-419,-495,-678,-752,-968] # mesure du plastique
epaisseur = [0.73, 0.76,0.80,0.835,0.89,0.93,0.955,0.995,1.03]
epaisseurs = [e - 0.73 for e in epaisseur]
mesure_x = [160,187,217,205,188,222,288,306,277,300,304,325,436,441,448,454,509,547,560,382,370,351,290,347]   # mesure de 10 à 250mm
mesure_y = [-66,-108,-155,-137,-111,-161,-262,-246,-280,-289,-323,-491,-497,-553,-542,-623,-679,-690,-428,-400,-371,-278,-271]  # mesure de 10 à 250mm


popt, pcov = curve_fit(f, x, epaisseurs)
a, b = popt
perr = np.sqrt(np.diag(pcov))

plt.figure(figsize=(10, 6))
plt.plot(x, f(np.array(x), *popt), 'k-', label='fit: a=%5.3f, b=%5.3f' % tuple(popt))
plt.plot(x, epaisseurs, 'ok', label='Données expérimentales')
plt.xlabel("Changement de résistance (mV)")
plt.ylabel("Épaisseur de la couche de plastique (mm)")

plt.figure(figsize=(10, 6))
for i in range(len(mesure_x)):
    plt.plot(i, f(mesure_x[i],a,b), 'ko')


popt, pcov = curve_fit(f, y, epaisseurs)
a, b = popt
perr = np.sqrt(np.diag(pcov))
plt.figure(figsize=(10, 6))
print(perr)
plt.plot(y, f(np.array(y), *popt), 'k-', label='fit: a=%5.3f, b=%5.3f' % tuple(popt))
plt.plot(y, epaisseurs, 'ok', label='Données expérimentales')
plt.xlabel("Changement de réactance  (mV)")
plt.ylabel("Épaisseur de la couche de plastique (mm)")


plt.figure(figsize=(10, 6))
for i in range(len(mesure_y)):
    plt.plot(i, f(mesure_y[i],a,b), 'ko')
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