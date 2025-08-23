# Fruit Inventory Program


fruits = [
    {"name": "apple", "price": 2.5, "quantity": 4},
    {"name": "banana", "price": 1.2, "quantity": 10},
    {"name": "orange", "price": 3.0, "quantity": 3}
]


while True:
    name = input("Enter fruit name (or 'stop' to finish): ")
    if name.lower() == "stop":
        break
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    fruits.append({"name": name, "price": price, "quantity": quantity})


fruit_dict = {
    fruit["name"]: {"price": fruit["price"], "quantity": fruit["quantity"]}
    for fruit in fruits
}


print("\n📊 Fruit Inventory:")
print("{:<10} {:<10} {:<10}".format("Name", "Price", "Quantity"))
print("-" * 30)
for name, details in fruit_dict.items():
    print("{:<10} {:<10} {:<10}".format(name, details["price"], details["quantity"]))