number_of_commands = int(input())

parking_database = {}

for _ in range(number_of_commands):
    command = input()
    cmd_info = command.split()

    if cmd_info[0] == "register":

        if cmd_info[1] not in parking_database:
            parking_database[cmd_info[1]] = cmd_info[2]
            print(f"{cmd_info[1]} registered {cmd_info[2]} successfully")
        else:
            print(f"ERROR: already registered with plate number {cmd_info[2]}")

    elif cmd_info[0] == "unregister":

        if cmd_info[1] not in parking_database:
            print(f"ERROR: user {cmd_info[1]} not found")
        else:
            print(f"{cmd_info[1]} unregistered successfully")
            parking_database.pop(cmd_info[1])

for key, value in parking_database.items():
    print(f"{key} => {value}")
