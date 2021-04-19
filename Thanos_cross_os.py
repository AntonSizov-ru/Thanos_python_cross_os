import os
import random


dir = input(r'Укажите путь к папке с файлами:').strip()
if os.name == 'nt':  # путь по умолчанию
    dir1 = r'C:\python_project\temp'
else:
    dir1 = r'/bin'
only_files = []

if dir == '':
    dir = dir1
else:
    dir = dir

files = list(os.listdir(dir))
random.shuffle(files)
for file in files:
    if os.path.isfile(os.path.join(dir, file)):
        print("беру файл")
        if files.index(file) % 2 == 0:
            only_files.append(file)
            print("тут ведь чистая математика")
            os.remove(os.path.join(dir, file))
    else:
        print("тутки папка вроде")
        continue

print(only_files, 'возрадуйтесь файлы ибо вам пришла смерть от Владыки Таноса')