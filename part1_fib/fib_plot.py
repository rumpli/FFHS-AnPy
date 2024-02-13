#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import time

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
start = time.time()
print(fib(fib_nummer))
end = time.time()
print("Time worked: ", end - start)

plt.xticks(xpoints)
plt.plot(xpoints, ypoints, 'o--r')
plt.title("Fibonacci Zahlenfolge")
plt.xlabel("Zahlenfolge")
plt.ylabel("Wert der Fibonacci Folge")
plt.grid(axis = 'x')
plt.show()
