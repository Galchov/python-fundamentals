def password_validator(text):
    """Checks if the input password is valid
    according to the requirements"""

    is_valid = True

    if len(text) < 6 or len(text) > 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")

    for el in text:

        if not el.isdigit() and not el.isalpha():
            is_valid = False
            print("Password must consist only of letters and digits")
            break

    digits_counter = 0

    for sym in text:
        if sym.isdigit():
            digits_counter += 1

    if digits_counter < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    if is_valid:
        print("Password is valid")


password = input()

password_validator(password)

# def is_password_lenght_valid(password: str):
#
#     if 6 <= len(password) <= 10:
#         return True
#
#     return False
#
# def is_password_alphanumberic(password: str):
#
#     is_alphanum = True
#
#     for ch in password:
#         if not (ch.isalpha() or ch.isdigit()):
#             is_alphanum = False
#             break
#
#     return is_alphanum
#
# def does_password_have_at_least_two_digits(password: str):
#
#     digits_count = 0
#
#     for ch in password:
#         if ch.isdigit():
#             digits_count += 1
#
#     if digits_count >= 2:
#         return True
#     else:
#         return False
#
# def validate_password(password: str):
#
#     is_valid = True
#
#     if not is_password_lenght_valid(password):
#         print("Password must be between 6 and 10 characters")
#         is_valid = False
#
#     if not is_password_alphanumberic(password):
#         print("Password must consist only of letters and digits")
#         is_valid = False
#
#     if not does_password_have_at_least_two_digits(password):
#         print("Password must have at least 2 digits")
#         is_valid = False
#
#     if is_valid:
#         print("Password is valid")
#
# new_password = input()
#
# validate_password(new_password)