# Dzisiaj mega proste zadanko.
# Napisz kod, który będzie prosił o dwie liczby i będzie je dzielił.
# Zadbaj przy pomocy try / except, o blokadę dzielenia przez 0.

print("Witaj w programie do dzielenia")
pierwsza = float(input("Podaj pierwszą liczbę: "))
druga = float(input("Podaj drugą liczbę: "))

try:
    print("Wynik =", pierwsza / druga)
except ZeroDivisionError:
    print("Cholero, nie dziel przez zero!")
