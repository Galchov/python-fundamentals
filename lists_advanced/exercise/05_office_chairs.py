rooms = int(input())

free_chairs = 0
no_chairs = False

for room in range(1, rooms + 1):
    n = input().split()

    if len(n[0]) < int(n[1]):
        print(f"{int(n[1]) - len(n[0])} more chairs needed in room {room}")
        no_chairs = True
    else:
        free_chairs += len(n[0]) - int(n[1])

if not no_chairs:
    print(f"Game On, {free_chairs} free chairs left")
