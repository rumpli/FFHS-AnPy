import matplotlib.pyplot as plt
import numpy as np

# F(x) = x
xpoints = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6])
ypoints = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6])
plt.plot(xpoints, ypoints, color="blue")

# F(x) = x*2
xpoints = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6])
ypoints = np.array([-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12])
plt.plot(xpoints, ypoints, color="red")

# F(x) = x^2 - 10
xpoints = np.linspace(-5,5,100)
ypoints = xpoints**2 - 10
plt.plot(xpoints, ypoints, color="lightblue")

# F(x) = 5 * x^2 + 5
xpoints = np.linspace(-5,5,100)
ypoints = 5*xpoints**2 + 5
plt.plot(xpoints, ypoints, color="green")

# F(-x) = 5 * -x^2 + 2
xpoints = np.linspace(-5,5,100)
ypoints = 5*-xpoints**2 + 2
plt.plot(xpoints, ypoints, color="orange")

# show the x-axis grid
plt.grid(axis='x')

# limit the x- and y-axis
plt.xlim(-5,5)
plt.ylim(-10,25)

# Set labels for title and the axis
plt.title("Funktionen")

plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")

plt.show()
