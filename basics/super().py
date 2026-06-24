# function used in a child to call methods from a parent class (superclass).
# allows you to extend the functionality of the inherited methods

class shape():
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"it is {self.color} {'filled' if self.is_filled else 'not filled'}")

class circle(shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"it is a circle with an area of {3.14 * self.radius ** 2}")

class square(shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"it is a square with an area of {self.width * self.width}")

class triangle(shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"it is a triangle with an area of {(self.width * self.height) / 2}")

circle = circle(color="red", is_filled=True, radius=5)
square = square(color="green", is_filled=True, width=5)
triangle = triangle(color="blue", is_filled=True, width=7, height=8)

# print(triangle.color)
# print(triangle.is_filled)
# print(triangle.width)
# print(triangle.height)

triangle.describe()