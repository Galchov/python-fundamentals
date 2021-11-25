def data_type(input_data, sym):

    if input_data == "int":
        sym = int(sym)

        action = sym * 2

        return action

    if input_data == "real":
        sym = float(sym)

        action = sym * 1.5

        return f"{action:.2f}"

    if input_data == "string":
        sym = str(sym).split()

        sym.insert(0, "$")
        sym.append("$")

        return "".join(sym)

text = input()
value = input()

print(data_type(text, value))