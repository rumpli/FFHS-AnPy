#!/usr/bin/python3

import time

count = 0


def fib(fib_nummer):
    global count
    count += 1
    if fib_nummer > 1:
        return fib(fib_nummer - 1) + fib(fib_nummer - 2)
    else:
        if fib_nummer == 0:
            return 0
        else:
            return 1


fib_nummer = int(input("Please input a number: "))
start = time.time()
print(fib(fib_nummer))
end = time.time()
print("Time worked: ", end - start)
print("fib() was called: ", count, " times")
