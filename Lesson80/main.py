# Twoim zadaniem jest napisanie prostego skracacza adresów URL, który będzie umożliwiał skracanie długich adresów
# internetowych do krótszych, łatwiejszych do zapamiętania wersji. Program powinien zapisywać skrócone (oraz pełne)
# adresy do pliku, a następnie odczytywać je przy kolejnym uruchomieniu.
# Wymagania:
# 1.Napisz program, który wczytuje adres URL od użytkownika.
# 2.Program powinien generować unikalny krótki identyfikator dla każdego adresu URL.
# 3.Pary adresów powinny być zapisywane w pliku w formacie tekstowym
# 4.Przy uruchomieniu programu, wczytaj zapisane wcześniej adresy z pliku.
# 5.Użytkownik powinien mieć możliwość wprowadzenia skróconego adresu, aby uzyskać pierwotny, długi adres URL.
# Sugestie:
# 1.Użyj funkcji skrótu (np. hashlib w Pythonie) do generowania unikalnych identyfikatorów dla adresów URL.
# 2.Zastanów się nad zastosowaniem algorytmu Base62 do konwersji identyfikatorów na krótsze ciągi znaków.
# 3.Aby sprawdzić, czy dany skrócony adres URL istnieje, użyj struktury danych, takiej jak słownik (dictionary) w
# Pythonie.

# coding=UTF-8
import hashlib
import base64
import os

FILE_NAME = "url_shortener.txt"


def save_to_file(short_url, original_url):
    with open(FILE_NAME, "a") as f:
        f.write(f"{short_url} {original_url}\n")


def load_urls():
    if not os.path.exists(FILE_NAME):
        return {}

    url_dict = {}
    with open(FILE_NAME, "r") as f:
        for line in f:
            short_url, original_url = line.strip().split()
            url_dict[short_url] = original_url

    return url_dict


def generate_short_url(original_url):
    hash_obj = hashlib.sha256(original_url.encode("utf-8"))
    hash_str = hash_obj.hexdigest()
    b64_encoded = base64.b64encode(hash_str.encode("utf-8"))[:6]
    short_url = b64_encoded.decode("utf-8").replace("/", "_").replace("+", "-")
    return short_url


def main():
    url_dict = load_urls()

    while True:
        user_input = input("Podaj adres URL lub skrócony adres URL (q aby zakończyć): ")

        if user_input == "q":
            break

        if user_input in url_dict:
            print(f"Oryginalny adres URL: {url_dict[user_input]}")
        else:
            short_url = generate_short_url(user_input)
            if short_url not in url_dict:
                save_to_file(short_url, user_input)
                url_dict[short_url] = user_input
                print(f"Skrócony adres URL: {short_url}")
            else:
                print("Skrót już istnieje. Spróbuj ponownie.")


if __name__ == "__main__":
    main()
