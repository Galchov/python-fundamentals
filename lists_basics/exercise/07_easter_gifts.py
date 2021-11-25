gifts_list = input().split(" ")

command_1 = "OutOfStock"
command_2 = "Required"
command_3 = "JustInCase"

command_end = "No Money"
command = input()

while command != command_end:
    list_of_command = command.split(" ")

    if list_of_command[0] == command_1:
        for gift in gifts_list:
            if gift == list_of_command[1]:
                index_of_el = gifts_list.index(gift)
                gifts_list[index_of_el] = "None"

    elif list_of_command[0] == command_2:
        if 0 <= int(list_of_command[2]) < len(gifts_list):
            gifts_list[int(list_of_command[2])] = list_of_command[1]

    elif list_of_command[0] == command_3:
        gifts_list[-1] = list_of_command[1]

    command = input()

for gift in gifts_list:
    if gift != "None":
        print(gift, end=" ")


# gifts = input().split(" ")
# command = input()
#
# while not command == "No Money":
#     command_info = command.split(" ")
#
#     if "OutOfStock" in command_info:
#         for i, item in enumerate(gifts):
#             if item == command_info[1]:
#                 gifts[i] = "None"
#
#     elif "Required" in command_info:
#         if 0 <= int(command_info[2]) < len(gifts):
#             gifts[int(command_info[2])] = command_info[1]
#
#     elif "JustInCase" in command_info:
#         gifts.pop(-1)
#         gifts.append(command_info[1])
#
#     command = input()
#
# for gift in gifts:
#     if not gift == "None":
#         print(gift, end=" ")