# Zadanie na dzisiaj:
# BARDZO proste :)
# Napisz program, który oblicza pole powierzchni koła i wypisuje wynik z zaokrągleniem do dwóch miejsc po przecinku.
# Użyj f-stringów do formatowania wydruku.
# 1.Poproś użytkownika o podanie promienia koła (r) jako liczby zmiennoprzecinkowej.
# 2.Oblicz pole powierzchni koła za pomocą wzoru: pole = π * r^2 (możesz użyć wartości pi z modułu math).
# 3.Wypisz wynik zaokrąglony do dwóch miejsc po przecinku, używając f-stringów.

import math

r = float(input("Podaj promień koła - liczba zmiennoprzecinkowa: "))
print(f"Wynik pola o wartości {r} równa się {math.pi * r**2:.2f}")
