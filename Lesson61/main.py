# Napisz program, który losuje 5 liczb całkowitych z zakresu od 1 do 10, a następnie prosi użytkownika o odgadnięcie co
# najmniej jednej z tych liczb. Program powinien odpowiedzieć, czy podana przez użytkownika liczba była jedną z
# wylosowanych lub nie.
import random

print("Witaj w losowaniu z zakresu od 1 do 10.")
while True:
    losowa = random.sample(range(1, 11), k=5)
    podana_liczba = input("Podaj liczbę od 1 do 10 i sprawdź czy trafiłeś "
                          "(wpisz pustą wartość i wciśnij Enter, aby zakończyć): ")
    if podana_liczba == "":
        print("Program został zakończony!")
        break

    try:
        podana_liczba = int(podana_liczba)
        if podana_liczba in losowa:
            print("Trafiłeś! Wylosowane liczby to:", losowa)
        elif podana_liczba > 10:
            print("Błędny zakres liczb! Losowane liczby są z zakresu od 1 do 10")
        else:
            print("Nie trafiłeś! Wylosowane liczby to:", losowa)

    except ValueError:
        print("Błąd! Wprowadź poprawną liczbę całkowitą.")
