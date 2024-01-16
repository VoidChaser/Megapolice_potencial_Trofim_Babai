import csv

with open('students.csv', 'r', encoding='utf8') as f:
    reader = list(csv.DictReader(f,
                                 delimiter=','))  # Объект DictReader класса csv -- необходим, чтобы прочитать данные в формате словарей из csv файла # delimiter -- разделитель, первый аргумент -- имя файл
    f.close()

finded = list(filter(lambda x: x['Name'].startswith('Хадаров Владимир'), reader))[
    0]  # Найдем запись -- словарь нужного нам Владимира Хадарова
print(
    f"Ты получил: {finded['score']}, за проект - {finded['titleProject_id']}")  # Выведем форматированную строку с результатом Владимира

scores = list(map(int, list(filter(lambda y: y != 'None', list(
    map(lambda x: x['score'], reader))))))  # Отфильтруем все результаты, чтобы найти среднее арифметическое
sr_arifm_score = round(sum(scores) / len(scores), 3)  # Найдем среднее арифмитическое

fieldnames = list(
    reader[0].keys())  # Fieldnames -- Имена полей -- первая строка csv файла -- каждое имя -- наименование в словаре

dicts_for_write = []  # Создадим массив, чтобы создать реформатированный словарь, чтобы заменить None на среднее арифмитическое
for _ in reader:
    new_dict_record = {}
    for key, value in _.items():
        if key == 'score' and value == 'None':
            new_dict_record[key] = sr_arifm_score
        else:
            new_dict_record[key] = value
    dicts_for_write.append(new_dict_record)

with open('students_new.csv', 'w', encoding='utf8') as ff:
    writer = csv.DictWriter(ff, delimiter=',', fieldnames=fieldnames)  # Откроем новый файл и запишем в него данные
    writer.writeheader()
    writer.writerows(dicts_for_write)
    ff.close()
