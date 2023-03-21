import math

def myBuild5(x):
  k = 0.00000000000000000001
  f = 0
  s = x
  n = 1

  while (abs(f - s) > k):
    f = s
    s += ((-1)**n) * (x**(2*n + 1)) / (2*n + 1)
    n += 1

  return s

x = 0.5
print("Tự tính: ", myBuild5(x))
print("Máy tính: ", math.atan(x))