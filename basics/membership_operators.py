# used to test whether a value or variable is found in a sequence
# (string, list, tuple, set or dictionary)
# 1. in     2. not in

# word = "apple"

# letter = input("guess a letter: ")

# if letter in word:      # not in
#     print(f"there is a {letter}")
# else:
#     print(f"no {letter}")



# students = {"SpongeBob", "patrick", "sandy"}

# student = input("Enter student name: ")

# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} is not a student")



# grades = {"sandy": "A", "squidward": "B", "spongebob": "C", "patrick": "D"}

# student = input("Enter your name: ")

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")



email = "pwn@gmail.com"

if "@" in email and "." in email:
    print("Email address is valid")
else:
    print("Email address is invalid")