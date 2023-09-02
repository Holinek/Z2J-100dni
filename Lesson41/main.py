# Dzisiaj będzie trudniej :) Masz napisać kalkulator :)
# 1.	Poproś użytkownika o dwie liczby (najpierw jedną, potem drugą)
# 2.	Poproś użytkownika o działanie, jakie ma być wykonane (+,-,/,*)
# 3.	Wyświetl rezultat działania na ekranie :)
# 4.	Wróć na początek.
# 5.	Wpisanie exit powinno zakończyć działanie kalkulatora.
# Ponownie. Masz już CAŁĄ potrzebną wiedzę :)
# Swoją drogą, jak sprytnie użyjesz wiedzy z dzisiejszej lekcji, możesz dodać kontrolę, czy wprowadzone dane są
# poprawne, i jeśli nie, poprosić o podanie właściwych :)
def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


print("Witaj w moim kalkulatorze.")
while True:
    user_choice = input("Jeżeli chcesz kontynuować wciśnij enter. \nJeżeli chcesz zamknąć kalkulator wpisz 'exit'\n")
    user_choice = user_choice.lower()
    if user_choice == "exit":
        break

    try:
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
    except ValueError:
        print("Nieprawidłowe dane wejściowe.")
        continue

    print("Dostępne możliwości wyboru: +, -, *, /.")
    result = input("Wybierz działanie: ")
    result = result.lower()

    while result not in ["+", "-", "*", "/"]:
        print("Nieprawidłowe działanie. Dostępne możliwości wyboru: +, -, *, /.")
        result = input("Wybierz działanie: ")
    if result == "+":
        print("wynik: ", addition(a, b))
    elif result == "-":
        print("wynik: ", subtraction(a, b))
    elif result == "*":
        print("wynik: ", multiplication(a, b))
    elif result == "/":
        if b != 0:
            print("wynik: ", division(a, b))
        else:
            print("Cholero, nie dziel przez zero!")
