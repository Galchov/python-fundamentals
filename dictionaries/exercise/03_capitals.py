countries = input().split(", ")    # Keys list
capitals = input().split(", ")    # Values list

country_capital_info = dict(zip(countries, capitals))

for key, value in country_capital_info.items():
    print(f"{key} -> {value}")