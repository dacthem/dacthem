import math

def sinh(x):
    res = x
    term = x
    i = 1
    while (term != 0):
        term *= x**2 / (2*i) / (2*i + 1)
        res += term
        i += 1
    return res

# ví dụ tính sinh của 1.5
print(sinh(1.5)) # kết quả: 2.1292794550948173