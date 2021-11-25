string_first = input().split(", ")
string_second = input().split(", ")

substrings = []

for item in string_first:
    for word in string_second:
        if item in word:
            substrings.append(item)
            break

print(substrings)

# Other way to solve the problem
# substrings = [item for item in string_first if any(word for word in string_second if item in word)]
