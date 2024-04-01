# python
import csv

def generate_hash(s):
    alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
    d = {l: i for i, l in enumerate(alphabet,1)}
    # словарь с преобразованными символами
    p = 67
    m = 10**9 + 9
    hash_value = 0
    p_pow = 1
    for c in s:
        hash_value = (hash_value + d[c] * p_pow) % m
        # генерация хэша
        p_pow = (p_pow * p) % m
    return int(hash_value)

users_with_hash=[]
with open('history_mirror.csv', encoding="utf8") as csvfile:
    # открываем файл
    reader = list(csv.DictReader(csvfile, delimiter=',', quotechar='"'))
    # считываем в список данные таблицы
    for row in reader:
        row['ID']=generate_hash(row['username'])
        # столбец с названием ID заполняем хэшом для каждого пользователя
        print(row)
        users_with_hash.append(row)
with open('users_with_hash.csv', 'w', newline='', encoding='utf-8') as file:
    # записываем в новый файл новую таблицу с хэшами для каждого пользователя
    w = csv.DictWriter(file, fieldnames=['ID', 'date', 'username', 'verdict'])
    w.writeheader()
    w.writerows(users_with_hash)
