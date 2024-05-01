import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline


def cubic_interpolation(bases, base_start=0, base_end=4 * np.pi):
    # X Punkte festlegen der Sinus Kurve
    xpoints = np.linspace(0, 4 * np.pi, num=100)
    ypoints = np.sin(xpoints)

    # Punkte für die Kubischen Splines erstellen
    xspline = np.linspace(base_start, base_end, num=bases)
    yspline = np.sin(xspline)

    cubic_spline = CubicSpline(xspline, yspline)

    # Sinus Kurve zeichnen
    plt.plot(xpoints, ypoints, '--', label='sin(x)')

    # Punkte für die linearen Splines zeichnen
    plt.plot(xspline, yspline, 'o', label='Base')

    # Kubische Approximation zeichnen
    plt.plot(xpoints, cubic_spline(xpoints), '-', label='Cubic Spline', color='red')

    plt.grid(color='gray', linestyle='--')
    plt.axis([-1.5, 13 , -1.5, 1.5])
    plt.legend(loc='best')
    plt.show()


cubic_interpolation(7)
cubic_interpolation(20)

cubic_interpolation(5, 0, 5)
cubic_interpolation(10, 1, 8)