def odd_even_sum(numbers):
    """Returns the sum of all even and all odd
    digits in the given number"""

    numbers_list = [int(num) for num in str(numbers)]

    odd_nums = []
    even_nums = []

    for index in range(len(numbers_list)):
        if numbers_list[index] % 2 == 0:
            even_nums.append(numbers_list[index])
        elif not numbers_list[index] % 2 == 0:
            odd_nums.append(numbers_list[index])

    return f"Odd sum = {sum(odd_nums)}, Even sum = {sum(even_nums)}"


entry_numbers = int(input())

print(odd_even_sum(entry_numbers))

# def odd_and_even_sum_of_digits(num: str):
#     """Returns the sums of all the odd and
#     all the even digits in the received number"""
#
#     odd_sum = 0
#     even_sum = 0
#
#     for ch in num:
#         digit = int(ch)
#
#         if digit % 2 == 0:
#             # even digit
#             even_sum += digit
#         else:
#             # odd digit
#             odd_sum += digit
#
#     return f"Odd sum = {odd_sum}, Even sum = {even_sum}"
#
# number = input()
#
# result = odd_and_even_sum_of_digits(number)
#
# print(result)