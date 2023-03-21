from vai import Circle, Rect, Triangle

def read_input_file(filename):
    shapes = []
    with open(filename, "r") as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line == "#Rect":
                width, height = map(int, lines[i+1].strip().split())
                x, y = map(int, lines[i+2].strip().split())
                shapes.append(Rect(width, height, x, y))
                i += 3
            elif line == "#Circle":
                radius = int(lines[i+1].strip())
                x, y = map(int, lines[i+2].strip().split())
                shapes.append(Circle(radius, x, y))
                i += 3
            elif line == "#Triangle":
                sides = list(map(int, lines[i+1].strip().split()))
                x, y = map(int, lines[i+2].strip().split())
                shapes.append(Triangle(*sides, x, y))
                i += 3
            else:
                i += 1
    return shapes

def main():
    shapes = read_input_file("input.txt")
    
    # Tính chu vi và diện tích của các hình
    max_chu_vi = 0
    max_dien_tich = 0
    max_chu_vi_shape = None
    max_dien_tich_shape = None
    
    for shape in shapes:
        chu_vi = shape.chu_vi()
        dien_tich = shape.dien_tich()
        
        if chu_vi > max_chu_vi:
            max_chu_vi = chu_vi
            max_chu_vi_shape = shape
        
        if dien_tich > max_dien_tich:
            max_dien_tich = dien_tich
            max_dien_tich_shape = shape
    
    # In kết quả
    print("Hinh co chu vi lon nhat la:")
    print(max_chu_vi_shape.__class__.__name__, "chu vi =", max_chu_vi)
    print("Hinh co dien tich lon nhat la:")
    print(max_dien_tich_shape.__class__.__name__, "dien tich =", max_dien_tich)

if __name__ == "__main__":
    main()
