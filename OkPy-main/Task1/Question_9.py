import math

def myBuild5(x):
    k = 0.00000000000000000001
    operator = 1
    f = 1
    s = 1 - (x**2/6)
    i = 4
    while (abs(f-s)>k):
        f = s
        if operator == 1:
            s = f - (x**i/math.factorial(i))
            operator = 0
        else:
            s = f + (x**i/math.factorial(i))
            operator = 1
        i += 2
    print("Tự tính:",f)

def fac5(x):
    print("Máy tính:", math.sin(x)/x)

x = float(input("Nhập giá trị x: "))
myBuild5(x)
fac5(x)