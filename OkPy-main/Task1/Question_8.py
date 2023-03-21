import math

def my_arcsin(x):
  k = 1
  res = x
  tmp = x
  eps = 1e-10 # độ chính xác mong muốn
  
  while abs(tmp) > eps:
    k += 2
    tmp *= (-x**2 * (k - 2) / (k - 1)) # tính phần tử tiếp theo của dãy
    res += tmp / k
    
  return res

x = 0.5
print("Giá trị arcsin của", x, "là:", my_arcsin(x))