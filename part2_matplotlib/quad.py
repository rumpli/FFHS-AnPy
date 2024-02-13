import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers (ranging from -5 to 5)
xpoints = np.linspace(-5,5,100)

# each x (or xpoint) to the power of 2
ypoints = xpoints**2

plt.plot(xpoints, ypoints)

# Set labels for title and the axis
plt.title("Quadratische Funktion F(x) = x^2")
plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")

# show the x-axis grid
plt.grid(axis='x')

# limit the x- and y-axis
plt.xlim(-5,5)
plt.ylim(0,25)

plt.show()
