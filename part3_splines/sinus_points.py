import matplotlib.pyplot as plt
import numpy as np

# X Punkte aufsetzen von 0-10, mit 10 Zwischenschritten
x10 = np.linspace(0, 10, num=10)
y10 = np.cos(x10)

# X Punkte aufsetzen von 0-10, mit 20 Zwischenschritten
x20 = np.linspace(0, 10, num=20)
y20 = np.cos(x20)

# X Punkte aufsetzen von 0-10, mit 50 Zwischenschritten
x50 = np.linspace(0, 10, num=50)
y50 = np.cos(x50)

# X Punkte aufsetzen von 0-10, mit 100 Zwischenschritten
x100 = np.linspace(0, 10, num=100)
y100 = np.cos(x100)

# Subplots erstellen (2 auf 2)
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x10, y10, 'o')
axs[0, 0].set_title('Sinus with 10 points')
axs[0, 1].plot(x20, y20, 'om')
axs[0, 1].set_title('Sinus with 20 points')
axs[1, 0].plot(x50, y50, 'og')
axs[1, 0].set_title('Sinus with 50 points')
axs[1, 1].plot(x100, y100, 'oc')
axs[1, 1].set_title('Sinus with 100 points')

# Keine Overlaps
plt.tight_layout()
plt.show()
