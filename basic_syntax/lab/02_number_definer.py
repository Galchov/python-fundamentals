number = float(input())

result = ""

if number == 0:
    result = "zero"

elif number > 0:

    if number < 1:
        result = "small positive"
    elif number > 1000000:
        result = "large positive"
    else:
        result = "positive"

else:
    if abs(number) < 1:
        result = "small negative"
    elif abs(number) > 1000000:
        result = "large negative"
    else:
        result = "negative"

print(result)