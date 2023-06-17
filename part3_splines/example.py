# 1 ===========================
# Importieren der benötigten Libraries; von matplotlib die Sublibrary pyplot
# mit dem Alias (oder Abkürzung) plt; sowie numpy als np
import matplotlib.pyplot as plt
import numpy as np

# 2 ===========================
# Definierung der X und Y Punkte
xpoints = np.array([0, 50])
ypoints = np.array([10,20])

# 3 ===========================
# Erstellung eines Graphen für die vorher definierten X und Y Punkte
plt.plot(xpoints, ypoints)

# 4 ===========================
# Anzeigen des erstellten Graphen
plt.show()
