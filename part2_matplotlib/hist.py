import matplotlib.pyplot as plt
import numpy as np

# Exam points (max 30 points)
points = np.array([1, 24, 15, 30, 20, 4, 15, 18, 9, 19])

labels = 'Note 1', 'Note 2', 'Note 3', 'Note 4', 'Note 5', 'Note 6'

# bins for each grade
bins = [0, 6, 12, 18, 24, 28, 30]
plt.hist(points, bins, facecolor='r', alpha=0.7, edgecolor='k', linewidth=1)

# Set text
plt.text(3, 2.2, labels[0], ha='center')
plt.text(9, 1.2, labels[1], ha='center')
plt.text(15, 2.2, labels[2], ha='center')
plt.text(21, 3.2, labels[3], ha='center')
plt.text(26, 1.2, labels[4], ha='center')
plt.text(30, 1.2, labels[5], ha='center')

# Set labels for title and the axis
plt.title("Noten")
plt.xlabel("Anzahl erreichte Punkte")
plt.ylabel("Häufigkeit")

plt.show()
