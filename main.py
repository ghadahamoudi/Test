import math


radius = float(input("Enter radius: "))

circumference = 2*math.pi*radius

print(f"Circumference: {round(circumference)}")

area = math.pi * pow(radius, 2)

print(f"Area: {round(area)}cm^2")