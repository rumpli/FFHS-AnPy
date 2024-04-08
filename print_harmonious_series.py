#!/usr/bin/python3

# Gibt die harmonische Reihe aus
# Weitz, Konkrete Mathematik (nicht nur) fuer Informatiker Mit vielen Grafiken und Algorithmen in Python
def print_harmonious_series(number):
    for n in range(1, number):
        print(n, sum(1 / k for k in range(1, n + 1)))


def print_harmonious_series_big(number):
    for e in range(1, number):
        n = 10 ** e
        print(n, sum(1 / k for k in range(1, n + 1)))


print_harmonious_series(100)
print_harmonious_series_big(10)
