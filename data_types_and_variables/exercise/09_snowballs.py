n = int(input())    # Number of snowballs

highest_snowball_snow = 0
highest_snowball_time = 0
highest_snowball_quality = 0
highest_snowball_value = 0

for snowball in range(1, n + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    if (snowball_snow // snowball_time) ** snowball_quality >= highest_snowball_value:
        highest_snowball_snow = snowball_snow
        highest_snowball_time = snowball_time
        highest_snowball_quality = snowball_quality
        highest_snowball_value = (snowball_snow // snowball_time) ** snowball_quality

print(f"{highest_snowball_snow} : {highest_snowball_time} = {highest_snowball_value} ({highest_snowball_quality})")