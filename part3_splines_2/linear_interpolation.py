import matplotlib.pyplot as plt
import numpy as np


def linear_interpolation(bases):
    # X Punkte festlegen der Sinus Kurve
    xpoints = np.linspace(0, 4 * np.pi, num=100)
    ypoints = np.sin(xpoints)

    # Punkte für die linearen Splines erstellen
    xspline = np.linspace(0, 4 * np.pi, num=bases)
    yspline = np.sin(xspline)

    linear_spline = np.interp(xpoints, xspline, yspline)

    # Sinus Kurve zeichnen
    plt.plot(xpoints, ypoints, '-', label='sin(x)')

    # Punkte für die linearen Splines zeichnen
    plt.plot(xspline, yspline, 'o', label='Base')

    # Lineare Approximation zeichnen
    plt.plot(xpoints, linear_spline, '--', label='Linear Spline', color='red')

    plt.grid(color='gray', linestyle='--')
    plt.axis([-1.5, 13 , -1.5, 1.5])
    plt.legend(loc='best')
    plt.show()


linear_interpolation(7)
linear_interpolation(20)
