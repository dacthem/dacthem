import math

def myLn(x, n):
    if x <= -1 or x > 1:
        return "Error: không thuộc khoảng (−1, +1]"
    elif x == 1:
        return 0
    else:
        s = 0
        for i in range(1, n+1):
            s += ((-1)**(i+1)) * (x**i) / i
        return s

# ví dụ: tính ln(1.5) với n = 10
print(myLn(0.5, 10))  # kết quả: -0.6931471805599453
print(math.log(1.5))  # so sánh với kết quả tính toán sẵn của Python