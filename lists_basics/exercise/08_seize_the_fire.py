cell_fire = input().split("#")
water = int(input())

total_effort = 0
total_fire = 0
put_out_cells = []

for cell in cell_fire:
    fire_info = cell.split(" = ")
    type_of_fire = str(fire_info[0])
    range_of_fire = int(fire_info[1])

    if water < int(fire_info[1]):
        continue

    if type_of_fire == "Low" and 1 <= range_of_fire <= 50:
        water -= int(fire_info[1])
        total_fire += int(fire_info[1])
        total_effort += (0.25 * int(fire_info[1]))
        put_out_cells.append(int(fire_info[1]))

    elif type_of_fire == "Medium" and 51 <= range_of_fire <= 80:
        water -= int(fire_info[1])
        total_fire += int(fire_info[1])
        total_effort += (0.25 * int(fire_info[1]))
        put_out_cells.append(int(fire_info[1]))

    elif type_of_fire == "High" and 81 <= range_of_fire <= 125:
        water -= int(fire_info[1])
        total_fire += int(fire_info[1])
        total_effort += (0.25 * int(fire_info[1]))
        put_out_cells.append(int(fire_info[1]))

print("Cells:")

for el in put_out_cells:
    print(f" - {el}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire:.0f}")