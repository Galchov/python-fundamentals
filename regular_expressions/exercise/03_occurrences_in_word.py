import re

# We lower the text and the searched word in order to be case-insensitive:
text = input().lower()
word = input().lower()

# This way dynamic pattern is created:
pattern = rf"\b{word}\b"

word_count = len(re.findall(pattern, text))    # Or you can use 'flags=re.IGNORECASE'

print(word_count)

# import re
#
# string_input = input()
# occurrences = input()
# occurrences_count = []
#
# pattern = f"\\b{occurrences}\\b"
#
# matches = re.findall(pattern, string_input, re.IGNORECASE)
#
# if matches:
#     occurrences_count.extend(matches)
#
# print(len(occurrences_count))