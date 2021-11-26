import re

text = input()
pattern = r"\s(?P<email>(?P<user>[A-Za-z0-9]+[A-Za-z0-9\.\-\_]*)\@(?P<host>[A-Za-z]+[A-Za-z\-]*(\.[A-Za-z]+[A-Za-z\-]*)+))"

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group("email"))

# import re
#
# text = input()
# regex = r'\s(?P<mail>[A-Za-z0-9]+[A-Za-z0-9\-\.\_]*\@[A-Za-z]+[A-Za-z\-]*(\.[A-Za-z]+)+)\b'
# print(*[match.group('mail') for match in re.finditer(regex, text)], sep="\n")