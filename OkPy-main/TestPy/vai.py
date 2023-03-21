import math

class Shape:
    def chu_vi(self):
        pass
    
    def dien_tich(self):
        pass

# !tinh chu vi, dien tich Circle voi r, x, y(radius, toa do x,y)
class Circle(Shape):
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
        
    def chu_vi(self):
        return 2*math.pi*self.r
    
    def dien_tich(self):
        return math.pi*self.r*self.r

# !tinh chu vi, dien tich Rect voi width, height, x, y
class Rect(Shape):
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
    def chu_vi(self):
        return 2*(self.width + self.height)
    
    def dien_tich(self):
        return self.width*self.height

# !tinh chu vi, dien tich Triangle voi a, b, c, x, y (a, b, c lan luot la ba canh cua tam giac)
class Triangle(Shape):
    def __init__(self, a, b, c, x, y):
        self.a = a
        self.b = b
        self.c = c
        self.x = x
        self.y = y
        
    def chu_vi(self):
        return self.a + self.b + self.c
    
    def dien_tich(self):
        p = (self.a + self.b + self.c)/2
        if p*(p-self.a)*(p-self.b)*(p-self.c) < 0:
            raise ValueError("Khong phai tam giac")
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))