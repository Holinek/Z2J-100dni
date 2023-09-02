# Przygotuj prosty słownik (dosłownie) polsko - angielski. 10-20 wyrazów max. Następnie komputer ma poprosić o wpisanie
# przez Ciebie zdania. Po jego wprowadzeniu ma przetłumaczyć wszystkie wyrazy, które znajdzie w słowniku i wydrukować
# przetworzone zdanie na ekranie. Wyrazy, które odnalazł, mają być przetłumaczone.
# Wyrazy, których nie odnalazł w słowniku. mają być wypisane, tak jak zostały wprowadzone, ale dodatkowo z * na końcu.
# Zadbaj o to, żeby pierwsza litera w zdaniu była pisana dużą literą.
# Przykład.
# Yesterday wieczorem learn się programować*.

slownik = {
    'dlaczego': 'why',
    'wczoraj': 'yesterday',
    'wiem': 'know',
    'i': 'and',
    'ja': 'I',
    'gdzie': 'where',
    'ty': 'you',
    'niebieski': 'blue',
    'czerwony': 'red',
    'czarny': 'black'
}

pobranie_tekstu = input("Podaj zdanie, które chcesz przetłumaczyć z języka polskiego na angielski: ")

rozdzielony_tekst = pobranie_tekstu.split()
zamienione = []

for slowo in rozdzielony_tekst:
    if slowo in slownik:
        zamienione.append(slownik[slowo] + " ")
    else:
        zamienione.append(slowo + "*")

przetlumaczony = ''.join(zamienione)
przetlumaczony = przetlumaczony.capitalize()

print(przetlumaczony)
