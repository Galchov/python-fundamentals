version = input().split(".")
version_string = "".join(version)

version_num = int(version_string)
version_num += 1

next_version_string = str(version_num)
next_version = list(next_version_string)

print(f"{'.'.join(next_version)}")
