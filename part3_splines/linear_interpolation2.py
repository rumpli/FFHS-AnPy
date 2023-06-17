import matplotlib.pyplot as plt
import numpy as np

# X Punkte aufsetzen von 0-10, mit 11 Zwischenschritten
xpoints = np.linspace(0, 10, num=11)
ypoints = np.cos(xpoints)

# X Punkte aufsetzen von 0-10, mit 1000 Zwischenschritten
xnew = np.linspace(0, 10, num=1000)
ynew = np.interp(xnew, xpoints, ypoints)

# Grafik zeichnen
plt.plot(xnew, ynew, '-', label='linear interp')
plt.plot(xpoints, ypoints, 'o', label='data')
plt.legend(loc='best')
plt.show()
