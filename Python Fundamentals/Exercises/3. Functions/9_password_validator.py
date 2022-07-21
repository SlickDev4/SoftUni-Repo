def length_is_valid(the_password):
    if 6 <= len(the_password) <= 10:
        return True

    print("Password must be between 6 and 10 characters")
    return False


def symbols_are_valid(the_password):
    if the_password.isalnum():
        return True

    print("Password must consist only of letters and digits")
    return False


def contains_at_least_two_digits(the_password):
    count = 0

    for digit in the_password:
        if digit.isdigit():
            count += 1

    if count >= 2:
        return True

    print("Password must have at least 2 digits")
    return False


password = input()
validated = [length_is_valid(password),
             symbols_are_valid(password),
             contains_at_least_two_digits(password)]

if all(validated):
    print("Password is valid")

