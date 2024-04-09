#!/usr/bin/python3

import matplotlib.pyplot as plt


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
        plt.plot(range(1, term_number + 1), partial_sum, label='exp={}'.format(exponent))


exponents = [1, 1.5, 2, 3, 5, 8, 10]
plot_harmonious_series(exponents, 37)
plt.title("General Harmonious Series for different exponents")
plt.xlabel("Count of terms")
plt.ylabel("Partial sum")
plt.legend()
plt.grid(True)
plt.show()

exponents = [3, 5, 8, 10]
plot_harmonious_series(exponents, 10)
plt.title("General Harmonious Series for different exponents")
plt.xlabel("Count of terms")
plt.ylabel("Partial sum")
plt.legend()
plt.grid(True)
plt.show()
