# Zadanie na dzisiaj:
# Twoim zadaniem jest napisanie kodu, który:
# 1.	Pobierze plik https://zerotojunior.dev/cezar.txt.
# 2.	Odszyfruje go (i automatycznie wykryje, że plik jest odszyfrowany).
# 3.	Wypisze odszyfrowany tekst na ekranie.
# Punkt 1.
# Możesz rozwiązać, bazując na przykładzie z lekcji.
# Punkt 2.
# Zawartość tekstu jest zaszyfrowana szyfrem Cezara, z użyciem dwóch alfabetów:
# small = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
# large = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ"
# To znaczy tylko, że jeśli litera w tekście była mała, jest przesuwana względem alfabetu small, a jeśli duża, względem
# alfabetu large.
# Co to jest szyfr Cezara?
# https://pl.wikipedia.org/wiki/Szyfr_Cezara
# Szyfr jest bardzo prosty. Wystarczy odgadnąć, jakie jest "przesunięcie".
# Teraz powstaje pytanie, skąd Twój program ma wiedzieć, że udało mu się odszyfrować tekst?
# Można zastosować mały trik.
# Po odszyfrowaniu policz wystąpienie wszystkich liter. Jeśli najwięcej jest liter "e", istnieje wysokie
# prawdopodobieństwo, że odszyfrowanie udało się poprawnie :)
# Jeśli tak nie jest, zwiększ przesunięcie o 1 i rozpocznij od nowa.
# Punkt 3.
# To już tylko chwila radości ;)

import requests
import string

url = 'https://zerotojunior.dev/cezar.txt'

response = requests.get(url)

if response.status_code == 200:
    text = response.content.decode('UTF-8', errors='ignore')

    small_alphabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
    large_alphabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ"

    decrypted = None
    best_match_count = 0
    best_shift = 0

    for shift in range(len(small_alphabet)):
        translated = ''

        for symbol in text:
            if symbol in small_alphabet:
                index = small_alphabet.index(symbol)
                translated += small_alphabet[(index - shift) % len(small_alphabet)]
            elif symbol in large_alphabet:
                index = large_alphabet.index(symbol)
                translated += large_alphabet[(index - shift) % len(large_alphabet)]
            else:
                translated += symbol

        letter_counts = {letter: translated.count(letter) for letter in string.ascii_lowercase}

        if letter_counts.get('e', 0) > best_match_count:
            best_match_count = letter_counts['e']
            best_shift = shift
            decrypted = translated

    if decrypted:
        print("Odszyfrowany tekst:")
        print(decrypted)
    else:
        print("Nie udało się odszyfrować tekstu.")
else:
    print("Nie udało się pobrać pliku.")
