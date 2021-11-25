numbers = [int(n) for n in input().split(", ")]
count_of_beggars = int(input())

collected = []
index = 0

for i in range(count_of_beggars):
    current_list = []

    for index in range(0, len(numbers) + 1, count_of_beggars):
        index += i
        if index < len(numbers):
            current_list.append(numbers[index])

    collected.append(sum(current_list))

print(collected)

# nums_str = input().split(', ')
# count = int(input())
#
# nums = []
#
# for num in nums_str:
#     nums.append(int(num))
#
# result_sum = [0] * count
#
# for i in range(len(nums)):
#     index = i % count
#     result_sum[index] += nums[i]
#
# print(result_sum)