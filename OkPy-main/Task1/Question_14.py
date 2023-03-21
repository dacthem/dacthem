import math

def myCosh(x):
    sum = 1
    term = 1
    n = 2
    while abs(term) > 1e-10:
        term *= x**2 / ((n-1) * n)
        sum += term
        n += 2
    return sum

x = 1.5
print(f"cosh({x}) = {myCosh(x)}")