import math

def exp_maclaurin(x, eps):
    # Khởi tạo biến ban đầu
    n = 0
    sum = 0
    term = 1

    # Tính giá trị của chuỗi đến khi đạt được độ chính xác mong muốn
    while abs(term) > eps:
        sum += term
        n += 1
        term = x ** n / math.factorial(n)
    return sum

x = 2
eps = 0.00001

# Tính và in ra giá trị của chuỗi tại x = 2
print("Giá trị của chuỗi tại x =",x, "là:",exp_maclaurin(x, eps))