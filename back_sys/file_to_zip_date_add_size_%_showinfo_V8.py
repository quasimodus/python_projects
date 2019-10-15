import shutil
import pathlib
import time
import os
from tkinter import messagebox as mb

# =============================================================
# ИСХОДНЫЕ ДАННЫЕ
ip_base = "Имидж Принт_основная"
ip = "ИмиджПринт"
ktn = "Каэтана"
sft = "ТК Свифт 8_2"

src_path = "\\\server\\1C\\"  # путь к файлу исходнику
target_path = "E:\\1C_back\\auto_backup\\"  # директория куда сохранится архив файла
# ==============================================================
list_of_firms = [ip_base, ip, ktn, sft]

# Создание новой папки =========================================
get_time = time.strftime("%Y-%m-%d-%H.%M", time.localtime())
new_path = r'E:\1C_back\auto_backup\1C_back_' + get_time
if not os.path.exists(new_path):
    os.makedirs(new_path)
# ===============================================================
for firm in list_of_firms:

    file_to_zip = firm  # имя исходного файла
    target_path2 = new_path + "\\"  # директория куда сохранится архив файла

    try:
        # Выполнение архивации по указанному пути
        shutil.make_archive(target_path2 + firm + '_' + get_time, 'zip', src_path, file_to_zip)

    except pathlib:

        mb.showinfo("Сообщение", "Ой! Что-то пошло не так!")

    finally:

        # ниже БАГИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИ
        # размер исходного файла ==========================================

        # b = str((os.path.getsize(src_path + file_to_zip)) // 1000)
        # print(b + 'Kb')

        # размер полученного файла =========================================

        # name_archive_file = ('1C_back' + a + '.zip')
        # z = str((os.path.getsize(target_path + name_archive_file)) // 1000)
        # print(z + 'Kb')

        # ======= Расчет процента сжатия ===================================

        # before = int(b)
        # after = int(z)
        # # prc = str(round(((1-(after / before)) * 100), 1))

        # Вывод сообщения с полной информацией ==============================

        # Git Test

        mb.showinfo("Сообщение",
                    "Бекап готов!\nРасположение архива: {0}\nПуть к источнику: {1}".format(target_path2, src_path))
