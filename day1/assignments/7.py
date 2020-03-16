def hypotenuse(p, b):
    return (p*p + b*b ) ** 0.5

p = float(input("perpendicular="))
b = float(input("base="))
h = hypotenuse(p, b)

print("Hypotenuse = ", h)