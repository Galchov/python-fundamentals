word = input()

while not word == "end":
    print(f"{word} = {word[::-1]}")
    word = input()

# text = input()
# while text != "end":
#     text_reversed = ""
#     for ch in reversed(text):
#         text_reversed += ch
#     print(text + " = " + text_reversed)
#     text = input()
