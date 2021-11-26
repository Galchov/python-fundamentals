command = input()

products_dict = {}

while not command == "buy":
    product_name, product_price, product_qty = command.split()
    price = float(product_price)
    quantity = int(product_qty)

    if product_name not in products_dict:
        products_dict[product_name] = {"Price": price, "Quantity": quantity}
    else:
        products_dict[product_name]["Quantity"] += quantity
        products_dict[product_name]["Price"] = price

    command = input()

for key, value in products_dict.items():
    total_price = value["Price"] * value["Quantity"]
    print(f"{key} -> {total_price:.2f}")