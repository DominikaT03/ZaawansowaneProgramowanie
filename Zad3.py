def czy_parzysta(liczba):
    return liczba % 2 == 0
wynik = czy_parzysta(10)
if wynik:
    print("Liczba parzysta")
else:
    print("Liczpa nieparzysta")