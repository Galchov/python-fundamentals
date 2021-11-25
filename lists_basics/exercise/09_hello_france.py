items_and_prices = input().split("|")
budget = float(input())

# Clothes - 50.00
# Shoes - 35.00
# Accessories - 20.50
new_prices = []
expenses = []

for item in items_and_prices:
    trade = item.split("->")

    if budget < float(trade[1]):
        continue

    if trade[0] == "Clothes" and float(trade[1]) <= 50.00:
        budget -= float(trade[1])
        expenses.append(float(trade[1]))
        new_prices.append(float(trade[1]) + float(trade[1]) * 0.40)

    elif trade[0] == "Shoes" and float(trade[1]) <= 35.00:
        budget -= float(trade[1])
        expenses.append(float(trade[1]))
        new_prices.append(float(trade[1]) + float(trade[1]) * 0.40)

    elif trade[0] == "Accessories" and float(trade[1]) <= 20.50:
        budget -= float(trade[1])
        expenses.append(float(trade[1]))
        new_prices.append(float(trade[1]) + float(trade[1]) * 0.40)

for price in new_prices:
    print(f"{price:.2f}", end=" ")

print(f"\nProfit: {sum(new_prices) - sum(expenses):.2f}")

if sum(new_prices) + budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")