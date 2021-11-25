factor = int(input())
count = int(input())

numbers_list = []

for num in range(factor, factor * count + 1):
    if num % factor == 0:
        numbers_list.append(num)

print(numbers_list)

# factor = int(input())
# count = int(input())
#
# new_list = []
#
# for number in range(1, count + 1):
#     new_list.append(number * factor)
#
# print(new_list)