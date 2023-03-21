import math

def myBuild3(x):
    if x <= -1 or x >= 1:
        print("Error: x thuộc khoảng (-1, 1)")
        return None
    else:
        n = 1
        result = 0
        while True:
            if n % 2 == 0:
                result -= x**n / n
            else:
                result += x**n / n
            n += 2
            if abs(x**n / n) < 1e-10:
                break
        return result

x = 0.5
print("ln((1+x)/(1-x)) = ", 2*myBuild3(x))