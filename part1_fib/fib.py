#!/usr/bin/python3

import time


def fib(fib_nummer):
    a = 0
    b = 1
    for _ in range(fib_nummer):
        a, b = b, a + b
    return a


fib_nummer = int(input("Please input a number: "))
start = time.time()
print(fib(fib_nummer))
end = time.time()
print("Time worked: ", end - start)
