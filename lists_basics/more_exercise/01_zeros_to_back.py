my_list = input().split(", ")

for i in range(len(my_list)):
    my_list[i] = int(my_list[i])

for j in my_list:
    if j == 0:
        my_list.remove(j)
        my_list.append(j)

print(my_list)
