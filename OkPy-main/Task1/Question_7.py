import math

def myCos(x):
    k = 0.0000000000001  # sai số mong muốn
    f = 1  # giá trị ban đầu của f
    s = 0  # giá trị ban đầu của s
    mu = 2  # mũ của x
    operator = 0  # biến để thay đổi dấu (+/-)

    while abs(f - s) > k:
        s = f
        if operator == 0:
            f -= (x ** mu) / math.factorial(mu)
            operator = 1
        else:
            f += (x ** mu) / math.factorial(mu)
            operator = 0

        mu += 2  # tăng mũ lên 2 để tính tiếp tục các số chẵn
    return f

x = 0.5
cos_x = myCos(x)
print("Giá trị của cos({}) là: {}".format(x, cos_x))