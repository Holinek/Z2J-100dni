# Zadanie na dzisiaj:
# Czas na sprawdzenie, czy rozumiesz rozwiązanie. Wypisz na ekranie wyniki tabliczki mnożenia od 1 do 100.
# Zadanie dodatkowe:
# Zrób to zadanie, ale formatując wyjściowy rezultat w tablicy 10 x 10."""

for a in range(1, 11):
    for b in range(1, 11):
        if b == 10:
            print(a*b, end="\n")
        else:
            print(a*b, end="\t")
