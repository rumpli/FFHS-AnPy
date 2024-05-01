import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline


def cubic_interpolation(bases):
    # X Punkte festlegen der Sinus Kurve
    xpoints = np.linspace(0, 4 * np.pi, num=100)
    ypoints = np.sin(xpoints)

    # Punkte für die linearen Splines erstellen / Platzierung der Punkte an ausgewählten Orten
    xspline = np.concatenate((np.linspace(1.2, 2, num=3), [4.7], np.linspace(6, 8.5, num=3)))
    yspline = np.sin(xspline)

    cubic_spline = CubicSpline(xspline, yspline)

    # Sinus Kurve zeichnen
    plt.plot(xpoints, ypoints, '--', label='sin(x)')

    # Punkte für die linearen Splines zeichnen
    plt.plot(xspline, yspline, 'o', label='Points')

    # Lineare Approximation zeichnen
    plt.plot(xpoints, cubic_spline(xpoints), '-', label='Points', color='red')

    plt.grid(color='gray', linestyle='--')
    plt.axis([-1.5, 13, -1.5, 1.5])
    plt.legend(loc='best')
    plt.show()


cubic_interpolation(7)
