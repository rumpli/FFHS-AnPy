import matplotlib.pyplot as plt
import numpy as np

# Set style
plt.style.use('ggplot')

xpoints = np.array(["Zürich", "Bern", "Waadt", "Aargau", "St. Gallen", "Genf"])
ypoints = np.array([81092, 82854, 90816, 80578, 71021, 87923])

# Set all the bars we need
x_position = np.arange(len(xpoints))
plt.bar(x_position, ypoints, color="lightblue")

# Set labels for title and the axis
plt.title("Wie hoch ist das Durchschnittsgehalt\n eines Informatiker in den 6 bevölkerungsstärksten Kantonen?")
plt.xlabel("Kantone")
plt.ylabel("Durchschnittsgehalt")

# Write to each x_position its corresponding xpoint value
plt.xticks(x_position, xpoints)

plt.show()
