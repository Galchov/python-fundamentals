vowels = ["a", "o", "u", "e", "i"]
text = input()

# result = []
# for el in text:
#     if el.lower() not in vowels:
#         result.append(el)
#
# print("".join(result))

result = ("".join([el for el in text if el.lower() not in vowels]))
print(result)