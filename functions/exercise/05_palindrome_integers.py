def palindrome_check(numbers):
    """Checks if the received integer is a palindrome
    and returns True for palindrome and False if it is not such"""

    for index in range(len(numbers)):
        item_list = []

        for item in numbers[index]:
            item_list.append(item)

        if item_list == item_list[::-1]:
            print(True)
        else:
            print(False)


positive_integers_list = input().split(", ")

palindrome_check(positive_integers_list)
