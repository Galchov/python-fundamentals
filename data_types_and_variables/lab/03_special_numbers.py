n = int(input())

for number in range(1, n + 1):
    num_as_string = str(number)
    result = 0
    for symbol in num_as_string:
        result += int(symbol)
    if result == 5 or result == 7 or result == 11:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")