# some_string = input()
#
# for letter in some_string:
#     print(letter * 2, end="")

text = input()
text_2 = str()

for char in text:
    text_2 += char + char

print(text_2)