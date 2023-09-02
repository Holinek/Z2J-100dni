# Zadanie dodatkowe:
# Narysuj prostokąt o podanych przez użytkownika rozmiarach.
while True:
    try:
        dlugosc = int(input("Podaj długość: "))
        if dlugosc <= 0:
            print("Długość musi być większa od zera")
        else:
            break
    except ValueError:
        print("Nieprawidłowe dane")

while True:
    try:
        wysokosc = int(input("Podaj wysokosc: "))
        if wysokosc <= 0:
            print("Długość musi być większa od zera")
        else:
            break
    except ValueError:
        print("Nieprawidłowe dane")

print("*" * dlugosc)
for y in range(wysokosc - 2):
    print("*" + " " * (dlugosc - 2) + "*")
print("*" * dlugosc)
