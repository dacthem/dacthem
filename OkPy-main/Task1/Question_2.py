import math

def mul(y):
    s = 1
    for i in range(1, y+1, 1):
        s *= i
    return s

eps = 0.000001
x = float(input("Nhập số x bất kì trong khoảng (-1, 1): "))
first = 1 / pow(1 + x, 3)
second = 1
n = 2
term = (-2 * 3 / 2) * x

while abs(term) > eps:
    second += term
    n += 1
    term *= ((n + 1) * (n + 2)) / ((n - 1) * n)
    term *= x
print("Giá trị của 1/(1+x)^3 là: ", first)
print("Giá trị của biểu thức bên phải là: ", second)
print("Giá trị chênh lệch giữa hai bên là: ", abs(first - second))
print("Giá trị chênh lệch giữa hai bên nhỏ hơn eps là : ", abs(first - second) < eps)