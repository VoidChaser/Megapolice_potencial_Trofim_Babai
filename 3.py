import csv

with open('students_new.csv', 'r', encoding='utf8') as f:  # откроем новый файл
    reader = list(csv.DictReader(f, delimiter=','))  # Получим данные
    f.close()

id_quote = input()  # Запускаем программу с помощью input, получим запрос
while id_quote != 'СТОП':  # Введем цикл while с остановкой на команде "СТОП"
    try:  # Используем паттерн проверки исключений -- try -- попробуем выполнить код. Он полностью отработает, если не получим исключение -- ошибку питона
        finded = list(filter(lambda x: x['id'] == id_quote, reader))[
            0]  # попробуем найти запись с необходимым id, полученным из input
        print(
            f"Проект № {id_quote} делал(а): {finded['Name']} он получил(а) оценку - {finded['score']}.")  # Форматировано выведем результат, если нашли запись
    except IndexError:  # При ненахождении записи по запросу -- обработаем исключение -- Напишем, что ничего не найдено
        print('Ничего не найдено.')
    id_quote = input()  # Для зацикливания программы снова вызовем запрос команды с помощью input
