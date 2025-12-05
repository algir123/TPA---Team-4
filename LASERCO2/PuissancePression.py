import numpy as np
import matplotlib.pyplot as plt

pression = [10, 15, 20, 25, 26, 27,27.5, 28, 29, 30, 35, 40 ,45, 50]
p35 = [0.8, 1.8, 2.5, 2.9 ,2.9, 2.95, 3, 2.95, 2.9, 2.9, 2.65, 1.95, 0.9, 0.1]
p30 = [0.55, 1.6, 2.54, 2.7, 2.75, 2.75,2.9, 2.8, 2.75, 2.75, 2.6, 2.1, 1.3, 0.1]

p35 = list(map(lambda x: x * 3, p35))
p30 = list(map(lambda x: x * 3, p30))

fig, ax = plt.subplots(2,1)
ax[0].scatter(pression, p30, label = "I = 30 mA")
ax[1].scatter(pression, p35, label = "I = 35 mA")
ax[0].grid(alpha = 0.3)
ax[1].grid(alpha = 0.3)
fig.supylabel('Puissance émise [W]')
fig.supxlabel("Pression [mbar]")
ax[0].legend()
ax[1].legend()
plt.show()