numbers_str = input().split()

inverted_numbers = []

for number in numbers_str:
    number_inverted = int(number) * -1

    inverted_numbers.append(number_inverted)

print(inverted_numbers)