import matplotlib.pyplot as plt
import numpy as np
from numpy import polynomial as P
from scipy.interpolate import CubicSpline


def interpolation_with_polynomial(bases, base_start=0, base_end=4 * np.pi):
    # X Punkte festlegen der Sinus Kurve
    xpoints = np.linspace(0, 4 * np.pi, num=100)
    ypoints = np.sin(xpoints)

    # Punkte (Stützstellen) für Splines festlegen
    xspline = np.linspace(base_start, base_end, num=bases)
    yspline = np.sin(xspline)

    # Kubischer Spline
    cubic_spline = CubicSpline(xspline, yspline)

    # Poylnom Grad n-1 (n sind Stützstellen)
    deg = len(xspline) - 1
    f1b = P.Polynomial.fit(xspline, yspline, deg)

    # Sinus Kurve zeichnen
    plt.plot(xpoints, ypoints, '-', label='sin(x)')

    # Punkte für Splines zeichnen
    plt.plot(xspline, yspline, 'o', label='Base')

    # Approximationen zeichnen
    plt.plot(xpoints, f1b(xpoints), '--', label='Cubic Spline', color='green')
    plt.plot(xpoints, cubic_spline(xpoints), '--', label='PolySpline', color='red')

    plt.grid(color='gray', linestyle='--')
    plt.axis([-1.5, 13, -1.5, 1.5])
    plt.legend(loc='best')
    plt.show()


interpolation_with_polynomial(6)
interpolation_with_polynomial(8)
