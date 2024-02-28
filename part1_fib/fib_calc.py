#!/usr/bin/python3

def fib_calc(fib_nummer):
    if fib_nummer == 0:
        return 1
    elif fib_nummer == 1:
        return 1
    else:
        return fib_calc(fib_nummer - 1) + fib_calc(fib_nummer - 2) + 1


fib_nummer = int(input("Please input a number: "))
print("It will take " + str(fib_calc(fib_nummer)) + " calls to calculate the " + str(fib_nummer) + "th fibonacci number")
