# python

import csv

with open('history_mirror.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    # считываем значения из файла в переменнную reader
    answer = list(reader)[1:]
    # удаляем верхнюю строчку с заголовками столбцов, чтобы она не мешала
    result = []
    # result - список, в который будем записывать результат выполнения программы
    for row in answer:
        # итерируемся по каждой строке таблицы
        if row[2] == 'Победа над смертью':
            result.append([row[0], row[1]])
            print(f'Сообщение было зафиксировано: {row[0]} у пользователя {row[1]}')

with open('mirror_error.csv', 'w', newline='', encoding='utf-8') as file:
    # записываем полученные данные в новый файл mirror_error.csv
    w = csv.writer(file)
    w.writerow(['date', 'username'])
    w.writerows(result)
