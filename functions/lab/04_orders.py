def calculate_total_price(product, qty):
    if product == "coffee":
        return qty * 1.50
    elif product == "water":
        return qty * 1.00
    elif product == "coke":
        return qty * 1.40
    elif product == "snacks":
        return qty * 2.00

type_product = input()
amount = int(input())

total_amount = calculate_total_price(type_product, amount)

print(f"{total_amount:.2f}")