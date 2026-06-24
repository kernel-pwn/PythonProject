# allows a class to inherit attributes and methods from another class
# helps with code reusability and extensibility
# class child(parent)

class animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class dog(animal):
    def speak(self):
        print("woof")

class cat(animal):
    def speak(self):
        print("meow")

class mouse(animal):
    def speak(self):
        print("squeak")

dog = dog("scooby")
cat = cat("garfield")
mouse = mouse("mickey")

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
cat.speak()