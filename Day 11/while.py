
food = input("Enter your food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter your another food you like (q to quit): ")
else:
    print(f"You like {food}")
