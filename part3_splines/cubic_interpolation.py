import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import numpy as np

# X Punkte aufsetzen von 0-10, mit 11 Zwischenschritten
xpoints = np.linspace(0, 10, num=11)
ypoints = np.cos(xpoints)
# Grafik zeichnen
plt.plot(xpoints, ypoints, 'o', label='data')

# Cubic Spline
spl = CubicSpline(xpoints, ypoints)

# Neue X und Y Werte
xnew = np.linspace(0, 10, num=20)
ynew = np.interp(xnew, xpoints, ypoints)
# Grafik zeichnen
plt.plot(xnew, spl(xnew), '-', label='cubic interp')

# Neue X und Y Werte (mehr Zwischenschritte)
xbetter = np.linspace(0, 10, num=50)
ybetter = np.interp(xbetter, xpoints, ypoints)

# Grafik zeichnen
plt.plot(xbetter, spl(xbetter), '-', label='cubic interp better')
plt.plot(xnew, ynew, '--', label='linear interp')
plt.legend(loc='best')
plt.show()
