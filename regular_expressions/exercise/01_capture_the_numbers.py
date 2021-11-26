import re

numbers = []
text = input()
while text:
    numbers.extend(re.findall(r"\d+", text))
    text = input()

print(*numbers)