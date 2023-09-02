# Zadanie dodatkowe:
# Napisz kod, który pyta użytkownika o ocenę z testu (od 1 do 6) i sprawdza, czy jest ona powyżej lub równa 4. Jeśli
# tak, to program powinien wyświetlić "Gratulacje, zdałeś!", w przeciwnym razie "Niestety, nie zdałeś.". (Pamiętaj, żeby
# ocenę pobierać jako liczbę)

ocena = int(input("Jaką dostałeś ocenę z testu? Od 1 do 6:\n"))
if ocena >= 4 and ocena < 7:
    print("Gratulacje, zdałeś!")
elif ocena < 4 and ocena > 0:
    print("Niestety, nie zdałeś.")
else:
    print("Nie podano prawidłowej oceny (od 1 do 6)")
