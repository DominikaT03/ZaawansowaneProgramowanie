def mnozenie_razy_2(liczby):
    nowe_liczby=[]
    for liczba in liczby:
        nowe_liczby.append(liczba*2)
    return nowe_liczby
lista_liczb=[1,2,3,4,5]
wynik=mnozenie_razy_2(lista_liczb)
print(wynik)

def mnozenie(liczby):
    return [liczba*2 for liczba in liczby]
lista_liczb=[2,3,4,5,6]
wynik=mnozenie(lista_liczb)
print(wynik)