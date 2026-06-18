# Evaluate multiple conditions (or, and, not)

#temp = 20
#is_raining = True

#if temp > 35 or temp < 0 or is_raining:
#    print("cancelled")
#else:
#    print("Lets go")


temp = 25
is_sunny = False

if temp >= 25 and is_sunny:
    print("it is hot")
    print("It is sunny")
elif temp < 15 and is_sunny:
    print("it is cold")
    print("It is sunny")
elif 25 > temp > 15 and is_sunny:
    print("it is perfect and sunny")
elif temp >= 25 and not is_sunny:
    print("it is hot")
    print("It is cloudy")
elif temp < 15 and not is_sunny:
    print("it is cold")
    print("It is sunny")
elif 25 > temp > 15 and not is_sunny:
    print("it is perfect but cloudy")