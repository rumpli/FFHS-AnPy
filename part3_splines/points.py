import matplotlib.pyplot as plt
import numpy as np

# X Punkte aufsetzen von 0-10, mit 1000 Zwischenschritten
xpoints = np.linspace(-1, 1, num=1000)
ypoints = xpoints**2 + 1

# Grafik zeichnen
plt.plot(xpoints, ypoints, '-', label='f(x)=x**2+1')

# X Punkte aufsetzen von 0-10, mit 2 Zwischenschritten
xpoints = np.linspace(-1, 1, num=2)
ypoints = xpoints**2 + 1

# Grafik zeichnen
plt.plot(xpoints, ypoints, 'o--', label='2 Punkte')

# X Punkte aufsetzen von 0-10, mit 3 Zwischenschritten
xpoints = np.linspace(-1, 1, num=3)
ypoints = xpoints**2 + 1

# Grafik zeichnen
plt.plot(xpoints, ypoints, 'o--', label='3 Punkte')

# X Punkte aufsetzen von 0-10, mit 4 Zwischenschritten
xpoints = np.linspace(-1, 1, num=4)
ypoints = xpoints**2 + 1

# Grafik zeichnen
plt.plot(xpoints, ypoints, 'o--', label='4 Punkte')

# X Punkte aufsetzen von 0-10, mit 5 Zwischenschritten
xpoints = np.linspace(-1, 1, num=5)
ypoints = xpoints**2 + 1

# Grafik zeichnen
plt.plot(xpoints, ypoints, 'o--', label='5 Punkte')
plt.legend(loc='best')
plt.show()
