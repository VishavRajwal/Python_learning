#SHOPPING CART 

fruits = [] 
prices = []
total = 0

while True:
    fruit = input("Enter the fruit you want to buy ( q to quit): ")
    if fruit == "q":
        break
    else:
        price = float(input(f"Enter the price of the {fruit}: $"))
        fruits.append(fruit)
        prices.append(price)

print("------YOUR SHOPPING LIST------")

for fruit in fruits:
    print(fruit)

for price in prices:
    total = total + price

 
print(f"Your total is: ${total}")
                                        