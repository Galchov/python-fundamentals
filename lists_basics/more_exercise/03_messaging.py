cipher = input().split()
message = list(input())

decoded_message = []

for symbol in cipher:
    start_cipher = 0
    current_symbol = 0
    current_cipher = list(symbol)
    for num_cipher in range(start_cipher, len(current_cipher)):
        current_symbol += int(current_cipher[num_cipher])
    start_cipher += 1
    if len(message) < current_symbol:
        index = current_symbol - len(message)  # ако цифрата е по-голяма от стринга, стига до края и започва да брои отначало
    else:
        index = current_symbol
    decoded_message.append(message[index])
    message.pop(index)

print("".join(decoded_message))