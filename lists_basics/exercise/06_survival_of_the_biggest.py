numbers_list = input().split()
n = int(input())

for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])

for i in range(n):
    min_element = min(numbers_list)

    numbers_list.remove(min_element)

for i in range(len(numbers_list)):
    numbers_list[i] = str(numbers_list[i])

print(', '.join(numbers_list))

# numbers_list = input().split()
# numbers_to_remove = int(input())
#
# for i in range(len(numbers_list)):
#     numbers_list[i] = int(numbers_list[i])
#
# for num in range(numbers_to_remove):
#     numbers_list.remove(min(numbers_list))
#
# for i in range(len(numbers_list)):
#     numbers_list[i] = str(numbers_list[i])
#
# print(", ".join(numbers_list))