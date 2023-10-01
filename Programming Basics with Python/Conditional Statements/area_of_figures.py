from math import pi

name = (input())

if name == "square":
    s = float(input())
    square_area = s * s
    print(f"{square_area:.3f}")

elif name == "rectangle":
    length_of_rectangle1 = float(input())
    length_of_rectangle2 = float(input())
    rect_area = length_of_rectangle1 * length_of_rectangle2
    print(f"{rect_area:.3f}")

elif name == "circle":
    radius_of_circle = float(input())
    circle_area = pi * radius_of_circle * radius_of_circle
    print(f"{circle_area:.3f}")

elif name == "triangle":
    triangle_height = float(input())
    triangle_length = float(input())
    triangle_area = 0.5 * triangle_length * triangle_height
    print(f"{triangle_area:.3f}")
