# Stwórz program, który będzie przechowywał słownik z nazwami państw i ich stolicami.
# Następnie poproś użytkownika o podanie nazwy państwa, a program ma wyświetlić stolicę tego państwa.
# Jeśli użytkownik poda nazwę państwa, której nie ma w słowniku, program powinien wyświetlić komunikat o błędzie.
def capital_of(country):
    countries = {
        "Polska": "Warszawa",
        "Niemcy": "Berlin",
        "Francja": "Paryż",
        "Włochy": "Rzym"
    }
    if country in countries:
        return countries[country]


def get_country(prompt):
    while True:
        country = input(prompt)
        country = country.capitalize()
        if country in ["Polska", "Niemcy", "Francja", "Włochy"]:
            return country
        elif country.lower() == "exit":
            return False
        else:
            print("Błędne Państwo, spróbuj ponownie")


def print_capital(capital):
    if capital:
        print(capital)


def run_program():
    while True:
        country = get_country("Podaj nazwę państwa lub wpisz 'exit' aby zakończyć: ")
        if not country:
            break
        capital = capital_of(country)
        print_capital(capital)


def desc():
    print("Witaj w programie, który poda Ci stolicę wskazanych Państw")
    print("Lista dostępnych Państw: Polska, Niemcy, Francja, Włochy")


desc()
run_program()
