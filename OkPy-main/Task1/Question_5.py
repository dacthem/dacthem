import math

def myBuild2(x):
  k = 0.00000000000000000001
  f = 1
  s = f - 1/2 * x

  mu = 3
  operator = 1
  hstu = 3
  mau = 2 * 4
  hsmau = 6

  while (abs(f - s) > k):
    f = s
    if operator == 1:
      if mu - 2 == 0:
        s = f
      else:
        s = f + (((mu - 1) / mu) * ((mu - 3) / (mu - 2)) * (x**mu))
      operator = 0
    else:
      if mu - 2 == 0:
        s = f
      else:
        s = f - (((mu - 1) / mu) * ((mu - 3) / (mu - 2)) * (x**mu))
      operator = 1

    mu = mu + 2
    hstu = hstu + 2
    mau = mau * hsmau
    hsmau = hsmau + 2

  print("Tự tính: ", f)

def fac2(x):
  print("Máy tính: ", 1 / math.sqrt(1 + x))

x = 0.5

fac2(x)
myBuild2(x)