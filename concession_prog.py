menu = {"pizza": 4.00, "nachos": 7.00, "chips": 1.30, "pretzel": 3.00, "hotdog": 2.00}

cart = []
total = 0

print("-------- MENU --------")
for key, value in menu.items():
    print(f"{key:10}: ${value :.2f}")
print("-----------------------")


while True:
    food = input("Select an item (q to quit) : ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("-------YOUR ORDER--------")

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"total is : ${total:.2f}")
