#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

def fib(fib_nummer):
  global ypoints, xpoints
  a = 0
  b = 1
  ypoints = np.array([a])
  xpoints = np.array([a])
  for i in range(fib_nummer):
    a, b = b, a + b
    ypoints = np.append(ypoints, a)
    xpoints = np.append(xpoints, i+1)
  return a

fib_nummer = int(input("Please input a number: "))
print(fib(fib_nummer))


# Erstellen der Werte für f(x) = 1.5^x
x_values = np.linspace(0, fib_nummer, 100)
y_values = 1.5**x_values

# Erstellen der Werte für f(x) = 1.6^x
x_values2 = np.linspace(0, fib_nummer, 100)
y_values2 = 1.6**x_values

plt.plot(x_values, y_values, label='f(x) = 1.5^x')
plt.plot(x_values2, y_values2, label='f(x) = 1.6^x')
plt.xticks(xpoints)
plt.plot(xpoints, ypoints, 'o--r')
plt.title("Fibonacci Zahlenfolge")
plt.xlabel("Zahlenfolge")
plt.ylabel("Wert der Fibonacci Folge")
plt.grid(axis = 'x')
plt.show()
