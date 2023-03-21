import math

def ln_1_minus_x(x):
    if x <= -1 or x >= 1:
        raise ValueError("x phải nằm trong khoảng (-1, 1)")
    
    result = 0
    i = 1
    while True:
        term = (-1)**(i+1) * x**i / i
        if abs(term) < 1e-6:
            break
        result += term
        i += 1
    
    return result

x = 0.5
print(ln_1_minus_x(x))  # -0.6931471805999999
print(math.log(1-x))   # -0.6931471805599453