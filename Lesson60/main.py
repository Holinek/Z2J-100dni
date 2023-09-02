# Zadanie na dzisiaj:
# Przed Tobą lista produktów, które trzeba kupić.
# jajka, mleko, chleb, jajka, masło, jajka, jabłka, chleb
# Przygotuj aplikację która.
# 1.Będzie miała wbudowany cennik wszystkich produktów.
# 2.Przygotuje listę zakupów, złożoną z unikalnych produktów oraz podanej obok liczby produktów do kupienia.
# 3.Wyliczy wartość zakupów i poda ją w podsumowaniu.
# Na moje oko, przyda Ci się lista, słownik i zbiór :)

cennik = {
    'jajka': 2.4,
    'mleko': 3.2,
    'chleb': 2.4,
    'masło': 4.8,
    'jabłka': 1.8
}

lista_zakupow = ["jajka", "mleko", "chleb", "jajka", "masło", "jajka", "jabłka", "chleb"]
unikalne_produkty = set(lista_zakupow)

ilosc_produktow = {}
for produkt in lista_zakupow:
    if produkt in ilosc_produktow:
        ilosc_produktow[produkt] += 1
    else:
        ilosc_produktow[produkt] = 1

suma_wartosci = 0
for produkt, ilosc in ilosc_produktow.items():
    cena = cennik.get(produkt, 0)
    suma_wartosci += cena * ilosc

print("Lista zakupów:")
for produkt in unikalne_produkty:
    print("- {}: {} szt.".format(produkt, ilosc_produktow[produkt]))
print("Całkowita wartość zakupów: {} PLN".format(suma_wartosci))
