input_text = input()

result_dict = {}

for char in input_text:
    if char != " ":
        result_dict[char] = input_text.count(char)

print('\n'.join('{} -> {}'.format(key, value) for (key, value) in result_dict.items()))