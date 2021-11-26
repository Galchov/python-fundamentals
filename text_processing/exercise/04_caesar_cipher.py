text = input()

# Here we store the encrypted message
encrypted_text = ""

# Here we use Caesar cipher to encrypt the message
for ch in text:
    current_char_code = ord(ch)

    encrypted_char = chr(current_char_code + 3)

    encrypted_text += encrypted_char

print(encrypted_text)


# ONE LINE ->
# print(''.join([chr(ord(ch) + 3)for ch in input()]))