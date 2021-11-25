tank_capacity = 255    # Water tank capacity in liters
n = int(input())

liters_in_the_tank = 0

for line in range(1, n + 1):
    water_liters = int(input())
    liters_in_the_tank += water_liters

    if liters_in_the_tank > tank_capacity:
        print("Insufficient capacity!")
        liters_in_the_tank -= water_liters
        continue

print(liters_in_the_tank)