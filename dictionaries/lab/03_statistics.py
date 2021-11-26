data = input()

products = {}

while not data == "statistics":
    product_name, product_qty = data.split(": ")

    if product_name not in products:
        products[product_name] = int(product_qty)
    else:
        products[product_name] += int(product_qty)

    data = input()

print("Products in stock:")

for key, value in products.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")