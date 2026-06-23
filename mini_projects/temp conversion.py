# temperature conversion

unit = input("is it Celsius or Fahrenheit? (C/F): ").lower()
temp = float(input("Enter Temperature: "))

if unit == "c":
    temp = round((temp * 9/5) + 32, 2)
    print(f"{temp} F")
elif unit == "f":
    temp = round((temp - 32) * 5/9, 2)
    print(f"{temp} C")
else:
    print(f"{unit} is an invalid option.")