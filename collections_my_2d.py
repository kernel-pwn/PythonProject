#fruits =     ["apple", "banana", "cherry", "coconut"]
#vegetables = ["celery", "carrots", "potatoes"]
#meats =      ["chicken", "fish", "turkey"]

#groceries = [fruits, vegetables, meats]

#print(groceries[0][0])



groceries = [["apple", "banana", "cherry", "coconut"],
             ["celery", "carrots", "potatoes"],
             ["chicken", "fish", "turkey"]]

for grocery in groceries:
    for item in grocery:
        print(item, end=" ")
    print()