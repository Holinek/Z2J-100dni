# Stwórz plik tekstowy zawierający następujące dane:
# Chleb,2.50
# Mleko,2.99
# Jajka,8.50
# Ser,12.99
# Masło,6.99
# Cukier,3.20
# Teraz napisz program, który odczyta plik tekstowy zawierający listę tych produktów.
# Następnie program powinien wyświetlić na ekranie nazwy produktów, których cena jest mniejsza niż 8 złotych.
file_path = "plik.txt"
produkty = {}

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        nazwa, cena = line.strip().split(",")
        produkty[nazwa] = float(cena)

for nazwa, cena in produkty.items():
    if cena < 8:
        print(nazwa, cena)
