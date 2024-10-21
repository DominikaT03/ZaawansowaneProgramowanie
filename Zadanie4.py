def wyswietl_drugi(liczby):
    for i in range(len(liczby)):
        if i % 2 == 1:
            print(liczby[i])
lista_liczb=list(range(10))
wyswietl_drugi(lista_liczb)