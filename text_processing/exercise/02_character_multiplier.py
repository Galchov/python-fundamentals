# List of strings/words
words = input().split()
word_one = words[0]
word_two = words[1]

total_sum = 0
shorter_word_length = min(len(word_one), len(word_two))

# Process shorter string
for i in range(shorter_word_length):
    word_one_current = word_one[i]
    word_two_current = word_two[i]

    ch_multiplication = ord(word_one_current) * ord(word_two_current)

    total_sum += ch_multiplication

# If the string have different lengths, we have to process characters of the longer one
longer_word_length = max(len(word_one), len(word_two))

for i in range(shorter_word_length, longer_word_length):
    if len(word_one) > len(word_two):
        current_word_char = word_one[i]
    else:
        current_word_char = word_two[i]

    total_sum += ord(current_word_char)

print(total_sum)