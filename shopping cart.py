# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("enter food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"enter price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("---- YOUR CART ----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total = total + price

print()
print(f"total price is ${total}")