# positional

# import time

# def count(end, start=0):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("done")

# count(10)


# keyword

# for x in range(1, 11):
#     print(x, end=" ")

# print("1", "2", "3", "4", "5", sep="-")

# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"

# phone_num = get_phone(country=880, area=183, first=170, last=7890)
# print(phone_num)



# arbitrary

# def display_main(*args):
#     for arg in args:
#         print(arg, end=" ")

# ("dr.", "adolf", "kernel", "3")



# args+kwargs

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip_code')}")

shipping_label("dr.", "kernel", "pwn", "3",
               street="123 street",
               pobox="123 po-box",
               city="detroit",
               state="nigga",
               zip_code="55010")