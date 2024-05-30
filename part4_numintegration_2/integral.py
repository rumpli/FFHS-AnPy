import numpy as np
import sympy as sy
import scipy.integrate as integrate
import matplotlib.pyplot as plt


# Calculate a function
def calc_function(f, x):
    expr = sy.sympify(f)
    # replace x with variable x
    expr = expr.subs(sy.symbols("x"), x)
    return expr.evalf()


# Calculate the difference between scipy.integrate and the approximation
def calc_integral_diff(f, a, b, result):
    # Calculate integral with scipy
    scipy_integral = integrate.quad(f, a, b)
    difference = (result - scipy_integral[0])
    # Quad gives the error bound - so we need only the first element
    print("SciPy: " + str(scipy_integral[0]))
    print("Differenz: " + str(difference))
    print()
    return difference


# Romberg rule
def romberg(f, a, b, n):
    # Create an interval from a to b in n steps
    intervals = np.linspace(a, b, n + 1)
    y = np.array([calc_function(f, x) for x in intervals])
    result = integrate.romb(y, dx=(b - a) / n)

    print("Romberg Regel: " + str(result))
    return result


# Sehnentrapez function
def sekanten_trapez_regel(f, a, b, n):
    # Create an interval from a to b in n steps
    intervals = np.linspace(a, b, n + 1)
    result = 0
    # For every interval (or strip)
    for strip in range(n):
        a, b = intervals[strip], intervals[strip + 1]
        # Sehnentrapez rule
        result += ((b - a) / 2) * ((calc_function(f, a)) + (calc_function(f, b)))
    print("Sehnentrapez Regel: " + str(result))
    return result


# Tangententrapez function
def tangenten_trapez_regel(f, a, b, n):
    # Create an interval from a to b in n steps
    intervals = np.linspace(a, b, n + 1)
    result = 0
    # For every interval (or strip)
    for strip in range(n):
        a, b = intervals[strip], intervals[strip + 1]
        # Tangententrapez rule
        result += (b - a) * (calc_function(f, ((a + b) / 2)))
    print("Tangententrapez Regel: " + str(result))
    return result


# Simpsons function
def simpson_regel(f, a, b, n):
    # Create an interval from a to b in n steps
    intervals = np.linspace(a, b, n + 1)
    result = 0
    # For every interval (or strip)
    for strip in range(n):
        a, b = intervals[strip], intervals[strip + 1]
        # Simpsonsche rule
        result += ((b - a) / 6) * ((calc_function(f, a)) + (4 * calc_function(f, (a + b) / 2)) + (calc_function(f, b)))
    print("Simpson Regel: " + str(result))
    return result


# create plot
def create_plot(sekanten, tangenten, simpson, romberg=None):
    # Strips for plot
    strips = np.array([1, 10, 100])
    plt.figure(figsize=(10, 6))
    plt.loglog(strips, sekanten, marker='o', label='Sehnentrapez')
    plt.loglog(strips, tangenten, marker='s', label='Tangenztrapez')
    plt.loglog(strips, simpson, marker='^', label='Simpsonsche Formel')
    if romberg is not None:
        strips = np.array([1, 16, 128])
        plt.loglog(strips, romberg, marker='x', label='Rombergsche Formel')
    plt.xlabel('Anzahl der Streifen')
    plt.ylabel('Fehlerdifferenz zu SciPy Integral')
    plt.title('Fehlerplot der Integrationsmethoden')
    plt.grid(True, which="both", ls="--")
    # Show plot
    plt.legend()
    plt.show()


# Integral 1
print("Integral 1")

# Sehnkanten Trapez
s1 = calc_integral_diff(lambda x: np.pi * 1 / x, 1, 2, sekanten_trapez_regel(str(np.pi) + "*1/x", 1, 2, 1))
s10 = calc_integral_diff(lambda x: np.pi * 1 / x, 1, 2, sekanten_trapez_regel(str(np.pi) + "*1/x", 1, 2, 10))
s100 = calc_integral_diff(lambda x: np.pi * 1 / x, 1, 2, sekanten_trapez_regel(str(np.pi) + "*1/x", 1, 2, 100))

# Tangenz
t1 = calc_integral_diff(lambda x: np.pi * 1 / x, 1, 2, tangenten_trapez_regel(str(np.pi) + "*1/x", 1, 2, 1))
t10 = calc_integral_diff(lambda x: np.pi * 1 / x, 1, 2, tangenten_trapez_regel(str(np.pi) + "*1/x", 1, 2, 10))
t100 = calc_integral_diff(lambda x: np.pi * 1 / x, 1, 2, tangenten_trapez_regel(str(np.pi) + "*1/x", 1, 2, 100))

# Simpsons
si1 = calc_integral_diff(lambda x: np.pi * 1 / x, 1, 2, simpson_regel(str(np.pi) + "*1/x", 1, 2, 1))
si10 = calc_integral_diff(lambda x: np.pi * 1 / x, 1, 2, simpson_regel(str(np.pi) + "*1/x", 1, 2, 10))
si100 = calc_integral_diff(lambda x: np.pi * 1 / x, 1, 2, simpson_regel(str(np.pi) + "*1/x", 1, 2, 100))

# Romberg
romberg1 = calc_integral_diff(lambda x: np.pi * 1 / x, 1, 2, romberg(str(np.pi) + "*1/x", 1, 2, 1))
romberg16 = calc_integral_diff(lambda x: np.pi * 1 / x, 1, 2, romberg(str(np.pi) + "*1/x", 1, 2, 16))
romberg128 = calc_integral_diff(lambda x: np.pi * 1 / x, 1, 2, romberg(str(np.pi) + "*1/x", 1, 2, 128))

# Create plot
create_plot(np.abs([s1, s10, s100]), np.abs([t1, t10, t100]), np.abs([si1, si10, si100]))
create_plot(np.abs([s1, s10, s100]), np.abs([t1, t10, t100]), np.abs([si1, si10, si100]), np.abs([romberg1, romberg16, romberg128]))

# Integral 2
print("Integral 2")

# Sehnkanten Trapez
s1 = calc_integral_diff(lambda x: x ** 3 + 3 * x ** 2, 0, 1, sekanten_trapez_regel("x**3+3*x**2", 0, 1, 1))
s10 = calc_integral_diff(lambda x: x ** 3 + 3 * x ** 2, 0, 1, sekanten_trapez_regel("x**3+3*x**2", 0, 1, 10))
s100 = calc_integral_diff(lambda x: x ** 3 + 3 * x ** 2, 0, 1, sekanten_trapez_regel("x**3+3*x**2", 0, 1, 100))

# Tangenz
t1 = calc_integral_diff(lambda x: x ** 3 + 3 * x ** 2, 0, 1, tangenten_trapez_regel("x**3+3*x**2", 0, 1, 1))
t10 = calc_integral_diff(lambda x: x ** 3 + 3 * x ** 2, 0, 1, tangenten_trapez_regel("x**3+3*x**2", 0, 1, 10))
t100 = calc_integral_diff(lambda x: x ** 3 + 3 * x ** 2, 0, 1, tangenten_trapez_regel("x**3+3*x**2", 0, 1, 100))

# Simpsons
si1 = calc_integral_diff(lambda x: x ** 3 + 3 * x ** 2, 0, 1, simpson_regel("x**3+3*x**2", 0, 1, 1))
si10 = calc_integral_diff(lambda x: x ** 3 + 3 * x ** 2, 0, 1, simpson_regel("x**3+3*x**2", 0, 1, 10))
si100 = calc_integral_diff(lambda x: x ** 3 + 3 * x ** 2, 0, 1, simpson_regel("x**3+3*x**2", 0, 1, 100))

# Romberg
romberg1 = calc_integral_diff(lambda x: np.pi * 1 / x, 1, 2, romberg("x**3+3*x**2", 1, 2, 1))
romberg16 = calc_integral_diff(lambda x: np.pi * 1 / x, 1, 2, romberg("x**3+3*x**2", 1, 2, 16))
romberg128 = calc_integral_diff(lambda x: np.pi * 1 / x, 1, 2, romberg("x**3+3*x**2", 1, 2, 128))

# Create plot
create_plot(np.abs([s1, s10, s100]), np.abs([t1, t10, t100]), np.abs([si1, si10, si100]))
create_plot(np.abs([s1, s10, s100]), np.abs([t1, t10, t100]), np.abs([si1, si10, si100]), np.abs([romberg1, romberg16, romberg128]))

# Integral 3
print("Integral 3")

# Sehnkanten Trapez
s1 = calc_integral_diff(lambda x: np.cos(x), -np.pi / 2, np.pi / 2,
                        sekanten_trapez_regel("cos(x)", -np.pi / 2, np.pi / 2, 1))
s10 = calc_integral_diff(lambda x: np.cos(x), -np.pi / 2, np.pi / 2,
                         sekanten_trapez_regel("cos(x)", -np.pi / 2, np.pi / 2, 10))
s100 = calc_integral_diff(lambda x: np.cos(x), -np.pi / 2, np.pi / 2,
                          sekanten_trapez_regel("cos(x)", -np.pi / 2, np.pi / 2, 100))

# Tangenz
t1 = calc_integral_diff(lambda x: np.cos(x), -np.pi / 2, np.pi / 2,
                        tangenten_trapez_regel("cos(x)", -np.pi / 2, np.pi / 2, 1))
t10 = calc_integral_diff(lambda x: np.cos(x), -np.pi / 2, np.pi / 2,
                         tangenten_trapez_regel("cos(x)", -np.pi / 2, np.pi / 2, 10))
t100 = calc_integral_diff(lambda x: np.cos(x), -np.pi / 2, np.pi / 2,
                          tangenten_trapez_regel("cos(x)", -np.pi / 2, np.pi / 2, 100))

# Simpsons
si1 = calc_integral_diff(lambda x: np.cos(x), -np.pi / 2, np.pi / 2, simpson_regel("cos(x)", -np.pi / 2, np.pi / 2, 1))
si10 = calc_integral_diff(lambda x: np.cos(x), -np.pi / 2, np.pi / 2,
                          simpson_regel("cos(x)", -np.pi / 2, np.pi / 2, 10))
si100 = calc_integral_diff(lambda x: np.cos(x), -np.pi / 2, np.pi / 2,
                           simpson_regel("cos(x)", -np.pi / 2, np.pi / 2, 100))

# Romberg
romberg1 = calc_integral_diff(lambda x: np.cos(x), -np.pi / 2, np.pi / 2, romberg("cos(x)", -np.pi / 2, np.pi / 2, 1))
romberg16 = calc_integral_diff(lambda x: np.cos(x), -np.pi / 2, np.pi / 2,
                          romberg("cos(x)", -np.pi / 2, np.pi / 2, 16))
romberg128 = calc_integral_diff(lambda x: np.cos(x), -np.pi / 2, np.pi / 2,
                           romberg("cos(x)", -np.pi / 2, np.pi / 2, 128))

# Create plot
create_plot(np.abs([s1, s10, s100]), np.abs([t1, t10, t100]), np.abs([si1, si10, si100]))
create_plot(np.abs([s1, s10, s100]), np.abs([t1, t10, t100]), np.abs([si1, si10, si100]), np.abs([romberg1, romberg16, romberg128]))