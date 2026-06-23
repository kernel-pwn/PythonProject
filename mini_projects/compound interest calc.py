#compound interest calc

principle = 0
rate = 0
time = 0

#while principle <= 0:
while True:
    principle = float(input("enter your principal amount: "))
    if principle < 0:
        print("principle can't be less than zero")
    else:
        break

#while rate <= 0:
while True:
    rate = float(input("enter your rate amount: "))
    if rate < 0:
        print("rate can't be less than zero")
    else:
        break

#while time <= 0:
while True:
    time = int(input("enter your time: "))
    if time < 0:
        print("time can't be less than zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"balance after {time} year/s is ${total:.2f}")