import math

calc_area = lambda r: (r**2) * math.pi

radius = int(input("Enter radius:"))
ans = calc_area(radius)
print(f"Area of the circle:{ans}")