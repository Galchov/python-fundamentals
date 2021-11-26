command = input()

resources = {}
resource_name = ''
line = 1

while not command == "stop":
    if not line % 2 == 0:
        resource_name = command
    else:
        if resource_name in resources:
            resources[resource_name] += int(command)
        else:
            resources[resource_name] = int(command)

    line += 1

    command = input()

for key, value in resources.items():
    print(f"{key} -> {value}")