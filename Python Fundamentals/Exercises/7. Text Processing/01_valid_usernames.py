def username_length(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def username_symbols(username):
    for element in username:
        if not (element.isalnum() or element == "-" or element == "_"):
            return False
    return True


def username_redundant(username):
    if " " in username:
        return False
    return True


def username_is_valid(username):
    if username_length(username) and username_symbols(username) and username_redundant(username):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if username_is_valid(username):
        print(username)
