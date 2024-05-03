import matplotlib.pyplot as plt
import numpy as np
from numpy import polynomial as P
from scipy.interpolate import CubicSpline


def interpolation():
    # X & Y Punkte aufsetzen mit Ausreisser
    xpoints = np.array([1., 2., 3., 4., 4.5, 5., 6., 7., 8])
    ypoints = xpoints ** 2
    ypoints[4] += 101

    xx = np.linspace(1, 8, 51)

    # Kubischer Spline
    cubic_spline = CubicSpline(xpoints, ypoints)

    # Poylnom Grad n-1 (n sind Stützstellen)
    deg = len(xpoints) - 1
    f1b = P.Polynomial.fit(xpoints, ypoints, deg)

    # Sinus Kurve zeichnen
    plt.plot(xpoints, ypoints, '-', label='f(x)')

    # Punkte für Splines zeichnen
    plt.plot(xpoints, ypoints, 'o', label='Base')

    # Approximationen zeichnen
    plt.plot(xx, f1b(xx), '--', label='Polynomial Spline', color='green')
    plt.plot(xx, cubic_spline(xx), '--', label='Cubic Spline', color='red')

    plt.grid(color='gray', linestyle='--')
    plt.legend(loc='best')
    plt.show()


interpolation()
