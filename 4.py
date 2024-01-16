import csv
import random

with open('students_new.csv', 'r', encoding='utf8') as f:  # Откроем новый файл
    reader = list(csv.DictReader(f, delimiter=','))  # Получим данные
    f.close()


def create_pass():  # Объявим функцию для создания паролей из больших, малых букв английского алфавита и цифр
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    nums = '0123456789'
    new_pass = ''  # Инициализируем строку, которая будет паролем
    for _ in range(7):
        new_pass += random.choice(random.choice([alphabet_upper, alphabet_lower,
                                                 nums]))  # С помощью метода choice библиотеки random будем выбирать случайные буквы разных регистров и цифр
    new_pass += random.choice(
        alphabet_upper)  # Для того, чтобы учесть условие обязательного наличия большой буквы -- добавим ее принудительно последней, во избежание случая, когда в пароле она отсутствует в первых 6 символах
    return new_pass  # Вовзращаем пароль


# print(create_pass()) #  Проверяем функцию на работоспособность

fieldnames = list(reader[0].keys())  # Получаем Fieldnames
fieldnames.append('login')  # добавляем в поле Fieldnames -- строки логин и пароль
fieldnames.append('password')

values = list(map(lambda x: (','.join(list(x.values())), x['Name'].split(' ')), reader))  # Смотрим значения по именам
print(values)

values = list(map(lambda x: f'{x[0]},{x[1][0]}_{x[1][1][0]}{x[1][2][0]},{create_pass()}',
                  values))  # преобразуем значения под новый необходимый вид
print(values)

new_dicts_list = []  # Создаем массив для того, чтобы добавлять в него словари
for val in values:
    new_dict = {}
    for _, __ in zip(fieldnames, val.split(',')):
        new_dict[_] = __
    new_dicts_list.append(new_dict)

with open('students_password.csv', 'w', encoding='utf8') as ff:  # Открываем новый файл на запись
    writer = csv.DictWriter(ff, delimiter=',',
                            fieldnames=fieldnames)  # Создаем объект writer модуля csv для записи словарей в новый csv файл
    writer.writeheader()
    writer.writerows(new_dicts_list)
    ff.close()
