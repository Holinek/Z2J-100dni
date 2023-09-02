# Stwórz generator hasła.
# 1.	 Hasło musi zawierać co najmniej jedną cyfrę.
# 2.	 Hasło musi zawierać co najmniej jedną dużą literę.
# 3.	 Hasło musi zawierać co najmniej jedną małą literę.
# 4.	 Hasło musi zawierać co najmniej jeden znak specjalny.
# 5.	 Hasło musi mieć między 10 a 15 znaków.
# 6.	 Hasło nie może zawierać znaków "mylących", 1, I, O, 0.
# _Hint
# Wyszukaj w Google: random number generator python
import random

cyfry = "23456789"
duze_litery = "ABCDEFGHJKLMNPRSTUWYZ"
male_litery = "abcdefghjklmnprstuwyz"
znaki_specjalne = "!@#$%^&*-_=~`|/()[]{}:;<>,.?"

haslo = []

haslo.append(random.choice(cyfry))
haslo.append(random.choice(duze_litery))
haslo.append(random.choice(male_litery))
haslo.append(random.choice(znaki_specjalne))

for i in range(0, 11):
    haslo.append(random.choice(cyfry + duze_litery + male_litery + znaki_specjalne))

random.shuffle(haslo[4:16])
haslo = ''.join(haslo)
print(haslo[0:random.randrange(10, 16)])
