# shopping cart program

item = input("what item would you like?: ")
price = float(input("what is the price?: "))
quantity = int(input("how many items would you like?: "))
total_price = price * quantity

print(f"U hv bought {quantity} {item}/s")
print(f"your total price is ${total_price}")