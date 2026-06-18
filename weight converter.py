# weight converter

weight = float(input("Please enter your weight: "))
unit = input("kilogram or pound? (K or L): ").lower()

if unit == "k":
    weight = weight * 2.205
    unit = "lbs"
    print(f"your weight is {round(weight, 2)} {unit}")
elif unit == "l":
    weight = weight / 2.205
    unit = "kgs"
    print(f"your weight is {round(weight, 2)} {unit}")
else:
    print(f"{unit} is not valid")
