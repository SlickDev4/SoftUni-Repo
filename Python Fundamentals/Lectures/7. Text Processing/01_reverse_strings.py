while True:
    text = input()
    if text == "end":
        break
    reversed_string = text[::-1]
    print(f"{text} = {reversed_string}")
