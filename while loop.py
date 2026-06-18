# Execute some code while some conditions remain true

#name = input("Enter your name: ")

#while name == "":
#    name = input("Enter your name: ")



#age = int(input("Enter your age: "))

#while age < 1:
#    print("Your age must be greater than or equal to one")
#    age = int(input("Please enter your age: "))

#print(f"Hello {name}")
#print(f"You are {age} years old")



#food = input("Enter a food you like (q to quit): ")

#while not food == "q":
#    print(f"You like {food}")
#    food = input("Enter a food you like (q to quit): ")

#print("bye")



num = int(input("enter a number (1-10): "))

while num < 1 or num > 10:
    print("Please enter a number between 1 and 10")
    num = int(input("enter a number (1-10): "))

print(f"the number is {num}")