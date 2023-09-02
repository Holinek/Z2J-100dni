# Stwórz plik todo.txt.
# Następnie napisz program, który pobierze od użytkownika listę zadań do zrobienia (np. zakupy, sprzątanie, pranie itp.)
# i zapisze je do tego pliku (rozszerzając ten plik o nowe zadania, bez kasowania starych).

file_path = "todo.txt"

while True:
    zadanie = input("Stwórz listę zadań do zrobienia. Jeżeli chcesz zamknąć program wciśnij ENTER(pusta linia): ")
    if not zadanie:
        break
    f = open(file_path, "a", encoding='utf-8')
    try:
        f.write(zadanie + '\n')
    finally:
        f.close()
