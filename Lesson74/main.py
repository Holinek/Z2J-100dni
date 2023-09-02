# Stwórz moduł o nazwie text, który zawiera następujące funkcje:
# 1.small_letters(s): Zmienia wszystkie litery w tekście na małe.
# 2.large_letters(s): Zmienia wszystkie litery w tekście na wielkie.
# Następnie zaimportuj te funkcje do głównego pliku i użyj ich, aby zmienić tekst wprowadzony przez użytkownika.

import text

prompt = input("Wypisz tekst, który zostanie zostanie wypisany małymi literami: ")
print(text.small_letters(prompt))
prompt = input("Wypisz tekst, który zostanie zostanie wypisany dużymi literami: ")
print(text.large_letters(prompt))
