def is_winning(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    left_side = ticket[:10]
    right_side = ticket[10:]
    symbols = ['@', '#', '$', '^']
    for symbol in symbols:
        for repetition in range(10, 5, -1):
            symbol_repetition = symbol * repetition
            if symbol_repetition in left_side and symbol_repetition in right_side:
                if repetition == 10:
                    return f'ticket "{ticket}" - {repetition}{symbol} Jackpot!'
                return f'ticket "{ticket}" - {repetition}{symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for ticket in tickets:
    print(is_winning(ticket))
