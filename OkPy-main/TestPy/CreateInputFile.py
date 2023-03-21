import random

def generate_input_file(n):
    with open("input.txt", "w") as file:
        for i in range(n):
            shape = random.choice(["Rect", "Circle", "Triangle"])
            file.write("#" + shape + "\n")
            if shape == "Rect":
                width = random.randint(1, 10)
                height = random.randint(1, 10)
                x = random.randint(0, 100)
                y = random.randint(0, 100)
                file.write(f"{width} {height}\n{x} {y}\n")
            elif shape == "Circle":
                radius = random.randint(1, 10)
                x = random.randint(0, 100)
                y = random.randint(0, 100)
                file.write(f"{radius}\n{x} {y}\n")
            else:
                a = random.randint(1, 10)
                b = random.randint(1, 10)
                c = random.randint(1, 10)
                x = random.randint(0, 100)
                y = random.randint(0, 100)
                file.write(f"{a} {b} {c}\n{x} {y}\n")

if __name__ == "__main__":
    generate_input_file(10)