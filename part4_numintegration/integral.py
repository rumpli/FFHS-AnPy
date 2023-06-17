import numpy as np
import sympy as sy
import scipy.integrate as integrate


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
    # Quad gives the error bound - so we need only the first element
    print("SciPy: " + str(scipy_integral[0]))
    print("Differenz: " + str(result - scipy_integral[0]))
    print()
    return


# summierte Sehnentrapezfunktion
def sekanten_trapez_regel(f, a, b, n):
    # Create an interval from a to b in n steps
    intervals = np.linspace(a, b, n + 1)
    result = 0
    # For every interval (or Strip/Streifen)
    for strip in range(n):
        a, b = intervals[strip], intervals[strip + 1]
        # Sehnentrapezformel
        result += ((b - a) / 2) * ((calc_function(f, a)) + (calc_function(f, b)))
    print("Sehnentrapez Regel: " + str(result))
    return result


# summierte Tangententrapezfunktion
def tangenten_trapez_regel(f, a, b, n):
    # Create an interval from a to b in n steps
    intervals = np.linspace(a, b, n + 1)
    result = 0
    # For every interval (or Strip/Streifen)
    for strip in range(n):
        a, b = intervals[strip], intervals[strip + 1]
        # Tangententrapezformel
        result += (b - a) * (calc_function(f, ((a + b) / 2)))
    print("Tangententrapez Regel: " + str(result))
    return result


# summierte Simpsonfunktion
def simpson_regel(f, a, b, n):
    # Create an interval from a to b in n steps
    intervals = np.linspace(a, b, n + 1)
    result = 0
    # For every interval (or Strip/Streifen)
    for strip in range(n):
        a, b = intervals[strip], intervals[strip + 1]
        # Simpsonscheformel
        result += ((b - a) / 6) * ((calc_function(f, a)) + (4 * calc_function(f, (a + b) / 2)) + (calc_function(f, b)))
    print("Simpson Regel: " + str(result))
    return result


# Integral 1
print("Integral 1")

# Sehnkanten Trapez
calc_integral_diff(lambda x: np.pi*1/x, 1, 2, sekanten_trapez_regel(str(np.pi) + "*1/x", 1, 2, 1))
calc_integral_diff(lambda x: np.pi*1/x, 1, 2, sekanten_trapez_regel(str(np.pi) + "*1/x", 1, 2, 10))
calc_integral_diff(lambda x: np.pi*1/x, 1, 2, sekanten_trapez_regel(str(np.pi) + "*1/x", 1, 2, 100))

# Tangenz
calc_integral_diff(lambda x: np.pi*1/x, 1, 2, tangenten_trapez_regel(str(np.pi) + "*1/x", 1, 2, 1))
calc_integral_diff(lambda x: np.pi*1/x, 1, 2, tangenten_trapez_regel(str(np.pi) + "*1/x", 1, 2, 10))
calc_integral_diff(lambda x: np.pi*1/x, 1, 2, tangenten_trapez_regel(str(np.pi) + "*1/x", 1, 2, 100))

# Simpsons
calc_integral_diff(lambda x: np.pi*1/x, 1, 2, simpson_regel(str(np.pi) + "*1/x", 1, 2, 1))
calc_integral_diff(lambda x: np.pi*1/x, 1, 2, simpson_regel(str(np.pi) + "*1/x", 1, 2, 10))
calc_integral_diff(lambda x: np.pi*1/x, 1, 2, simpson_regel(str(np.pi) + "*1/x", 1, 2, 100))


# Integral 2
print("Integral 2")

# Sehnkanten Trapez
calc_integral_diff(lambda x: x**3+3*x**2, 0, 1, sekanten_trapez_regel("x**3+3*x**2", 0, 1, 1))
calc_integral_diff(lambda x: x**3+3*x**2, 0, 1, sekanten_trapez_regel("x**3+3*x**2", 0, 1, 10))
calc_integral_diff(lambda x: x**3+3*x**2, 0, 1, sekanten_trapez_regel("x**3+3*x**2", 0, 1, 100))

# Tangenz
calc_integral_diff(lambda x: x**3+3*x**2, 0, 1, tangenten_trapez_regel("x**3+3*x**2", 0, 1, 1))
calc_integral_diff(lambda x: x**3+3*x**2, 0, 1, tangenten_trapez_regel("x**3+3*x**2", 0, 1, 10))
calc_integral_diff(lambda x: x**3+3*x**2, 0, 1, tangenten_trapez_regel("x**3+3*x**2", 0, 1, 100))

# Simpsons
calc_integral_diff(lambda x: x**3+3*x**2, 0, 1, simpson_regel("x**3+3*x**2", 0, 1, 1))
calc_integral_diff(lambda x: x**3+3*x**2, 0, 1, simpson_regel("x**3+3*x**2", 0, 1, 10))
calc_integral_diff(lambda x: x**3+3*x**2, 0, 1, simpson_regel("x**3+3*x**2", 0, 1, 100))

# Integral 3
print("Integral 3")

# Sehnkanten Trapez
calc_integral_diff(lambda x: np.cos(x), -np.pi/2, np.pi/2, sekanten_trapez_regel("cos(x)", -np.pi/2, np.pi/2, 1))
calc_integral_diff(lambda x: np.cos(x), -np.pi/2, np.pi/2, sekanten_trapez_regel("cos(x)", -np.pi/2, np.pi/2, 10))
calc_integral_diff(lambda x: np.cos(x), -np.pi/2, np.pi/2, sekanten_trapez_regel("cos(x)", -np.pi/2, np.pi/2, 100))

# Tangenz
calc_integral_diff(lambda x: np.cos(x), -np.pi/2, np.pi/2, tangenten_trapez_regel("cos(x)", -np.pi/2, np.pi/2, 1))
calc_integral_diff(lambda x: np.cos(x), -np.pi/2, np.pi/2, tangenten_trapez_regel("cos(x)", -np.pi/2, np.pi/2, 10))
calc_integral_diff(lambda x: np.cos(x), -np.pi/2, np.pi/2, tangenten_trapez_regel("cos(x)", -np.pi/2, np.pi/2, 100))

# Simpsons
calc_integral_diff(lambda x: np.cos(x), -np.pi/2, np.pi/2, simpson_regel("cos(x)", -np.pi/2, np.pi/2, 1))
calc_integral_diff(lambda x: np.cos(x), -np.pi/2, np.pi/2, simpson_regel("cos(x)", -np.pi/2, np.pi/2, 10))
calc_integral_diff(lambda x: np.cos(x), -np.pi/2, np.pi/2, simpson_regel("cos(x)", -np.pi/2, np.pi/2, 100))