# python object-oriented programming

# object = A "bundle" of related attributes (variables) and methods (functions)
# ex. phone, cup, book
# you need a class to create many objects

# class = (blueprint) used to design the structure and layout of an object

class car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"you drive the car {self.model}")

    def stop(self):
        print(f"you stop the car {self.model}")

    def descirbe(self):
        print(f"{self.year} {self.color} {self.model}")

car1 = car("Pagani", 2026, "black", False)
car2 = car("Miata", 2025, "pink", True)
car3 = car("mustang", 2024, "blue", True)

#    print(car3.model)
#    print(car3.year)
#    print(car3.color)
#    print(car3.for_sale)

# car1.drive()
# car1.stop()

car1.descirbe()