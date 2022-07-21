text = input().upper()
unique_symbols = ''
current_symbol = ''
repetition = ''
for index in range(len(text)):
    if not text[index].isdigit():
        current_symbol += text[index]
    else:
        for check_next_symbol in range(index, len(text)):
            if not text[check_next_symbol].isdigit():
                break
            repetition += text[check_next_symbol]
        repetition = int(repetition)
        unique_symbols += repetition * current_symbol
        current_symbol = ""
        repetition = ""

print(f"Unique symbols used: {len(set(unique_symbols))}")
print(unique_symbols)



