print("Welcome to the Python Pizza Place")

bill = 0
pizza_mapping = {
    "S": 15,
    "M": 20,
    "L": 25
}

size = input("What size pizza do you want? S, M or L: ")


while size not in pizza_mapping:
    print("Invalid size entered. Let's try again.")
    size = input("What size pizza do you want? S, M or L: ")

price : int = pizza_mapping[size]
print(price)

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if pepperoni == "Y":
    if size == "S":
        price += 2
    if size != "S":
        price += 3

if extra_cheese == "Y":
    price += 3

print(f"The pizza price is ${price}")
