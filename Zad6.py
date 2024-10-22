def funkcja (lista1, lista2):
    lista = list(set(lista1+lista2))
    lista_wynikowa=[x**3 for x in lista]
    return lista_wynikowa
lista1=[1,2,3,4,5]
lista2=[2,3,4,5,6]
wynik=funkcja(lista1,lista2)
print(wynik)
