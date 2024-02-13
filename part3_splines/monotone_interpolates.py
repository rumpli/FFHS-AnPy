import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline, PchipInterpolator, Akima1DInterpolator
import numpy as np

# X & Y Punkte aufsetzen mit Ausreisser
xpoints = np.array([1., 2., 3., 4., 4.5, 5., 6., 7., 8])
ypoints = xpoints**2
ypoints[4] += 101

xx = np.linspace(1, 8, 51)

# Grafik zeichnen
plt.plot(xx, CubicSpline(xpoints, ypoints)(xx), '--', label='Cubic spline')
plt.plot(xx, Akima1DInterpolator(xpoints, ypoints)(xx), '-', label='Akima1D')
plt.plot(xx, PchipInterpolator(xpoints, ypoints)(xx), '-', label='pchip')
plt.plot(xpoints, ypoints, 'o', label='points')
plt.legend()
plt.show()
