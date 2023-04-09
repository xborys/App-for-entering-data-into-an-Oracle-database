import random

def generuj_pesel():
    miesiace_31 = [1, 3, 5, 7, 8, 10, 12] # miesiące z 31 dniami
    miesiac = random.randint(1, 12)
    if miesiac in miesiace_31:
        dzien = random.randint(1, 31)
    elif miesiac == 2:
        if random.randint(0, 1):
            dzien = random.randint(1, 28)
        else:
            dzien = random.randint(1, 29)
    else:
        dzien = random.randint(1, 30)

    rok = random.randint(1900, 2099)
    rok_str = str(rok)[2:]

    miesiac_str = f'{miesiac:02d}'
    dzien_str = f'{dzien:02d}'

    liczby = [random.randint(0, 9) for _ in range(4)]
    liczby_str = ''.join(str(liczba) for liczba in liczby)

    suma_kontrolna = (9 * int(rok_str[0]) + 7 * int(rok_str[1]) + 3 * int(miesiac_str[0]) + 1 * int(miesiac_str[1]) + 9 * int(dzien_str[0]) + 7 * int(dzien_str[1]) + 3 * liczby[0] + 1 * liczby[1] + 9 * liczby[2] + 7 * liczby[3]) % 10
    pesel = f'{rok_str}{miesiac_str}{dzien_str}{liczby_str}{suma_kontrolna}'

    return pesel
