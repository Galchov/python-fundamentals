party_size = int(input())
days = int(input())

total_coins = 0

for day in range(1, days + 1):

    if day % 10 == 0:    # Start of the day
        party_size -= 2

    if day % 3 == 0 and day % 5 == 0:
        party_size += 5

    total_coins += 50 - (party_size * 2)    # Every day

    if day % 3 == 0:    # Every third day
        total_coins -= party_size * 3

    if day % 5 == 0:    # Every fifth day
        total_coins += party_size * 20

        if day % 3 == 0:    # 15th day
            total_coins -= party_size * 2

coins_each = int(total_coins / party_size)

print(f"{party_size} companions received {coins_each} coins each.")