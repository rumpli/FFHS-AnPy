import matplotlib.pyplot as plt
import numpy as np

# X Punkte aufsetzen von 0-10, mit 1000 Zwischenschritten
xpoints = np.linspace(0, 10, num=1000)
ypoints = np.cos(xpoints)

# Grafik zeichnen
plt.plot(xpoints, ypoints, '-', label='sinus')
plt.legend(loc='best')
plt.show()
