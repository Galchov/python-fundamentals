numbers = [int(num) for num in input().split(", ")]

boundary = 10

while len(numbers) > 0:
    nums_group_of_10s = [el for el in numbers if el <= boundary]
    numbers = [x for x in numbers if x not in nums_group_of_10s]
    print(f"Group of {boundary}'s: {nums_group_of_10s}")
    boundary += 10