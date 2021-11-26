text = input()
result = ''

i = 0
while i < len(text):
    current_char = text[i]
    current_sequence_length = 1

    for j in range(i + 1, len(text)):
        next_char = text[j]

        if current_char == next_char:
            current_sequence_length += 1
        else:
            break

    result += current_char
    i += current_sequence_length

print(result)

# text = input()
# result = ''
#
# i = 0
# while i < len(text):
#     curr_ch = text[i]
#     current_sequence_length = 1
#
#     for j in range(i + 1, len(text)):
#         next_ch = text[j]
#
#         if curr_ch == next_ch:
#             current_sequence_length += 1
#         else:
#             break
#
#     result += curr_ch
#     i += current_sequence_length
#
# # Set cannot be used because the order of the elements is not guaranteed
# # result = set(text)
# print(result)