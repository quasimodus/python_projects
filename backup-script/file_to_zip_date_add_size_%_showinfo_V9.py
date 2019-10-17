import shutil
import pathlib
import time
import os
from tkinter import messagebox as mb

# ВХОДНЫЕ ДАННЫЕ ===============================================
ip_base = "Имидж Принт_основная"
ip = "ИмиджПринт"
ktn = "Каэтана"
sft = "ТК Свифт 8_2"

src_path = 'C:\\TEST_1C\\'  # путь к файлу исходнику
destination_path = 'C:\\TEST_1C\\auto_backup\\'
# ===============================================================
list_of_firms = [ip_base, ip, ktn, sft]

# Создание новой папки ==========================================
new_time = time.strftime("%Y-%m-%d-%H.%M", time.localtime())
new_path = rf'{destination_path}1C_back_' + new_time
if not os.path.exists(new_path):
    os.makedirs(new_path)
# ===============================================================
for firm in list_of_firms:
    file_to_zip = firm  # имя исходного файла
    target_path = new_path + "\\"  # директория куда сохранится архив файла


    def make_archive(source, destination):
        base = os.path.basename(destination)
        name = base.split('.')[0]
        format = base.split('.')[1]
        archive_from = os.path.dirname(source)
        archive_to = os.path.basename(source.strip(os.sep))
        shutil.make_archive(name, format, archive_from, archive_to)
        shutil.move('%s.%s' % (name, format), destination)

make_archive('/path/to/folder', '/path/to/folder.zip')



    try:
        shutil.make_archive(target_path + firm + '_' + new_time, 'zip', src_path, file_to_zip)
    except pathlib:
        mb.showinfo("Сообщение", "Ой! Что-то пошло не так!")

mb.showinfo("Сообщение", f"Бекап готов!\nРасположение архива: {target_path}\nПуть к источнику: {src_path}")





