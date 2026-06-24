# another way to achieve polymorphism besides inheritance
# object must have the minimum necessary attributes/methods
# "if it looks like aa duck and quacks like a duck, it must be a duck."

class animal:
    alive = True

class dog(animal):
    def speak(self):
        print("I am a dog.")

class cat(animal):
    def speak(self):
        print("I am a cat.")

class car:

    alive = False

    def speak(self):
        print("I am a car.")

animals = [dog(), cat(), car()]

for animal in animals:
    animal.speak()
    print(animal.alive)