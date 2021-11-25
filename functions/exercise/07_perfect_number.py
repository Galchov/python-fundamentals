def perfect_number(num):

    divisors = []

    for n in range(1, num):
        if num % n == 0:
            divisors.append(n)

    if sum(divisors) == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())

print(perfect_number(number))