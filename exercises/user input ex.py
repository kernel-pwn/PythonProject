# rectangle area calc

length = float(input("length of rectangle: "))
width = float(input("width of rectangle: "))
measurement = input("cm/m/km: ").lower()

area = length * width

print(f"the area of rectangle is {area} {measurement}²")
