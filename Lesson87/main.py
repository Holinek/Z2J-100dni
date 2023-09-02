# """Zadanie na dzisiaj:
# Mając listę uczniów i ich ocen, użyj list comprehensions, aby utworzyć nową listę z uczniami, którzy otrzymali ocenę
# co najmniej 4.0. Następnie, używając dictionary comprehensions, utwórz słownik, gdzie kluczem będzie imię ucznia,
# a wartością jego ocena.
# Przykładowa lista uczniów i ocen:
# students = [("Ania", 3.5), ("Kamil", 4.5), ("Ola", 4.0), ("Piotr", 5.0), ("Ewa", 3.0)]"""

students = [("Ania", 3.5), ("Kamil", 4.5), ("Ola", 4.0), ("Piotr", 5.0), ("Ewa", 3.0)]

students_with_min_grade = [student for student in students if student[1] >= 4]
student_grade_dict = {student[0]: student[1] for student in students}

print("Uczniowie z oceną co najmniej 4.0:")
print(students_with_min_grade)
print("Słownik ocen uczniów:")
print(student_grade_dict)
