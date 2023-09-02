# Zadanie na dzisiaj:
# Napisz kod, który pyta użytkownika o wiek i sprawdza, czy jest on pełnoletni. Jeśli tak, to program powinien
# wyświetlić "Jesteś pełnoletni!", w przeciwnym razie "Nie jesteś jeszcze pełnoletni.".
# (Pamiętaj, żeby wiek pobierać jako liczbę).

wiek = int(input("Ile masz lat?\n"))
if wiek >= 18:
    print("Jesteś pełnoletni!")
elif wiek < 18 and wiek > 0:
    print("Nie jesteś jeszcze pełnoletni.")
else:
    print("Nie wprowadzono prawidłowej odpowiedzi")
