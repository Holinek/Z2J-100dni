# Napisz program w Pythonie, który zorganizuje pliki tekstowe z folderu "źródłowego" do folderów "docelowych"
# na podstawie ich rozszerzeń.
# Przykładowo, wszystkie pliki .txt powinny zostać przeniesione do folderu txt, a pliki .csv do folderu csv.
# Kroki do wykonania zadania:
# 1.Utwórz folder źródłowy source oraz kilka plików tekstowych z różnymi rozszerzeniami, takimi jak .txt, .csv i .md.
# 2.Napisz program, który:
# a. Wyszuka wszystkie pliki tekstowe w folderze źródłowym.
# b. Dla każdego pliku utworzy folder docelowy (jeśli jeszcze nie istnieje) na podstawie rozszerzenia pliku.
# c. Przeniesie plik do odpowiedniego folderu docelowego.
# Miłej zabawy :)

import os
import shutil


def organize_files(source_folder):
    for file_name in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, file_name)):
            file_extension = os.path.splitext(file_name)[1]
            destination_folder = os.path.join(source_folder, file_extension[1:])

            if not os.path.exists(destination_folder):
                os.mkdir(destination_folder)
                print(f"Utworzono folder {destination_folder}")

            source_file = os.path.join(source_folder, file_name)
            destination_file = os.path.join(destination_folder, file_name)
            shutil.move(source_file, destination_file)
            print(f"Przeniesiono plik {file_name} do {destination_folder}")


source_folder = "source"
organize_files(source_folder)
