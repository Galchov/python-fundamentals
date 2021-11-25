import math

n = int(input())
p = int(input())

res = n // p
reminder = n % p

if reminder == 0:
    print(res)
else:
    print(res + 1)