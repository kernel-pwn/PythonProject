# A func that prompts the user to enter data. It returns the data as a string

name = input("what is ur name: ")
age = input("what is ur age: ")

age = int(age)
age = age + 1

print(f"hello {name}!")
print("Happy Birthday!")
print(f"you are {age} years old")