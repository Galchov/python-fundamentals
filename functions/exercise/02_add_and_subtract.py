def sum_numbers(first_int, second_int):
    """Returns the sum of the two integers"""

    result = first_int + second_int
    return result

def subtract(third_int):
    """Returns the difference between the
    result of sum_numbers and the third integer"""

    diff = sum_numbers(first_int=number_1, second_int=number_2) - third_int
    return diff

def add_and_subtract(first_int, second_int, third_int):
    """Receives all the three integers and
    returns the other two functions"""

    sum_numbers(first_int, second_int)
    subtract(third_int)


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

add_and_subtract(number_1, number_2, number_3)
print(subtract(number_3))

# def sum_numbers(num_1: int, num_2: int):
#     """Returns the sum of the two arguments"""
#
#     total = num_1 + num_2
#
#     return total
#
# def subtract(sum_1: int, num_3: int):
#     """Returns the difference between sum_numbers
#     and num_3"""
#
#     difference = sum_1 - num_3
#
#     return difference
#
# def add_and_subtract(num_1: int, num_2: int, num_3: int):
#     """Receives all the three integers and
#     returns the other two functions"""
#
#     sum_1 = sum_numbers(num_1, num_2)
#     result = subtract(sum_1, num_3)
#
#     return result
#
# number_1 = int(input())
# number_2 = int(input())
# number_3 = int(input())
#
# print(add_and_subtract(number_1, number_2, number_3))