import math

def mySin(x):
    k = 0.0000000000001  # sai số mong muốn
    f = x  # giá trị ban đầu của f
    s = 0  # giá trị ban đầu của s
    mu = 3  # mũ của x
    operator = 0  # biến để thay đổi dấu (+/-)

    while abs(f - s) > k:
        s = f
        if operator == 0:
            f -= (x ** mu) / math.factorial(mu)
            operator = 1
        else:
            f += (x ** mu) / math.factorial(mu)
            operator = 0

        mu += 2  # tăng mũ lên 2 để tính tiếp tục các số lẻ
    return f

x = 0.5
sin_x = mySin(x)
print("Giá trị của sin({}) là: {}".format(x, sin_x))