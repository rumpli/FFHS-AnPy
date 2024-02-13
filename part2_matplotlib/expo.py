import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers (ranging from 0 to 5)
xpoints = np.linspace(0,5,100)

# number 3 to the power of each x (or xpoint)
ypoints = 3**xpoints

plt.plot(xpoints, ypoints)

# Set labels for title and the axis
plt.title("Exponentielle Funktion F(x) = a^x")
plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")

# show the x-axis grid
plt.grid(axis='x')

# limit the x- and y-axis
plt.xlim(0,5)
plt.ylim(0,250)

plt.show()
