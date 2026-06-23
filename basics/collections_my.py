# Single "variable" used to store multiple values



# list = [] ordered and changeable. Duplicates ok

#fruits = ["apple", "banana", "cherry", "coconut"]

#fruits[0] = "orange"
#fruits.append("orange")
#fruits.remove("apple")
#fruits.insert(0, "pineapple")
#fruits.sort()
#fruits.reverse()
#fruits.pop(3)
#fruits.clear()
#fruits.index("apple")
#fruits.count("apple")

#print("apple" in fruits)

#for fruit in fruits:
#    print(fruit, end=" ")

#-------------------------------

# tuple = () ordered and unchangeable. Duplicates ok. Faster

#fruits = ("apple", "banana", "cherry", "coconut")

#for fruit in fruits:
#    print(fruit, end=" ")


#--------------------------------


# set = {} unordered and immutable, but add/remove ok. No dupes

#fruits = {"apple", "banana", "cherry", "coconut"}

#fruits.add("mango")
#fruits.remove("apple")
#fruits.pop()
#fruits.clear()


#for fruit in fruits:
#    print(fruit, end=" ")

#--------------------------------


fruits = {"apple", "banana", "cherry", "coconut"}

fruit = input("enter fruit name: ")

if fruit in fruits:
    print(f"{fruit} was found")
else:
    print(f"{fruit} was not found")






