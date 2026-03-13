import math

def calc_area(r):
    return math.pi*(int(r)^2)

radius = input("Enter radius:")
ans = calc_area(radius)
print(f"Area of the circle:{ans}")