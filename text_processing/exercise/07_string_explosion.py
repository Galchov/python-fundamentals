text = input()

result_text = ""

i = 0
bomb_power = 0

while i < len(text):
    current_char = text[i]

    if not current_char == ">":
        result_text += current_char
    else:
        result_text += ">"
        bomb_power += int(text[i + 1])

        while bomb_power > 0:
            i += 1

            if i >= len(text):
                break

            current_char = text[i]

            if current_char == ">":
                result_text += ">"
                bomb_power += int(text[i + 1])
            else:
                bomb_power -= 1

    i += 1

print(result_text)

# Simplified solution ->

# text = input()
#
# result_text = ''
#
# i = 0
# bomb_power = 0
# while i < len(text):
#     curr_ch = text[i]
#
#     if curr_ch == '>':
#         # Increase bomb power
#         result_text += '>'
#         bomb_power += int(text[i + 1])
#     else:
#         if bomb_power > 0:
#             # There is bomb activated and we skip characters
#             bomb_power -= 1
#         else:
#             # There is no bomb activated and we append characters
#             result_text += curr_ch
#
#     i += 1
#
# print(result_text)