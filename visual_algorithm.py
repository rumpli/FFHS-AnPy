#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np


def general_harmonious_series(number, exponent):
    partial_sum_list = []
    current_sum = 0
    for n in range(1, number + 1):
        current_sum += 1 / (n ** exponent)  # Allgemeine harmonische Reihe
        partial_sum_list.append(current_sum)  # Teilglieder der Liste anhängen
    return partial_sum_list


def plot_harmonious_series(exponent_list, term_number):
    for exponent in exponent_list:
        partial_sum = general_harmonious_series(term_number, exponent=exponent)
        plt.plot(range(1, term_number + 1), partial_sum, label='Harmonious series')


# Erstellen der Datenpunkte für die verschiedenen Zeitkomplexitäten
x = np.linspace(1, 37)
y1 = np.ones_like(x)
y2 = x
y3 = x * np.log(x)
y4 = np.log(x)

# Plotten der harmonischen Reihe
exponents = [1]
plot_harmonious_series(exponents, 37)

# Plotten von O(1)
plt.plot(x, y1, label="O(1)")

# Plotten von O(n)
# plt.plot(x, y2, label="O(n)")

# Plotten von O(n log(N))
# plt.plot(x, y3, label="O(n * ln(n))")

# Plotten von 0(log(n))
plt.plot(x, y4, label="O(ln(n))")

# Plotten von 0(log(n) + 1)
plt.plot(x, y4+1, label="O(ln(n) + 1)")

plt.title("Development off different algorithm against the harmonious series")
plt.xlabel("Count of terms")
plt.ylabel("Partial sum")
plt.legend()
plt.grid(True)
plt.show()
