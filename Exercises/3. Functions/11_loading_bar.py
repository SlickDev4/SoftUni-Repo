def loading_bar(number):
    if number % 10 == 0:
        percentage = "%" * int((number / 10))
        dots = "." * (10 - len(percentage))
        if number < 100:
            return f"{number}% [{percentage}{dots}]\nStill loading..."
        return f"{number}% Complete!\n[{percentage}{dots}]"


number_inp = int(input())
print(loading_bar(number_inp))
