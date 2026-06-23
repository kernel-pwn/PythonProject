# A default value for certain parameters
# default is used when that argument is omitted
# make your funcs more flexible, reduces # of arguments
# 1. positional, 2. Default, 3. keyword, 4. arbitrary



# default

# def net_price(list_price, discount=0, tax=0.05):
#     return list_price * (1-discount) * (1 + tax)

# print(net_price(500))
# print(net_price(500, 0.1))
# print(net_price(500, 0.1,0))



# keyword

# def hello(greeting, title, firstname, lastname):
#     print(f"{greeting} {title}{firstname} {lastname}")

# hello("hello", "mr.", "kernel", "pwn")
# hello("hello", firstname="kernel", lastname="pwn", title="mr.")



# arguments
# args   = allows you to pass multiple non-key arguments
# kwargs = allows you to pass multiple keyword arguments
# * unpacking operator

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1, 2, 3, 4, 5))

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 street", city="detroit", state="nigga", zip="165")