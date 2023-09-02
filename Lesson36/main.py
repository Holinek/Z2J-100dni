# Masz przez 3 tygodnie, wykonywać codziennie pięć konkretnych tasków.
# Zadanie A, Zadanie B, Zadanie C, Zadanie D i Zadanie E
# Przygotuj kod, który wypisze na ekranie listę zadań w następujący sposób.
# Dzień tygodnia - numer zadania - opis zadania
# 1 - 1 - Zadanie A
# 1 - 2 - Zadanie B
# 1 - 3 - Zadanie C
# 1 - 4 - Zadanie D
# 1 - 5 - Zadanie E
# 2 - 1 - Zadanie A
# 2 - 2 - Zadanie B
# Itd.

lists = ["A", "B", "C", "D", "E"]

for week in range(1, 4):
    for day in range(1, 6):
        print(week, "-", day, "- Zadanie", lists[day-1])
