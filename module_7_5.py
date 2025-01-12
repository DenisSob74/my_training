import os
import time
directory = '.'

#path = os.path.join(r'P:\pythonproject-university\module_7\main.py')
#print(path)

for root, dirs, files in os.walk(directory):

  for file in files:
    filepath = os.path.join(r'P:\pythonproject-university\module_7\main.py')
    filetime = os.path.getmtime(filepath)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(filepath)
    parent_dir = os.path.dirname(filepath)

    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize}'
          f' байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')