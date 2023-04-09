import random

def generate_vin():
    characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    weights = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]

    vin_without_check_digit = ''.join(random.choices(characters, k=16))

    check_digit = sum(characters.index(vin_without_check_digit[i]) * weights[i] for i in range(16)) % 11
    if check_digit == 10:
        check_digit = 'X'
    else:
        check_digit = str(check_digit)

    return vin_without_check_digit + check_digit
