import csv


def insertion_sort(array):  # Создадим функцию сортировки вставками, адаптированную для работы с массивом
    n = len(array)
    for _ in range(1, n):
        x = array[_]
        __ = _

        while __ > 0 and array[__ - 1][1] > x[1]:
            array[__] = array[__ - 1]
            __ -= 1

        array[__] = x
    return array


with open('students_new.csv', 'r', encoding='utf8') as f:  # Откроем новый файл
    reader = list(csv.DictReader(f, delimiter=','))  # Получим информацию из файла
    f.close()

scores = list(map(lambda x: (x['Name'], float(x['score']), x['class']),
                  reader))  # Отфильтруем все результаты, отсортируем их по оценке
# print(insertion_sort(scores))
ten_grade_scores = list(filter(lambda x: x[2].startswith('10'),
                               scores))  # Отфильтруем среди найденых ранее результатов -- записи учеников из 10-ого класса
# print(ten_grade_scores)

print('10 класс:')  # Форматированный вывод
for _, __ in enumerate(ten_grade_scores[::-1],
                       start=1):  # С помощью итератора Enumerate выведем форматированную информацию о победителях из десятокго класса
    print(f"{_} место: {__[0]}")

# scores = list(map(int, list(filter(lambda y: y != 'None', list(map(lambda x: x['score'], reader))))))
# sr_arifm_score = round(sum(scores) / len(scores), 3)

fieldnames = list(reader[0].keys())
