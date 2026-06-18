# {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to utmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 3000.1459
price2 = -9870.6523
price3 = 1200.34242

print(f"price1 = ${price1:.2f}")
print(f"price2 = ${price2:10}")
print(f"price3 = ${price3:010}")
print(f"price1 = ${price1:<10}")
print(f"price2 = ${price2:>10}")
print(f"price3 = ${price3:^10}")
print(f"price1 = ${price1:+}")
print(f"price2 = ${price2: }")
print(f"price3 = ${price3:,}")
print(f"price1 = ${price1:,.2f}")
print(f"price2 = ${price2:+,.2f}")
print(f"price3 = ${price3:}")
