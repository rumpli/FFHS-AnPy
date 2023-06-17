import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 3, 4, 5, 6])
ypoints = np.array([1, 2, 3, 4, 5, 6])

plt.plot(xpoints, ypoints)

# Set labels for title and the axis
plt.title("Lineare Funktion F(x) = x")
plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")

plt.show()
