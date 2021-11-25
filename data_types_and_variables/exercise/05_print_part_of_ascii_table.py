start = int(input())
end = int(input())

for i in range(start, end + 1):
    ch = chr(i)

    if i == end:
        print(f"{ch}")
    else:
        print(f"{ch}", end=" ")