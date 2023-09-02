# Zadanie dodatkowe:
# Stwórz listę przechowującą nazwy Twoich ulubionych napojów. Następnie, przy pomocy komendy if (poznanej niedawno),
# wyświetl na ekranie "Ta nazwa jest krótka", jeśli nazwa 1 elementu listy jest krótsza od 10 znaków, lub
# "Ta nazwa jest długa", jeśli jest dłuższa niż 10 znaków. Dla przypomnienia, określenie długości tekstu było w lekcji 9

napoje = ["Sprite", "Pepsi", "Fanta", "Woda"]
x = len(napoje[0])
if x < 10:
    print("Ta nazwa jest krótka")
elif x > 10:
    print("Ta nazwa jest długa")
