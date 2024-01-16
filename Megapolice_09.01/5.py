import csv
import random


def hash(s): # Создадим функцию для нахождения хеша строки
    p = 53
    m = 10 ** 9 + 9
    hash_sum = 0
    for _, __ in enumerate(list(s['password'])):
        print(_, __, ord(__))
        hash_sum += ord(__) * (p ** _) % m
    return hash_sum


with open('students_password.csv', 'r', encoding='utf8') as f: # Открываем файл
    reader = list(csv.DictReader(f, delimiter=',')) # Получаем данные
    for _ in reader:
        print(_)
        _['hash'] = hash(_) # добавляем поле Hash в словарь и присваиваем ему вычисленное значение хеш-функции для соответствующего пароля
    print(reader)
    f.close()

with open('students_with_hash.csv', 'w', encoding='utf8') as ff: # Откроем новый файл под запись
    writer = csv.DictWriter(ff, delimiter=';', fieldnames=reader[0].keys()) # Создадим объект writer из модуля csv для записи в новый файл
    writer.writeheader()
    writer.writerows(reader[1:])
    ff.close()